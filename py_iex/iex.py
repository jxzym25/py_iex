import requests
import sys
from functools import wraps
import inspect
from json import loads

class IEX(object):
    """
    Base class for IEX API
    """
    _IEX_API_URL = "https://api.iextrading.com/1.0"

    def __init__(self, retries=5):
        """
        Initialize the class

        retries:    Maximum amount of retries in case of faulty connection or
            server not able to answer the call.
        """
        self.retries = retries

    def _retry(func):
        """
        Decorator for retrying api calls

        func:   The function to be retried
        """
        @wraps(func)
        def _retry_wrapper(self, *args, **kwargs):
            error_message = ""
            for retry in xrange(self.retries + 1):
                try:
                    return func(self, *args, **kwargs)
                except ValueError as err:
                    error_message = str(err)
            raise ValueError(str(error_message))
        return _retry_wrapper

    @classmethod
    def _call_api_on_func(cls, func):
        argspec = inspect.getargspec(func)
        try:
            pos = len(argspec.args) - len(argspec.defaults)
            defaults = dict(zip(argspec.args[pos:], argspec.defaults))
        except:
            if argspec.args:
                # no default
                pos = len(argspec.args)
                defaults = {}
            elif argspec.defaults:
                pos = 0
                defaults = argspec.defaults

        @wraps(func)
        def _call_wrapper(self, *args, **kwargs):
            function_names = func(self, *args, **kwargs)
            url = "{}/{}".format(IEX._IEX_API_URL, '/'.join(function_names))

            if len(argspec) > 1:
                url = "{}?".format(url)
                for idx, arg_name in enumerate(argspec.args[1:]):
                    if arg_name in defaults:
                        try:
                            arg_value = kwargs[arg_name]
                        except KeyError:
                            arg_value = defaults[arg_name]
                        if arg_value:
                            if isinstance(arg_value, tuple) or isinstance(arg_value, list):
                                arg_value = ','.join([str(v) for v in arg_value])
                            url = "{}{}={}&".format(url, arg_name, arg_value)
                url = url[:-1]
            return self._handle_api_call(url)
        return _call_wrapper

    @_retry
    def _handle_api_call(self, url):
        """
        Handle the return call from the api and return a data object.
        It raises a ValueError on problems.

        url:    The url of the service
        """
        response = requests.get(url)
        return response.json()
