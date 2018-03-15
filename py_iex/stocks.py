from .iex import IEX

class Stocks(IEX):
    """
    This class implements all the api calls to stocks
    """
    @IEX._call_api_on_func
    def get_batch(self, symbol, types="quote", symbols=None, range=None):
        """
        Return intraday batched information
        
        Options
        Option  Description
        symbol  Use market to query multiple symbols (i.e. .../market/batch?...)

        Parameters
        Parameter   Details
        types   - Required 
                - Comma delimited list of endpoints to call. The names should match the individual endpoint names. Limited to 10 types.
        symbols - Optional 
                - Comma delimited list of symbols limited to 100. This parameter is used only if market option is used .
        range   - Optional 
                - Used to specify a chart range if chart is used in types parameter.
        *   - Optional 
            - Parameters that are sent to individual endpoints can be specified in batch calls and will be applied to each supporting endpoint.
        """
        
        _FUNCTION_KEYS = ("stock", symbol, "batch")
        return _FUNCTION_KEYS
            
    @IEX._call_api_on_func
    def get_book(self, symbol):
        """
        Return book information

        Options
        Symbol
        """

        _FUNCTION_KEYS = ("stock", symbol, "book")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_chart(self, symbol, range, char_reset=None, chart_simplify=None, chart_interval=None):
        """
        Return chart information

        Options
        Range   Description Source
        5y  Five years  Historically adjusted market-wide data
        2y  Two years   Historically adjusted market-wide data
        1y  One year    Historically adjusted market-wide data
        ytd Year-to-date    Historically adjusted market-wide data
        6m  Six months  Historically adjusted market-wide data
        3m  Three months    Historically adjusted market-wide data
        1m  One month (default) Historically adjusted market-wide data
        1d  One day IEX-only data by minute
        2018-03-14Specific 2018-03-14IEX-only data by minute for a specified date in the format YYYYMMDD if available. Currently supporting trailing 30 calendar days.
        dynamic One day Will return 1d or 1m data depending on the day or week and time of day. Intraday per minute data is only returned during market hours.

        Parameters
        Parameter   Details
        chartReset  - Optional
                    - boolean. If true, 1d chart will reset at midnight instead of the default behavior of 9:30am ET.
        chartSimplify   - Optional
                        - boolean. If true, runs a polyline simplification using the Douglas-Peucker algorithm. This is useful if plotting sparkline charts.
        chartInterval   - Optional
                        - number. If passed, chart data will return every Nth element as defined by chartInterval
        """

        if range not in ("5y", "2y", "1y", "ytd", "6m", "3m", "1m", "1d", "dynamic"):
            _FUNCTION_KEYS = ("stock", symbol, "chart", 'date', range)
        else:
            _FUNCTION_KEYS = ("stock", symbol, "chart", range)
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_company(self, symbol):
        """
        Return company information

        Options
        Symbol
        """

        _FUNCTION_KEYS = ("stock", symbol, "company")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_delayed_quote(self, symbol):
        """
        This returns the 15 minute delayed market quote.

        Options
        Symbol
        """

        _FUNCTION_KEYS = ("stock", symbol, "delayed-quote")
        return _FUNCTION_KEYS
    
    @IEX._call_api_on_func
    def get_dividends(self, symbol, range):
        """
        Return dividends information

        Options
        Symbol

        Range   Description Source
        5y  Five years  Historical market data
        2y  Two years   Historical market data
        1y  One year    Historical market data
        ytd Year-to-date    Historical market data
        6m  Six months  Historical market data
        3m  Three months    Historical market data
        1m  One month (default) Historical market data
        """

        _FUNCTION_KEYS = ("stock", symbol, "dividends", range)
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_earnings(self, symbol):
        """
        Pulls data from the four most recent reported quarters.

        Options
        Symbol
        """

        _FUNCTION_KEYS = ("stock", symbol, "earnings")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_effective_spread(self, symbol):
        """
        This returns an array of effective spread, eligible volume, and price improvement of a stock, by market. Unlike volume-by-venue, this will only return a venue if effective spread is not 'N/A'. Values are sorted in descending order by effectiveSpread. Lower effectiveSpread and higher priceImprovement values are generally considered optimal.
        Effective spread is designed to measure marketable orders executed in relation to the market center's quoted spread and takes into account hidden and midpoint liquidity available at each market center. Effective Spread is calculated by using eligible trade prices recorded to the consolidated tape and comparing those trade prices to the National Best Bid and Offer ("NBBO") at the time of the execution.

        Options
        Symbol
        """

        _FUNCTION_KEYS = ("stock", symbol, "effective-spread")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_financials(self, symbol):
        """
        Pulls income statement, balance sheet, and cash flow data from the four most recent reported quarters.

        Options
        Symbol
        """

        _FUNCTION_KEYS = ("stock", symbol, "financials")
        return _FUNCTION_KEYS

    #@IEX._call_api_on_func
    #def get_threshold_securities(self, date, format=None, token=None):
    #    """
    #    Return IEX Regulation SHO Threshold Securities List

    #    Options
    #    Range   Description Source
    #    2018-03-15Specific 2018-03-15Daily list data for a specified date in the format YYYYMMDD,if available, or sample. If sample, a sample file will be returned

    #    Parameters
    #    Parameter   Details
    #    format  - Parameter is optional
    #            - Value can be csv or psv
    #            - When parameter is not present, format defaults to JSON
    #    token   - Parameter is optional
    #            - Value is the API token from your IEX user account
    #            - If you have been permissioned for CUSIP information you'll receive a CUSIP field, othewise data defaults to exclude CUSIP.
    #    """

    #    _FUNCTION_KEYS = ("stock", "market", "threshold-securities", date)
    #    return _FUNCTION_KEYS
    
    #@IEX._call_api_on_func
    #def get_short_interest(self, date, format=None, token=None):
    #    """
    #    Return IEX Regulation SHO Threshold Securities List

    #    Options
    #    Range   Description Source
    #    2018-03-15Specific 2018-03-15Daily list data for a specified date in the format YYYYMMDD,if available, or sample. If sample, a sample file will be returned

    #    Parameters
    #    Parameter   Details
    #    format  - Parameter is optional
    #            - Value can be csv or psv
    #            - When parameter is not present, format defaults to JSON
    #    token   - Parameter is optional
    #            - Value is the API token from your IEX user account
    #            - If you have been permissioned for CUSIP information you'll receive a CUSIP field, othewise data defaults to exclude CUSIP.
    #    """

    #    _FUNCTION_KEYS = ("stock", "market", "short-interest", date)
    #    return _FUNCTION_KEYS
    
    @IEX._call_api_on_func
    def get_stats(self, symbol):
        """
        Return key stats

        Options
        Symbol
        """

        _FUNCTION_KEYS = ("stock", symbol, "stats")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_list(self, top, display_percent=None):
        """
        Returns an array of quotes for the top 10 symbols in a specified list.

        Options
        Option      Details
        top         Can be ("mostactive", "gainers", "losers", "iexvolume", "iexpercent")

        Parameters
        Parameter   Details
        displayPercent  - Optional
                        - If set to true, all percentage values will be multiplied by a factor of 100 (Ex: /stock/aapl/quote?displayPercent=true)
        """

        _FUNCTION_KEYS = ("stock", "market", "list", top)
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_logo(self, symbol):
        """
        This is a helper function, but the google APIs url is standardized.

        Options
        Symbol
        """

        _FUNCTION_KEYS = ("stock", symbol, "logo")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_news(self, symbol, range):
        """
        Return news information

        Options

        Option  Description
        symbol  Use market to get market-wide news (i.e. .../market/news/...)
        range   Number between 1 and 50. Default is 10. (i.e. .../news/last/1)
        """

        if range:
            _FUNCTION_KEYS = ("stock", symbol, "news", "last", str(range))
        else:
            _FUNCTION_KEYS = ("stock", symbol, "news")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_ohlc(self, symbol):
        """
        Returns the official open and close for a give symbol.

        Options
        Symbol
        """

        _FUNCTION_KEYS = ("stock", symbol, "ohlc")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_peers(self, symbol):
        """
        Return peers information

        Options
        Symbol
        """

        _FUNCTION_KEYS = ("stock", symbol, "peers")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_previous(self, symbol):
        """
        This returns previous day adjusted price data for a single stock, or an object keyed by symbol of price data for the whole market.

        Options
        Symbol
        """

        _FUNCTION_KEYS = ("stock", symbol, "previous")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_price(self, symbol):
        """
        Return price information

        Options
        Symbol
        """

        _FUNCTION_KEYS = ("stock", symbol, "price")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_quote(self, symbol):
        """
        Return quote information

        Options
        Symbol

        Parameters
        Parameter   Details
        displayPercent  - Optional
                        - If set to true, all percentage values will be multiplied by a factor of 100 (Ex: /stock/aapl/quote?displayPercent=true)
        """

        _FUNCTION_KEYS = ("stock", symbol, "quote")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_relevant(self, symbol):
        """
        Return relevant information

        Options
        Symbol
        """

        _FUNCTION_KEYS = ("stock", symbol, "relevant")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_splits(self, symbol, range):
        """
        Return splits information

        Options
        Symbol

        Range   Description Source
        5y  Five years  Historical market data
        2y  Two years   Historical market data
        1y  One year    Historical market data
        ytd Year-to-date    Historical market data
        6m  Six months  Historical market data
        3m  Three months    Historical market data
        1m  One month (default) Historical market data
        """

        _FUNCTION_KEYS = ("stock", symbol, "splits", range)
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_time_series(self, symbol):
        """
        time-series is an alternate way to access the chart endpoint.

        Options
        Symbol
        """
        
        _FUNCTION_KEYS = ("stock", symbol, "time-series")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_volume_by_venue(self, symbol):
        """
        This returns 15 minute delayed and 30 day average consolidated volume percentage of a stock, by market. This call will always return 13 values, and will be sorted in ascending order by current day trading volume percentage.

        Options
        Symbol
        """

        _FUNCTION_KEYS = ("stock", symbol, "volume-by-venue")
        return _FUNCTION_KEYS
