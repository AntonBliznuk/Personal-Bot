import unittest
from app.parsers.ShareRate import share_rate_parser
from app.parsers.CryptocurrencyRate import cryptocurrency_rate_parser
from app.parsers.HryvniaRate import hryvnia

class TestCryptocurrencyRateParser(unittest.TestCase):

    def test_valid_rate(self):
        self.assertIsInstance(cryptocurrency_rate_parser('bitcoin'), float)
        self.assertIsInstance(cryptocurrency_rate_parser('toncoin'), float)
        self.assertIsInstance(cryptocurrency_rate_parser('notcoin'), float)

    def test_invalid_rate(self):
        self.assertIsNone(cryptocurrency_rate_parser('not-valid-name'))


class TestShareRateParser(unittest.TestCase):

    def test_valid_rate(self):
        self.assertIsInstance(share_rate_parser('aapl'), float)
        self.assertIsInstance(share_rate_parser('nvda'), float)
        self.assertIsInstance(share_rate_parser('msft'), float)

    def test_invalid_rate(self):
        self.assertIsNone(share_rate_parser('not-valid-name'))


class TestHryvniaRate(unittest.TestCase):

    def test_valit_rate(self):
        self.assertIsInstance(hryvnia(), float)


if __name__ == '__main__':
    unittest.main()
