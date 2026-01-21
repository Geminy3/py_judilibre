from urllib.parse import urlencode
import requests
import json
from exceptions import (
    ERROR_CODES_TO_EXCEPTIONS,
    JudilibreInternalError,
    JudilibreTooManyRequestError,
    JudilibreSuspiciousActivityError,
    JudilibreResourceNotFoundError,
    JudilibreUnauthorizedError,
    JudilibreInvalidCredentialsError,
    JudilibreInvalidRequestError
)

convert_bool = {
    False: "false",
    True: "true"
}

def build_url(url_method, params):
        url = f"{url_method}?{urlencode(params, doseq=True)}"
        return(url)

def build_params(args):
    params = {}
    for arg in args:
        if args[arg] != None and args[arg] != '':
            if type(args[arg]) is bool:
                params[arg] = convert_bool[args[arg]]
            else:
                params[arg] = args[arg]
    return(params)

def requests_api(url, header):
    res = requests.get(url = url, 
                headers=header)
    if res.status_code == 200:
        return(json.loads(res.content))
    else:
        if res.status_code in ERROR_CODES_TO_EXCEPTIONS:
            exception = ERROR_CODES_TO_EXCEPTIONS[res.status_code]
            raise exception from res
        else:
            raise res