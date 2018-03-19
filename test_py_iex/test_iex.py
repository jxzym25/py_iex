from ..py_iex.iex import IEX
from ..py_iex.stocks import Stocks
from ..py_iex.reference_data import ReferenceData
from ..py_iex.market_data import MarketData
from ..py_iex.stats import Stats
from ..py_iex.markets import Markets
import unittest
import sys
import os
import requests

class TestIEX(unittest.TestCase):
    _API_EQ_NAME_TEST = "aapl"

    def test_handle_api_call(self):
        """
        Test that api call returns a json file as requested
        """
        iex = IEX()
        url = "https://api.iextrading.com/1.0/stock/aapl/batch?symbols=aapl&types=quote&range=1m&last=5"
        data = iex._handle_api_call(url)
        self.assertIsInstance(data, dict, 'Result data must be a dict')

    def test_stocks_batch(self):
        """
        Test that api call returns a json file as requested
        """
        st = Stocks()
        data = st.get_batch(TestIEX._API_EQ_NAME_TEST, "book")
        self.assertIsInstance(data, dict, 'Result data must be a dict')

    def test_stocks_book(self):
        """
        Test that api call returns a json file as requested
        """
        st = Stocks()
        data = st.get_book(TestIEX._API_EQ_NAME_TEST)
        self.assertIsInstance(data, dict, 'Result data must be a dict')

    def test_stock_delayed_quote(self):
        """
        Test that api call returns a json file as requested
        """
        st = Stocks()
        data = st.get_delayed_quote(TestIEX._API_EQ_NAME_TEST)
        self.assertIsInstance(data, dict, 'Result data must be a dict')

    #def test_stock_threshold_securities_csv(self):
    #    """
    #    Test that api call returns a csv file as requested
    #    """
    #    st = Stocks()
    #    data = st.get_threshold_securities("20180103", format="csv")
    #    print data

    def test_reference_data_symbols(self):
        """
        Test that api call returns a json file as requested
        """
        ref = ReferenceData()
        data = ref.get_symbols()
        self.assertIsInstance(data, list, 'Result data must be a list')

    def test_reference_data_corporate_actions(self):
        """
        Test that api call returns a json file as requested
        """
        ref = ReferenceData()
        data = ref.get_corporate_actions("sample")
        self.assertIsInstance(data, list, 'Result data must be a list')

    def test_market_data_last(self):
        """
        Test that api call returns a json file as requested
        """
        md = MarketData()
        data = md.get_last(symbols=TestIEX._API_EQ_NAME_TEST)
        self.assertIsInstance(data, list, 'Result data must be a list')

    def test_stats_historical_daily(self):
        """
        Test that api call returns a json file as requested
        """
        stats = Stats()
        data = stats.get_historical_daily(date="20180301", last=5)
        self.assertIsInstance(data, list, 'Result data must be a list')

    def test_markets(self):
        """
        Test that api call returns a json file as requested
        """
        m = Markets()
        data = m.get_market()
        self.assertIsInstance(data, list, 'Result data must be a list')
 
