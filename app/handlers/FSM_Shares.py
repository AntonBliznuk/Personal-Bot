from aiogram import F, Router, types
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from config import db_menage
from app.keyboards import sub_kb

router_shares = Router()

# Define states for the shares insertion process
class Shares(StatesGroup):
    name = State()  # State for receiving the name (ticker) of the share
    count = State()  # State for receiving the amount of the share

@router_shares.message(F.text == '✅Внести цінні папери✅')
async def shares_insert(message: Message, state: FSMContext):
    # Set the state to `Shares.name` for receiving the share ticker
    await state.set_state(Shares.name)
    # Prompt the user to enter the ticker of the share
    await message.answer('Введіть тикер активу.\nПриклад: aapl, googl, nvda, AMZN',
                         reply_markup=types.ReplyKeyboardRemove())


@router_shares.message(Shares.name)
async def shares_name(message: Message, state: FSMContext):
    if db_menage.is_valid_asset_name(message.text, 'share', show_error=False):
        await state.update_data(name=message.text)
        await state.set_state(Shares.count)
        await message.answer('Введіть кількість.\nПриклад: 1.0, 2.3')
    else:
        await message.answer("Не вірна назва активу.", reply_markup=sub_kb)
        await state.clear()



@router_shares.message(Shares.count)
async def shares_count(message: Message, state: FSMContext):

    # Update the state data with the received amount
    if db_menage.is_valid_amount(message.text, show_error=False):
        await state.update_data(count=message.text)
        data = await state.get_data()
        db_menage.insert_asset_info(message.from_user.id, 'share', data['name'], data['count'])
        await message.answer('Дані збережено.', reply_markup=sub_kb)
        await state.clear()

    else:
        await message.answer('Не вірна кількість активу.', reply_markup=sub_kb)
        await state.clear()
