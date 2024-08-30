from aiogram import F, Router, types
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.DataManagement import insert_shares
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
    # Update the state data with the received share ticker
    await state.update_data(name=message.text)
    # Set the state to `Shares.count` for receiving the amount
    await state.set_state(Shares.count)
    # Prompt the user to enter the amount of the share
    await message.answer('Введіть кількість.\nПриклад: 1.0, 2.3')

@router_shares.message(Shares.count)
async def shares_count(message: Message, state: FSMContext):
    # Update the state data with the received amount
    await state.update_data(count=message.text)

    # Retrieve all stored data from the state
    data = await state.get_data()
    # Insert the share data into the database
    insert_shares(message.from_user.id, data['name'], data['count'])

    # Notify the user that the data has been saved and show the main keyboard
    await message.answer('Дані збережено.', reply_markup=sub_kb)
    # Clear the state data
    await state.clear()
