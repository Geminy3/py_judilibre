import requests
import time
from config import KEY_PISTE
import json

def healthcheck():
    header = {
        "accept" : "application/json",
        "KeyId" : KEY_PISTE
    }
    res = requests.get(url = f"https://sandbox-api.piste.gouv.fr/cassation/judilibre/v1.0/healthcheck", 
                       headers=header)
    return(json.loads(res.content))


def searchJudilibre(params):
    header = {
        "accept" : "application/json",
        "KeyId" : KEY_PISTE
    }
    res = requests.get(url = f"https://sandbox-api.piste.gouv.fr/cassation/judilibre/v1.0/search?{params}", 
                       headers=header)
    return(json.loads(res.content))

def getDecText(id):
    header = {
        "accept" : "application/json",
        "KeyId" : KEY_PISTE
    }
    res = requests.get(url= f"https://sandbox-api.piste.gouv.fr/cassation/judilibre/v1.0/decision?id={id}", 
                       headers=header)
    if res.status_code == 200:
        return(json.loads(res.content))
    else:
        print(res, id)

def getTaxonomy(params):
    header = {
        "accept" : "application/json",
        "KeyId" : KEY_PISTE
    }
    res = requests.get(url= f"https://sandbox-api.piste.gouv.fr/cassation/judilibre/v1.0/taxonomy?{params}", 
                       headers=header)
    if res.status_code == 200:
        return(json.loads(res.content))
    else:
        print(res, id)

if __name__ == "__main__":
    day, month, year, h, m = time.localtime()[:5]
    print(f"Start process on the {day}-{month}-{year} at {h}:{m}")
    print(healthcheck())
    # paramsTaxo="id=theme"
    # print(getTaxonomy(paramsTaxo))
    params = "query=trouble+voisinage&page_size=50"#&theme=troubles+anormaux+de+voisinage"
    res = searchJudilibre(params)
    print(res["total"])
    print(res["next_page"])
    dec = res['results']
    for i, d in enumerate(dec[20:24]):
        print(i)
        #print(d.keys())
        id = d['id']
        resDec = getDecText(id)
        print(resDec.keys())
        #print(resDec["text"])
        print(resDec["solution"])
        print(resDec["jurisdiction"])
        print(resDec["themes"])

        