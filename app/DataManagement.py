import sqlite3
from app.parsers.ShareRate import share_rate_parser
from app.parsers.CryptocurrencyRate import cryptocurrency_rate_parser


class Menager:

    type_list = {'crypto', 'share'}

    def __init__(self, file_path: str) -> None:
        db = sqlite3.connect(file_path)
        cur = db.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS share (user_id INTEGER, asset_name TEXT, amount REAL)")
        cur.execute("CREATE TABLE IF NOT EXISTS crypto (user_id INTEGER, asset_name TEXT, amount REAL)")
        db.commit()

        self.db = db
        self.cur = cur


    def is_valid_asset_type(self, asset_type, show_error=True)-> bool:
        if asset_type == 'all_assets':
            return True

        if asset_type not in Menager.type_list:
            if show_error:
                raise ValueError(f"wrong asset type <{asset_type}>")
            else:
                return False
        return True



    def is_valid_asset_name(self, asset_name, asset_type='all_assets', show_error=True)-> bool:

        if asset_type == 'all_assets':
            if not ((cryptocurrency_rate_parser(asset_name)) or (share_rate_parser(asset_name))):
                if show_error:
                    raise ValueError(f"wrong asset name <{asset_name}>")
                else:
                    return False

        self.is_valid_asset_type(asset_type=asset_type)

        if asset_type == 'crypto':
            if not cryptocurrency_rate_parser(asset_name):
                if show_error:
                    raise ValueError(f"wrong asset name <{asset_name}>")
                else:
                    return False

        elif asset_type == 'share':
            if not share_rate_parser(asset_name):
                if show_error:
                    raise ValueError(f"wrong asset name <{asset_name}>")
                else:
                    return False

        return True



    def is_valid_user_id(self, user_id, asset_type='all_assets', show_error=True) -> bool:

        if asset_type == 'all_assets':
            crypto_result = self.cur.execute("SELECT * FROM crypto WHERE user_id = ?", (user_id, )).fetchone()
            share_result = self.cur.execute("SELECT * FROM share WHERE user_id = ?", (user_id, )).fetchone()
            if not (crypto_result or share_result):
                if show_error:
                    raise ValueError(f"wrong user_id <{user_id}>")
                else:
                    return False

        self.is_valid_asset_type(asset_type=asset_type)

        if asset_type == 'crypto':
            crypto_result = self.cur.execute("SELECT * FROM crypto WHERE user_id = ?", (user_id, )).fetchone()
            if not crypto_result:
                if show_error:
                    raise ValueError(f"wrong user_id <{user_id}>")
                else:
                    return False

        if asset_type == 'share':
            share_result = self.cur.execute("SELECT * FROM share WHERE user_id = ?", (user_id, )).fetchone()

            if not share_result:
                if show_error:
                    raise ValueError(f"wrong user_id <{user_id}>")
                else:
                    return False
        return True



    def is_valid_amount(self, amount, show_error=True)-> bool:
        try:
            amount = float(amount)
        except ValueError:
            return False
        
        if amount <= 0:
            if show_error:
                raise ValueError(f"wrong amount <{amount}>")
            else:
                return False
        return True



    def select_assets_info(self, user_id: int, asset_type='all_assets') -> list:
        if asset_type == 'all_assets':
            crypto = self.cur.execute(f"SELECT asset_name, amount FROM crypto WHERE user_id = ?", (user_id, )).fetchall()
            share = self.cur.execute(f"SELECT asset_name, amount FROM share WHERE user_id = ?", (user_id, )).fetchall()
            return crypto + share

        if self.is_valid_asset_type(asset_type=asset_type):
            result = self.cur.execute(f"SELECT asset_name, amount FROM {asset_type} WHERE user_id = ?", (user_id, )).fetchall()
            return result

        raise ValueError("select_assets_info - Error")



    def insert_asset_info(self, user_id: int, asset_type: str, asset_name: str, amount: float) -> None:
        self.is_valid_amount(amount)
        self.is_valid_asset_type(asset_type)

        if self.is_valid_asset_name(asset_name, asset_type):

            if self.cur.execute(f"SELECT * FROM {asset_type} WHERE user_id = ? and asset_name = ?", (user_id, asset_name)).fetchone() is None:
                self.cur.execute(f"INSERT INTO {asset_type} VALUES (?, ?, ?)", (user_id, asset_name, amount))
                self.db.commit()

            else:
                self.cur.execute(f"UPDATE {asset_type} SET amount = amount + ? WHERE asset_name = ? AND user_id = ?", (amount, asset_name, user_id))
                self.db.commit()


    def delete_asset_info(self, user_id: int, asset_type='all', asset_name='all') -> None:
        self.is_valid_user_id(user_id)

        if asset_type == 'all' and asset_name == 'all':
            self.cur.execute(f"DELETE FROM crypto WHERE user_id = ?", (user_id, ))
            self.cur.execute(f"DELETE FROM share WHERE user_id = ?", (user_id, ))
            self.db.commit()
            return

        elif asset_type == 'all' and self.is_valid_asset_name(asset_name, show_error=False):
            self.cur.execute(f"DELETE FROM crypto WHERE user_id = ? AND asset_name = ?", (user_id, asset_name))
            self.cur.execute(f"DELETE FROM share WHERE user_id = ? AND asset_name = ?", (user_id, asset_name))
            self.db.commit()
            return

        elif asset_name == 'all' and self.is_valid_asset_type(asset_type, show_error=False):
            self.cur.execute(f"DELETE FROM {asset_type} WHERE user_id = ?", (user_id, ))
            self.db.commit()
            return


        elif self.is_valid_asset_type(asset_type) and self.is_valid_asset_name(asset_name, asset_type):
            self.cur.execute(f"DELETE FROM {asset_type} WHERE user_id = ? AND asset_name = ?", (user_id, asset_name))
            self.db.commit()
            return


    def update_asset_info(self, user_id: int, asset_type: str, asset_name: str, new_amount: float) -> None:
        self.is_valid_amount(new_amount)
        self.is_valid_asset_type(asset_type)
        self.is_valid_user_id(user_id, asset_type)
        self.is_valid_asset_name(asset_name, asset_type)

        self.cur.execute(f"UPDATE {asset_type} SET amount = ? WHERE asset_name = ? AND user_id = ?", (new_amount, asset_name, user_id))
        self.db.commit()