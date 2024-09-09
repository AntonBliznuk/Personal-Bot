from aiogram import F, Router, types
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from config import db_menage
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
    if db_menage.is_valid_asset_name(message.text, 'crypto', show_error=False):
        await state.update_data(name=message.text)
        await state.set_state(Cripto.count)
        await message.answer("Введіть кількість.\nПриклад: 1.2")

    else:
        await message.answer("Не вірна назва криптовалюти", reply_markup=sub_kb)
        # Clear the state data
        await state.clear()



@router_cripto.message(Cripto.count)
async def cripto_count(message: Message, state: FSMContext):

    if db_menage.is_valid_amount(message.text, show_error=False):

        await state.update_data(count=message.text)
        data = await state.get_data()
        db_menage.insert_asset_info(message.from_user.id, 'crypto', data['name'], data['count'])

        await message.answer("Дані збережено.", reply_markup=sub_kb)
        await state.clear()

    else:
        await message.answer("Не вірна кількість активу.", reply_markup=sub_kb)
        await state.clear()


