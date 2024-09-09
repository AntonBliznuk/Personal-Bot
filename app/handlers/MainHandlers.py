from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import F, Router

from config import db_menage
from app.keyboards import main_kb, sub_kb

from app.parsers.ShareRate import share_rate_parser
from app.parsers.CryptocurrencyRate import cryptocurrency_rate_parser
from app.parsers.HryvniaRate import hryvnia

def make_message(my_list: list, fun_count) -> str:
    result = ''
    whole_sum = 0
    hryvnia_rate = hryvnia()

    for i in my_list:
        result_fun = fun_count(i[0])
        whole_sum += result_fun * i[1]
        result += f'{i[0].upper()}:\nКурс: {result_fun}\nКількість: {i[1]}\nUSD: {round(result_fun * i[1], 2)}\nUAH: {round(hryvnia_rate * (result_fun * i[1]), 2)}\n\n'

    return result + f'USD: {round(whole_sum, 2)}\nUAH: {round(whole_sum * hryvnia_rate, 2)}'


router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    # Handle the /start command
    await message.answer(f"Привіт {message.from_user.first_name}, мене звуть Personal Bot, я допоможу тобі стежити за твоїми активами!", reply_markup=main_kb)



@router.message(F.text == "💸Сума всіх активів💸")
async def money_count(message: Message):

    final_numb = 0

    result_crypto = db_menage.select_assets_info(message.from_user.id, 'crypto')
    result_share = db_menage.select_assets_info(message.from_user.id, 'share')

    for asset_c in result_crypto:
        final_numb += cryptocurrency_rate_parser(asset_c[0]) * asset_c[1]

    for asset_s in result_share:
        final_numb += share_rate_parser(asset_s[0]) * asset_s[1]

    # Handle the request to display the total assets
    await message.answer(f"UAH -> {round(final_numb * hryvnia(), 2)}\nUSD -> {round(float(final_numb), 2)}")



@router.message(F.text == '💎Криптовалюта💎')
async def crypto_info(message: Message):
    result_crypto = db_menage.select_assets_info(message.from_user.id, 'crypto')
    # Handle the request to display the total assets
    await message.answer(make_message(result_crypto, cryptocurrency_rate_parser))



@router.message(F.text == '📝Цінні папери📝')
async def shares_info(message: Message):
    result_share = db_menage.select_assets_info(message.from_user.id, 'share')
    # Handle the request to display the total assets
    await message.answer(make_message(result_share, share_rate_parser))



@router.message(F.text == '🛠Управління активами🛠')
async def manage_assets(message: Message):
    # Handle the request to display the asset management options
    await message.answer(text='Виберіть дію: ', reply_markup=sub_kb)



@router.message(F.text == '🔴🔴Назад🔴🔴')
async def back(message: Message):
    # Handle the request to go back to the main menu
    await message.answer('Ви повернулися назад', reply_markup=main_kb)



@router.message(F.text == '❌Видалити криптовалюту❌')
async def crypto_delete(message: Message):
    try:
        db_menage.delete_asset_info(message.from_user.id, 'crypto')
        await message.answer('Усю вашу криптовалюту було видалено.')

    except ValueError:
        await message.answer('Ви ще не внесли криптовалюту.')



@router.message(F.text == '❌Видалити цінні папери❌')
async def share_delete(message: Message):
    try:
        db_menage.delete_asset_info(message.from_user.id, 'share')
        await message.answer('Усі ваші цінні папери було видалено.')

    except ValueError:
        await message.answer('Ви ще не внесли цінні папери.')

