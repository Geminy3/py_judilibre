from urllib.parse import urlencode
import requests
import json

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
                    headers= header)
    if res.status_code == 200:
        return(json.loads(res.content))
    else:
        return(ConnectionError)