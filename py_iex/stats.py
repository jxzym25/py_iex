from .iex import IEX

class Stats(IEX):
    @IEX._call_api_on_func
    def get_intraday(self):
        """
        Returns intraday statistics
        """
        _FUNCTION_KEYS = ("stats", "intraday")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_recent(self):
        """
        This call will return a minimum of the last five trading days up to all trading days of the current month.
        """
        _FUNCTION_KEYS = ("stats", "recent")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_records(self):
        """
        Returns records statistics
        """
        _FUNCTION_KEYS = ("stats", "records")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_historical_summary(self, date=None, format=None):
        """
        The /stats/historical endpoint without any parameters will return the current month's stats.

        Parameters
        Parameter   Details
        date        - Parameter is optional
                    - Value needs to be in four-digit year, two-digit month format (YYYYMM) (i.e January 2017 would be written as 201701)
                    - Historical data is only available for prior months, starting with January 2014
                    - When parameter is not present, request returns prior month's data
        format      - Parameter is optional
                    - Value can only be csv
                    - When parameter is not present, format defaults to JSON
        """
        _FUNCTION_KEYS = ("stats", "historical")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_historical_daily(self, date=None, last=None, format=None):
        """
        This call will return daily stats for a given month or day.
        
        Parameters

        Parameter   Details
        date        - Parameter is optional
                    - Option 1: Value needs to be in four-digit year, two-digit month format (YYYYMM) (i.e January 2017 would be written as 201701)
                    - Option 2: Value needs to be in four-digit year, two-digit month, two-digit day format (YYYYMMDD) (i.e January 21, 2017 would be written as 20170121)
                    - Historical data is only available for prior months, starting with January 2014
        last        - Parameter is optional
                    - Is used in place of date to retrieve last n number of trading days.
                    - Value can only be a number up to 90
        format      - Parameter is optional
                    - Value can only be csv
                    - When parameter is not present, format defaults to JSON
        """
        _FUNCTION_KEYS = ("stats", "historical", "daily")
        return _FUNCTION_KEYS
