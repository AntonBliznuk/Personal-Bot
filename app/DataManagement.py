import sqlite3
from app.ShareRate import shares_parser
from app.CryptocurrencyRate import crypto_parser
from app.HryvniaRate import hryvnia

# Connect to the SQLite database (bot.db) and create a cursor object for executing SQL commands
db = sqlite3.connect('bot.db')
cursor = db.cursor()

def create_table():
    # Create a table for cryptocurrency if it does not exist
    cursor.execute('CREATE TABLE IF NOT EXISTS cripto (id INTEGER, name TEXT, count FLOAT)')
    # Create a table for shares if it does not exist
    cursor.execute('CREATE TABLE IF NOT EXISTS shares (id INTEGER, name TEXT, count FLOAT)')
    db.commit()

def insert_cripto(id, name, count):
    # Insert a new record into the cryptocurrency table
    cursor.execute(f'INSERT INTO cripto (id ,name, count) VALUES ({id},"{name}",{count})')
    db.commit()

def insert_shares(id, name, count):
    # Insert a new record into the shares table
    cursor.execute(f'INSERT INTO shares (id ,name, count) VALUES ({id},"{name}",{count})')
    db.commit()

def select_info(id, what):
    data = None
    info_money = None

    if what == 'cripto':
        # Select all records from the cryptocurrency table where the id matches
        data = cursor.execute(f'SELECT * FROM cripto WHERE id = {id}').fetchall()
        # Extract names for parsing
        task = [i[1] for i in data]
        # Parse cryptocurrency information
        info_money = crypto_parser(task)

    elif what == 'share':
        # Select all records from the shares table where the id matches
        data = cursor.execute(f'SELECT * FROM shares WHERE id = {id}').fetchall()
        # Extract names for parsing
        task = [i[1] for i in data]
        # Parse share information
        info_money = shares_parser(task)

    if len(data) == 0:
        return "Записів не знайдено"  # Return message if no records are found

    else:
        message_text = ""
        sum_shares = 0

        for i in range(len(data)):
            name = data[i][1]
            amount = data[i][2]
            price = info_money[data[i][1]][0]
            money = amount * info_money[data[i][1]][1]

            # Format the message text with the details of each record
            message_text += (f'{name}:\n'
                             f'Кількість: {amount}\n'
                             f'Сума в доларах: ${round(float(money), 2)}💰\n'
                             f'Сума в гривнях: ₴{round(float(money) * hryvnia(), 2)}🪙\n'
                             f'Курс: {price}\n\n')

            sum_shares += money

        # Append the total amount summary to the message text
        message_text += (f'Сума: ${round(float(sum_shares), 2)}\n'
                         f'Сума: ₴{round(float(sum_shares) * hryvnia(), 2)}')
        return message_text

def sum_money(id):
    sum_all = 0

    # Select all records from both cryptocurrency and shares tables where the id matches
    cripto = cursor.execute(f'SELECT * FROM cripto WHERE id = {id}').fetchall()
    share = cursor.execute(f'SELECT * FROM shares WHERE id = {id}').fetchall()

    # Extract names for parsing
    task_cripto = [i[1] for i in cripto]
    task_share = [i[1] for i in share]

    # Parse cryptocurrency and share information
    result_cripto = crypto_parser(task_cripto)
    result_share = shares_parser(task_share)

    # Calculate total amount for cryptocurrencies
    for i in range(len(cripto)):
        amount = cripto[i][2]
        money = amount * result_cripto[cripto[i][1]][1]
        sum_all += money

    # Calculate total amount for shares
    for i in range(len(share)):
        amount = share[i][2]
        money = amount * result_share[share[i][1]][1]
        sum_all += money

    # Return the total amount in dollars and hryvnias
    return (f'Сума в долларах: ${round(sum_all, 2)}\n'
            f'Сума в гривнях: ₴{round(sum_all * hryvnia(), 2)}')

def delete(id, what):
    # Delete records from the specified table where the id matches
    cursor.execute(f'DELETE FROM {what} WHERE id = {id};')
    db.commit()
