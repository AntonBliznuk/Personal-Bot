from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import F, Router

from app.keyboards import main_kb, sub_kb
from app.DataManagement import select_info, sum_money, delete

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    # Handle the /start command
    await message.answer("Привіт, мене звуть Personal Bot, я допоможу тобі стежити за твоїми активами!", reply_markup=main_kb)

@router.message(F.text == "💸Сума всіх активів💸")
async def money_count(message: Message):
    # Handle the request to display the total assets
    await message.answer(sum_money(message.from_user.id))

@router.message(F.text == '💎Криптовалюта💎')
async def crypto_info(message: Message):
    # Handle the request to display cryptocurrency information
    await message.answer(select_info(message.from_user.id, 'cripto'))

@router.message(F.text == '📝Цінні папери📝')
async def shares_info(message: Message):
    # Handle the request to display share information
    await message.answer(select_info(message.from_user.id, 'share'))

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
    # Handle the request to delete all cryptocurrencies
    delete(message.from_user.id, 'cripto')
    await message.answer('Усю вашу криптовалюту було видалено.')

@router.message(F.text == '❌Видалити цінні папери❌')
async def share_delete(message: Message):
    # Handle the request to delete all shares
    delete(message.from_user.id, 'shares')
    await message.answer('Усі ваші цінні папери було видалено.')
