[![Build Status](https://travis-ci.org/jxzym25/py_iex.svg?branch=master)](https://travis-ci.org/jxzym25/py_iex)
[![PyPI version](https://badge.fury.io/py/py_iex.svg)](https://badge.fury.io/py/py_iex)
[![BCH compliance](https://bettercodehub.com/edge/badge/jxzym25/py_iex?branch=master)](https://bettercodehub.com/)

# py_iex
IEX delivers a free API for real time financial data. The module implements a
python interface to the free API provided by IEX.

Data provided for free by IEX. https://iextrading.com/developer/
API Exhibit A. https://iextrading.com/api-exhibit-a

You see all avaialbe APIs in IEX's document https://iextrading.com/developer/docs/

## Install
To install the package use:
```shell
pip install py_iex
```
If you want to install from source, then use
```shell
git clone https://github.com/jxzym25/py_iex.git
pip install -e py_iex
```

## Usage
To get data in python, simply import the library and call the objec for realtime
finance data. Classes include Stocks, ReferenceData, MarketData, Stats, Markets.

```python
from py_iex.stocks import Stocks
st = Stocks()
# get json object with the price information
data = st.get_price('AAPL')

from py_iex.reference_data import ReferenceData
ref = ReferenceData()
# get list of symbols from reference data
symbols = ref.get_symbols()

from py_iex.market_data import MarketData
md = MarketData()
# get trade data for executions on IEX
data = md.get_last(symbols='AAPL')

from py_iex.stats import Stats
stats = Stats()
# get historical summary of certain month
summary = stats.get_historical_summary(date='201803')

from py_iex.markets import Markets
m = Markets()
# get traded volume on the markets
data = m.get_market()
```
Internally there is a retries counter, which used to minimize connection errors
 (in case that the api is not able to respond in time). The default is set to 5.
```python
st = Stocks(retries=YOUR_RETRIES)
```
You can use help to see all the modules/functions available now.

The library currently only supports giving its results as json dictionaries or
list of json dictionaries.
