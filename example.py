import time
from config import KEY_PISTE
from judilibre_api.api import Judilibre

if __name__ == "__main__":
    day, month, year, h, m = time.localtime()[:5]
    print(f"Start process on the {day}-{month}-{year} at {h}:{m}")

    api = Judilibre(api_key=KEY_PISTE)
    #api.scan(jurisdiction=["tj", "ca"])
    search_call = api.search(query="trouble anormal de voisinage", date_start='', page_size=50, jurisdiction=['tj', 'ca'])
    print(search_call['total'])
    for i, id in enumerate([res['id'] for res in search_call['results']]):
        print(f"{i} - ID ----> {id}")
        res = api.decision(id=id)