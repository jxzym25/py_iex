from .iex import IEX

class MarketData(IEX):
    """
    This class implements all the api calls to IEX Market Data
    """
    @IEX._call_api_on_func
    def get_tops(self, symbols=None, format=None):
        """
        TOPS provides IEX's aggregated best quoted bid and offer position in near real time for all securities on IEX's displayed limit order book. TOPS is ideal for developers needing both quote and trade data.

        Parameters
        Parameter   Details
        symbols     - Parameter is optional
                    - Value needs to be a comma-separated list of symbols (i.e SNAP,fb)
                    - When parameter is not present, request returns all symbols
        format      - Parameter is optional
                    - Value can only be csv
                    - When parameter is not present, format defaults to JSON
        """

        _FUNCTION_KEYS = ("tops")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_last(self, symbols=None, format=None):
        """
        Last provides trade data for executions on IEX. It is a near real time, intraday API that provides IEX last sale price, size and time. Last is ideal for developers that need a lightweight stock quote.

        Parameters
        Parameter   Details
        symbols     - Parameter is optional
                    - Value needs to be a comma-separated list of symbols (i.e SNAP,fb)
                    - When parameter is not present, request returns all symbols
        format      - Parameter is optional
                    - Value can only be csv
                    - When parameter is not present, format defaults to JSON
        """

        _FUNCTION_KEYS = ("tops", "last")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_hist(self, date=None):
        """
        HIST will provide the output of IEX data products for download on a T+1 basis. Data will remain available for the trailing twelve months.

        Parameters
        Parameter   Details
        date        - Parameter is optional
                    - Value needs to be in four-digit year, two-digit month, two-digit day format (YYYYMMDD) (i.e May 15, 2017 would be written as 20170515)
                    - When parameter is not present, request returns all available dates
        """

        _FUNCTION_KEYS = ("hist")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_deep(self, symbols=None):
        """
        DEEP is used to receive real-time depth of book quotations direct from IEX. The depth of book quotations received via DEEP provide an aggregated size of resting displayed orders at a price and side, and do not indicate the size or number of individual orders at any price level. Non-displayed orders and non-displayed portions of reserve orders are not represented in DEEP.

        DEEP also provides last trade price and size information. Trades resulting from either displayed or non-displayed orders matching on IEX will be reported. Routed executions will not be reported.

        Parameters
        Parameter   Details
        symbols     - Parameter is required
                    - Value needs to be a single symbol (i.e snap)
        """
        
        _FUNCTION_KEYS = ("deep")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_book(self, symbols=None):
        """
        Book shows IEX's bids and asks for given symbols.

        Parameters
        Parameter   Details
        symbols     - Parameter is required
                    - Value needs to be a comma-separated list of symbols (i.e SNAP,fb)
                    - Maximum of 10 symbols
        """
        
        _FUNCTION_KEYS = ("deep", "book")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_trades(self, symbols=None, last=None):
        """
        Trade report messages are sent when an order on the IEX Order Book is executed in whole or in part. DEEP sends a Trade report message for every individual fill.

        """
        _FUNCTION_KEYS = ("deep", "trades")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_system_events(self):
        """
        The System event message is used to indicate events that apply to the market or the data feed.

        There will be a single message disseminated per channel for each System Event type within a given trading session.
        """
        _FUNCTION_KEYS = ("deep", "system-event")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_trading_status(self, symbols=None):
        """
        The Trading status message is used to indicate the current trading status of a security. For IEX-listed securities, IEX acts as the primary market and has the authority to institute a trading halt or trading pause in a security due to news dissemination or regulatory reasons. For non-IEX-listed securities, IEX abides by any regulatory trading halts and trading pauses instituted by the primary or listing market, as applicable.

        IEX disseminates a full pre-market spin of Trading status messages indicating the trading status of all securities. In the spin, IEX will send out a Trading status message with "T" (Trading) for all securities that are eligible for trading at the start of the Pre-Market Session. If a security is absent from the dissemination, firms should assume that the security is being treated as operationally halted in the IEX Trading System.

        After the pre-market spin, IEX will use the Trading status message to relay changes in trading status for an individual security. Messages will be sent when a security is:

        - Halted
        - Paused*
        - Released into an Order Acceptance Period*
        - Released for trading
        *The paused and released into an Order Acceptance Period status will be disseminated for IEX-listed securities only. Trading pauses on non-IEX-listed securities will be treated simply as a halt.

        Parameters

        Parameter   Details
        symbols     - Parameter is required
                    - Value needs to be a comma-separated list of symbols (i.e SNAP,fb)
                    - Maximum of 10 symbols
        """
        _FUNCTION_KEYS = ("deep", "trading-status")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_op_halt_status(self, symbols=None):
        """
        The Exchange may suspend trading of one or more securities on IEX for operational reasons and indicates such operational halt using the Operational halt status message.

        IEX disseminates a full pre-market spin of Operational halt status messages indicating the operational halt status of all securities. In the spin, IEX will send out an Operational Halt Message with "N" (Not operationally halted on IEX) for all securities that are eligible for trading at the start of the Pre-Market Session. If a security is absent from the dissemination, firms should assume that the security is being treated as operationally halted in the IEX Trading System at the start of the Pre-Market Session.

        After the pre-market spin, IEX will use the Operational halt status message to relay changes in operational halt status for an individual security.

        Parameters
        Parameter   Details
        symbols     - Parameter is required
                    - Value needs to be a comma-separated list of symbols (i.e SNAP,fb)
                    - Maximum of 10 symbols
        """
        _FUNCTION_KEYS = ("deep", "op-halt-status")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_ssr_status(self, symbols=None):
        """
        In association with Rule 201 of Regulation SHO, the Short Sale Price Test Message is used to indicate when a short sale price test restriction is in effect for a security.

        IEX disseminates a full pre-market spin of Short sale price test status messages indicating the Rule 201 status of all securities. After the pre-market spin, IEX will use the Short sale price test status message in the event of an intraday status change.

        The IEX Trading System will process orders based on the latest short sale price test restriction status.

        Parameters
        Parameter   Details
        symbols     - Parameter is required
                    - Value needs to be a comma-separated list of symbols (i.e SNAP,fb)
                    - Maximum of 10 symbols
        """
        _FUNCTION_KEYS = ("deep", "ssr-status")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_security_event(self, symbols=None):
        """
        The Security event message is used to indicate events that apply to a security. A Security event message will be sent whenever such event occurs

        Parameters
        Parameter   Details
        symbols     - Parameter is required
                    - Value needs to be a comma-separated list of symbols (i.e SNAP,fb)
                    - Maximum of 10 symbols
        """
        _FUNCTION_KEYS = ("deep", "security-event")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_trade_break(self, symbols=None, last=None):
        """
        Trade break messages are sent when an execution on IEX is broken on that same trading day. Trade breaks are rare and only affect applications that rely upon IEX execution based data.

        Parameters
        Parameter   Details
        symbols     - Parameter is required
                    - Value needs to be a comma-separated list of symbols (i.e SNAP,fb)
                    - Maximum of 10 symbols
        last        - Parameter is optional
                    - Value needs to be a number (i.e 5)
                    - Default is 20
                    - Maximum of 500
        """
        _FUNCTION_KEYS = ("deep", "trade-break")
        return _FUNCTION_KEYS

    @IEX._call_api_on_func
    def get_auction(self, symbols=None):
        """
        DEEP broadcasts an Auction Information Message every one second between the Lock-in Time and the auction match for Opening and Closing Auctions, and during the Display Only Period for IPO, Halt, and Volatility Auctions. Only IEX listed securities are eligible for IEX Auctions.

        Parameters
        Parameter   Details
        symbols     - Parameter is required
                    - Value needs to be a comma-separated list of symbols (i.e SNAP,fb)
                    - Maximum of 10 symbols
        """
        _FUNCTION_KEYS = ("deep", "auction")
        return _FUNCTION_KEYS


    @IEX._call_api_on_func
    def get_official_price(self, symbols=None):
        """
        The Official Price message is used to disseminate the IEX Official Opening and Closing Prices.

        These messages will be provided only for IEX Listed Securities.

        Parameters
        Parameter   Details
        symbols     - Parameter is required
                    - Value needs to be a comma-separated list of symbols (i.e SNAP,fb)
                    - Maximum of 10 symbols
        """
        _FUNCTION_KEYS = ("deep", "official-price")
        return _FUNCTION_KEYS

