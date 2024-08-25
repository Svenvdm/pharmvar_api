import logging
import requests
import requests.packages
from typing import List, Dict
from exceptions import PharmVarApiException, NoDataFoundError
from models import Result
from json import JSONDecodeError


class RestAdapter:
    def __init__(self, hostname: str = "www.pharmvar.org/api-service" , api_key: str = "", version: str = "0.1", ssl_verify: bool = True, logger: logging.Logger = None):
        """
        :param hostname: The hostname of the API server: e.g. www.pharmvar.org/api-service
        :param api_key (optional): The API key to use for authentication
        :param version: The version of the API to use: currently only "0.1" is supported
        :param ssl_verify: Normally set to True, but if having SSL/TLS cert validation issues, can turn off with False
        :param logger (optional): pass your logger here to use it, otherwise a new logger will be created
        """

        self.url = f"https://{hostname}/"
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        self._logger = logger or logging.getLogger(__name__)

        if not ssl_verify:
            requests.packages.urllib3.disable_warnings()

    def _do(self, http_method: str, endpoint: str, params: Dict = None, data: Dict = None, headers: Dict = {"Accept" : "application/json"}) -> Result:
        full_url = f"{self.url}{endpoint}"
        print(headers)
        log_line_pre = f"method={http_method}, url={full_url}, params={params}"
        log_line_post = ', '.join((log_line_pre, "success={}, status_code={}, message={}"))
        # Log HTTP params and perform an HTTP request, catching and re-raising any exceptions
        try:
            self._logger.debug(msg = log_line_pre)   
            response = requests.request(method = http_method,
                                    url = full_url,
                                    headers = headers,
                                    params = params,
                                    data = data,
                                    verify = self._ssl_verify)
        except requests.exceptions.RequestException as e:
            self._logger.error(msg=(str(e)))
            raise PharmVarApiException("Request failed") from e

        # Deserialize JSON output to Python object, or return failed Result on exception
        print(response.text)
        try:
            if headers["Accept"] == "application/json":
                data_out = response.json()
            elif headers["Accept"] == "text/plain":
                data_out = response.text
        except (JSONDecodeError, ValueError) as e:
            self._logger.error(msg = log_line_post.format("False", "None", e)) 
            raise PharmVarApiException("Bad JSON in response") from e

        # If status_code in 200-299 range, return success Result with data, otherwise raise exception
        is_success = 200 <= response.status_code <= 299
        log_line = log_line_post.format(is_success, response.status_code, response.reason)
        if is_success:
            self._logger.debug(msg = log_line)
            result = Result(status_code = response.status_code, message = response.reason, data = data_out)
            if not result.data:
                # current behaviour for empty data is to raise an exception, but could be changed to return a Result with empty data
                raise NoDataFoundError(f"No data found for endpoint: {endpoint}")
            return result
        self._logger.error(msg = log_line)
        raise PharmVarApiException(f"Request failed with status code {response.status_code}: {data_out["errorMessage"] if data_out else response.reason}")

    def get(self, endpoint: str, params: Dict = None) -> Result:
        """
        Perform an HTTP GET request to the API
        :param endpoint: The API endpoint to call
        :param params: A dictionary of parameters to pass to the API
        :return: A Result object containing the status code, message, and data
        """
        return self._do("GET", endpoint, params = params)
    



        



