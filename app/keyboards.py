from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Main keyboard
# This keyboard is presented to users as the main menu with options for total assets, asset management, cryptocurrency, and securities.
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='💸Сума всіх активів💸'), KeyboardButton(text='🛠Управління активами🛠')],
        [KeyboardButton(text='💎Криптовалюта💎'), KeyboardButton(text='📝Цінні папери📝')],
    ],
    resize_keyboard=True,  # This resizes the keyboard to fit the screen
    input_field_placeholder='Виберіть дію: '  # Placeholder text in the input field
)

# Keypad for asset management
# This keyboard appears when users are managing their assets, with options to add or remove cryptocurrency and securities.
sub_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='✅Внести криптовалюту✅'), KeyboardButton(text='✅Внести цінні папери✅')],
        [KeyboardButton(text='❌Видалити криптовалюту❌'), KeyboardButton(text='❌Видалити цінні папери❌')],
        [KeyboardButton(text="🔴🔴Назад🔴🔴")]
    ],
    resize_keyboard=True,  # This resizes the keyboard to fit the screen
    input_field_placeholder='Виберіть дію: '  # Placeholder text in the input field
)

