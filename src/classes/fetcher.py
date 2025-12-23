import requests
import configparser
import src.utils.typesafe_utils as t

from typing import Any, Dict
from urllib.parse import urljoin
from dataclasses import dataclass



def _load_api_key(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    return config.get("api_key", "account_key")


@dataclass
class APIResponse:
    raw: requests.Response
    content: Any

    def __getattr__(self, name):
        return getattr(self.raw, name)



class _MethodWrapper:
    def __init__(self, parent, http_method):
        self._parent = parent
        self._method = getattr(parent._session, http_method)


    def __call__(self, endpoint, *args, **kwargs) -> APIResponse:

        """TODO: add caching of requests deal figure out how to use it with the APIResponese class?  
                 could maybe do some cool things with it tbh

                 might be able to actually use that as the cache? 
                 -> cache is stored on a date basis? each day requests get made, i have a db in the back end 
                 -> that is storing the responses from the api and also a lookup key
                 -> APIResponse (in its own file now) can handle loading from a json 
                 -> _MethodWrapper handles the clearing of a hash map at a certian time and then builds it out 
                 -> over a period of time 
                 -> maybe not even in a db just a local mem that stores the requests and responses? idk tbd
        """

        endpoint = str(endpoint).lstrip("/")

        response = self._method(urljoin(self._parent.base_url, endpoint), *args, **kwargs)
        
        if response.headers.get("content-type", "").startswith("application/json"):
            # just overriding content 'b' (by default) to the json obj
            return APIResponse(response, response.json())

        else:
            # dont love might chagne response structure later
            return APIResponse(response, response.content)

        

class Fetcher:
    def __init__(
        self,
        fetcher_profile: Dict,
        response_format="json",
        raise_on_error=True,
    ):

        self._session = requests.Session()
        self.base_url = t.dig(fetcher_profile, ["BASE_URL"])

        if not self.base_url:
            raise Exception("failed to build fetcher")
        

        if (config_path := t.dig(fetcher_profile, ["CONFIG_PATH"])):
            api_key = _load_api_key(config_path)
            api_key_name = t.dig(fetcher_profile, ["KEY_NAME"])

            self._session.headers.update({api_key_name: api_key})
        
        self._session.params = {"format": response_format}

        if (parameters := t.dig(fetcher_profile, ["PARAMETERS"], {})):
            self._session.params.update(parameters)

        if raise_on_error:
            self._session.hooks = {
                "response": lambda r, *args, **kwargs: r.raise_for_status()
            }


    def __getattr__(self, method_name):
        method = _MethodWrapper(self, method_name)
        self.__dict__[method_name] = method
        return method


    
        