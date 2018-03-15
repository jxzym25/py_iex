from ..py_iex.iex import IEX
from ..py_iex.stocks import Stocks
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
