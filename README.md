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
finance data.
```python
from py_iex.stocks import Stocks
st = Stocks()
# get json object with the price information
data = st.get_price('AAPL')
```
Internally there is a retries counter, which used to minimize connection errors
 (in case that the api is not able to respond in time). The default is set to 5.
```python
st = Stocks(retries=YOUR_RETRIES)
```
You can use help to see all the modules/functions available now.

The library currently only supports giving its results as json dictionaries.
