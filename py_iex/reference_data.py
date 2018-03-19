from .iex import IEX

class ReferenceData(IEX):
    """
    This class implements all the api calls to reference data
    """
    @IEX._call_api_on_func
    def get_symbols(self, format=None):
        """
        This call returns an array of symbols IEX supports for trading. This list is updated daily as of 7:45 a.m. ET. Symbols may be added or removed by IEX after the list was produced.

        Parameters

        Parameter   Details
        format  - Parameter is optional
                - Value can only be csv
                - When parameter is not present, format defaults to JSON
        """

        _FUNCTION_KEYS = ("ref-data", "symbols")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_corporate_actions(self, date, format=None, token=None):
        """
        This call returns an array of new issues, symbol and name changes, and deleted issues, as well as new firms, name changes, and deleted firms for IEX-listed securities.

        Records are added once known by the Exchange and will be removed when the Effective Date is in the past.

        Updates are posted once per hour from 8:00 a.m. to 6:00 p.m. ET on each trading day

        Options
        Range   Description     Source
        date    Specific date   Daily list data for a specified date in the format YYYYMMDD,if available, or sample. If sample, a sample file will be returned

        Parameters
        Parameter   Details
        format  - Parameter is optional
                - Value can be csv or psv
                - When parameter is not present, format defaults to JSON
        token   - Parameter is optional
                - Value is the API token from your IEX user account
                - If you have been permissioned for CUSIP information you'll receive a CUSIP field, othewise data defaults to exclude CUSIP.
        """

        if date:
            _FUNCTION_KEYS = ("ref-data", "daily-list", "corporate-actions", date)
        else:
            _FUNCTION_KEYS = ("ref-data", "daily-list", "corporate-actions")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_dividends(self, date, format=None, token=None):
        """
        This call details upcoming dividend information and other corporate actions, such as stock splits, for IEX-listed securities.

        Records are added once known by the Exchange. A new record with the same Record ID as a previously communicated record will appear when an existing record is being modified or deleted by the Exchange. All records will be removed each evening.

        Updates are posted once per hour from 8:00 a.m. to 6:00 p.m. ET on each trading day

        Options
        Range   Description     Source
        date    Specific date   Daily list data for a specified date in the format YYYYMMDD,if available, or sample. If sample, a sample file will be returned

        Parameters
        Parameter   Details
        format  - Parameter is optional
                - Value can be csv or psv
                - When parameter is not present, format defaults to JSON
        token   - Parameter is optional
                - Value is the API token from your IEX user account
                - If you have been permissioned for CUSIP information you'll receive a CUSIP field, othewise data defaults to exclude CUSIP.
        """

        if date:
            _FUNCTION_KEYS = ("ref-data", "daily-list", "dividends", date)
        else:
            _FUNCTION_KEYS = ("ref-data", "daily-list", "dividends")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_next_day_ex_date(self, date, format=None, token=None):
        """
        This call provides advance notification of dividend declarations impacting IEX-listed securities.

        Records are added at 8:00 a.m. ET one trading day before the specified Ex-Date. Records would have been communicated in the IEX Dividends Daily List when they were added or modified by the Exchange. Records are removed when Ex-Date is equal to today or when the record is deleted by the Exchange (in this case, a new record will appear in the IEX Dividends Daily List with an Event Type=DELETE for the affected Record ID).

        Updates are posted once per hour from 8:00 a.m. to 6:00 p.m. ET on each trading day

        Options
        Range   Description     Source
        date    Specific date   Daily list data for a specified date in the format YYYYMMDD,if available, or sample. If sample, a sample file will be returned

        Parameters
        Parameter   Details
        format  - Parameter is optional
                - Value can be csv or psv
                - When parameter is not present, format defaults to JSON
        token   - Parameter is optional
                - Value is the API token from your IEX user account
                - If you have been permissioned for CUSIP information you'll receive a CUSIP field, othewise data defaults to exclude CUSIP.
        """

        if date:
            _FUNCTION_KEYS = ("ref-data", "daily-list", "next-day-ex-date", date)
        else:
            _FUNCTION_KEYS = ("ref-data", "daily-list", "next-day-ex-date")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_symbol_directory(self, date, format=None, token=None):
        """
        This call returns an array of all IEX-listed securities and their corresponding data fields. The IEX-Listed Symbol Directory Daily List is initially generated and posted to the IEX website at 8:30 p.m. Eastern Time (ET) before each trading day, and then once per hour from 9 p.m. until 6 p.m. ET the following day.

        Options
        Range   Description     Source
        date    Specific date   Daily list data for a specified date in the format YYYYMMDD,if available, or sample. If sample, a sample file will be returned

        Parameters
        Parameter   Details
        format  - Parameter is optional
                - Value can be csv or psv
                - When parameter is not present, format defaults to JSON
        token   - Parameter is optional
                - Value is the API token from your IEX user account
                - If you have been permissioned for CUSIP information you'll receive a CUSIP field, othewise data defaults to exclude CUSIP.
        """

        if date:
            _FUNCTION_KEYS = ("ref-data", "daily-list", "symbol-directory", date)
        else:
            _FUNCTION_KEYS = ("ref-data", "daily-list", "symbol-directory")
        return _FUNCTION_KEYS

