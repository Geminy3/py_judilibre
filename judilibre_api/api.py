from judilibre_api.utils import convert_bool, build_params, build_url, requests_api

class Judilibre():

    def __init__(self, api_key):
        self.header = {
            "accept" : "application/json",
            "KeyID" : api_key
        }
        self.base_url = 'https://sandbox-api.piste.gouv.fr/cassation/judilibre/v1.0/'
        print(f"Status : {self.healthcheck()}")        

    def build_requests(self, args, suffix, verbose):
        verbose = args.pop("verbose")
        params = build_params(args)
        url = build_url(url_method=self.base_url+suffix, params=params)
        if verbose:
            print(f"PARAMS : {params}")
            print(f"URL : {url}")
        self.res = requests_api(url, self.header)
        #return(None)

    def scan(self, type:list[str] = None, theme:list[str] = None, chamber:list[str] = None, 
             formation:list[str] = None, jurisdiction:list[str] = None, location:list[str] = None,
             publication:list[str] = None, solution:list[str] = None, date_start:str = '2021-01-01T06:00:00Z', date_end:str = '', 
             abridged:bool = False, date_type:str = "creation", order:str = 'asc', batch_size:int = 10, search_after:str = '', 
             resolve_references:bool = False, withFileOfType:list[str] = None, particularInterest:bool = False, verbose:bool = False):
        args = locals()
        del args['self']
        return(self.build_requests(args, "scan", verbose))

    def decision(self, id:str = '', resolve_references:bool = False, query:str = '', operator:str = '', verbose:bool = False):
        args = locals()
        del args['self']
        if len(args['id']) == 0:
            return(ValueError("id argument is mandatory"))
        else:
            return(self.build_requests(args, "decision", verbose))

    def healthcheck(self):
        return(requests_api(self.base_url+"healthcheck", self.header))

    def transactionnalhistory(self, date:str = '2021-05-13T06:00:00Z', page_size:int = 500, from_id:str = '', verbose:bool = False):
        args = locals()
        del args['self']
        if len(args['date']) == 0:
            return(ValueError("date argument is mandatory"))
        else:
            return(self.build_requests(args, "transactionnalhistory", verbose))

    def search(self, query:str = '', field:list[str] = None, operator:str = '', type:list[str] = None, theme:list[str] = None, 
               chamber:list[str] = None, formation:list[str] = None, jurisdiction:list[str] = None, location:list[str] = None,
               publication:list[str] = None, solution:list[str] = None, date_start:str = '2021-01-01T06:00:00Z', date_end:str = '', 
               sort:str = 'scorepub', order:str = 'asc', page_size:int = 10, page:int = 0, resolve_references:bool = False, 
               withFileOfType:list[str] = None, particularInterest:bool = False, verbose:bool = False):
        args = locals()
        del args['self']
        return(self.build_requests(args, "search", verbose))

    def taxonomy(self, id:str = '', key:str = '', value:str = '', context_value:str = '', verbose:bool = False):
        args = locals()
        del args['self']
        return(self.build_requests(args, "taxonomy", verbose))

    def stats(self, jurisdiction:str = '', location:str = '', date_start = '', date_end = '', particularInterest:str = '',
              keys:str='', verbose:bool = False):
        args = locals()
        del args['self']
        return(self.build_requests(args, "stats", verbose))