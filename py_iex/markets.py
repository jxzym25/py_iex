from .iex import IEX

class Markets(IEX):
    @IEX._call_api_on_func
    def get_market(self, format=None):
        """
        This endpoint returns near real time traded volume on the markets. Market data is captured by the IEX system from approximately 7:45 a.m. to 5:15 p.m. ET.

        Parameters
        Parameter   Details
        format      - Parameter is optional
                    - Value can only be csv
                    - When parameter is not present, format defaults to JSON
        """
        _FUNCTION_KEYS = ["market"]
        return _FUNCTION_KEYS


