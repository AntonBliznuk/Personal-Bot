import unittest
from app.DataManagement import Menager


class TestIsValidAssetType(unittest.TestCase):

    def setUp(self) -> None:
        self.menager = Menager("/Users/antonbliznuk/Образование/Программирование/Python/ООП свалка/Тг Бот Активы/asset.db")

    def test_valid_asset_type(self):
        self.assertTrue(self.menager.is_valid_asset_type('share'))
        self.assertTrue(self.menager.is_valid_asset_type('crypto'))
        self.assertTrue(self.menager.is_valid_asset_type('all_assets'))

    def test_invalid_asset_type_no_error(self):
        self.assertFalse(self.menager.is_valid_asset_type('stocks', show_error=False))
        self.assertFalse(self.menager.is_valid_asset_type('invalid_type', show_error=False))
        self.assertFalse(self.menager.is_valid_asset_type('cryptocurency', show_error=False))

    def test_invalid_asset_type_with_error(self):
        with self.assertRaises(ValueError):
            self.menager.is_valid_asset_type('invalid_type')



class TestIsValidAssetName(unittest.TestCase):

    def setUp(self) -> None:
        self.menager = Menager("/Users/antonbliznuk/Образование/Программирование/Python/ООП свалка/Тг Бот Активы/asset.db")

    def test_valid_asset_name(self):
        self.assertTrue(self.menager.is_valid_asset_name("aapl"))
        self.assertTrue(self.menager.is_valid_asset_name("bitcoin"))
        self.assertTrue(self.menager.is_valid_asset_name("aapl", 'share'))
        self.assertTrue(self.menager.is_valid_asset_name("toncoin", 'crypto'))

    def test_invalid_asset_name_no_error(self):
        self.assertFalse(self.menager.is_valid_asset_name("aapl", 'crypto', show_error=False))
        self.assertFalse(self.menager.is_valid_asset_name("bitcoin", 'share', show_error=False))
        self.assertFalse(self.menager.is_valid_asset_name("invalid_asset_name", show_error=False))
        self.assertFalse(self.menager.is_valid_asset_name("invalid_asset_name", 'share', show_error=False))
        self.assertFalse(self.menager.is_valid_asset_name("invalid_asset_name", 'crypto', show_error=False))

    def test_invalid_asset_name_with_error(self):
        with self.assertRaises(ValueError):
            self.menager.is_valid_asset_name("aapl", 'crypto')
            self.menager.is_valid_asset_name("bitcoin", 'share')
            self.menager.is_valid_asset_name("invalid_asset_name")
            self.menager.is_valid_asset_name("invalid_asset_name", 'share')
            self.menager.is_valid_asset_name("invalid_asset_name", 'crypto')
            self.menager.is_valid_asset_name("invalid_asset_name", 'invalid_asset_type')


class TestIsValidAmount(unittest.TestCase):

    def setUp(self) -> None:
        self.menager = Menager("/Users/antonbliznuk/Образование/Программирование/Python/ООП свалка/Тг Бот Активы/asset.db")

    def test_valid_amount(self):
        self.assertTrue(self.menager.is_valid_amount(1))
        self.assertTrue(self.menager.is_valid_amount(0.1))
        self.assertTrue(self.menager.is_valid_amount(1365345))

    def test_invalid_amount_no_error(self):
        self.assertFalse(self.menager.is_valid_amount(0, show_error=False))
        self.assertFalse(self.menager.is_valid_amount(-1, show_error=False))
        self.assertFalse(self.menager.is_valid_amount(-12435, show_error=False))

    def test_invalid_amount_with_error(self):
        with self.assertRaises(ValueError):
            self.menager.is_valid_amount(0)
            self.menager.is_valid_amount(-1)
            self.menager.is_valid_amount(-12435)



if __name__ == '__main__':
    unittest.main()
