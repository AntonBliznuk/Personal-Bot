from aiogram import F, Router, types
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.DataManagement import insert_cripto
from app.keyboards import sub_kb

router_cripto = Router()

# Define states for the cryptocurrency insertion process
class Cripto(StatesGroup):
    name = State()  # State for receiving the name of the cryptocurrency
    count = State()  # State for receiving the amount of the cryptocurrency

@router_cripto.message(F.text == '✅Внести криптовалюту✅')
async def cripto_insert(message: Message, state: FSMContext):
    # Set the state to `Cripto.name` for receiving the cryptocurrency name
    await state.set_state(Cripto.name)
    # Prompt the user to enter the name of the cryptocurrency
    await message.answer("Введіть назву криптовалюти.\nПриклад: Bitcoin", reply_markup=types.ReplyKeyboardRemove())

@router_cripto.message(Cripto.name)
async def cripto_name(message: Message, state: FSMContext):
    # Update the state data with the received cryptocurrency name
    await state.update_data(name=message.text)
    # Set the state to `Cripto.count` for receiving the amount
    await state.set_state(Cripto.count)
    # Prompt the user to enter the amount of the cryptocurrency
    await message.answer("Введіть кількість.\nПриклад: 1.2")

@router_cripto.message(Cripto.count)
async def cripto_count(message: Message, state: FSMContext):
    # Update the state data with the received amount
    await state.update_data(count=message.text)

    # Retrieve all stored data from the state
    data = await state.get_data()
    # Insert the cryptocurrency data into the database
    insert_cripto(id=message.from_user.id, name=data['name'], count=data['count'])

    # Notify the user that the data has been saved and show the main keyboard
    await message.answer("Дані збережено.", reply_markup=sub_kb)
    # Clear the state data
    await state.clear()
