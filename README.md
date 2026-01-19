# py_judilibre

This repository aims to simplfy the access to the [Judilibre](https://piste.gouv.fr/index.php?option=com_apiportal&view=apitester&usage=api&apitab=tests&apiName=JUDILIBRE&apiId=34c6d930-c6da-470f-b30b-a6ffa5dee6b3&managerId=3&type=rest&apiVersion=1.0.0&Itemid=179&swaggerVersion=2.0&lang=fr) API by providing a Python wrapper around it.

Judilibre is a service provided by the French Ministry of Justice that allows users to search for and retrieve legal decisions from various French judicial courts.

## Installation

## Features

- Search for legal decisions using various criteria.
- Retrieve detailed information about specific decisions.
- Handle API authentication and requests seamlessly.

The default methods provided by the API are wrapped in Python functions for ease of use.
- `scan`: 
- `decision`:
- `healthcheck`: healthcheck gives the status of the API. This function is called automatically when initializing the `Judilibre` class.
- `transcationnalhistory`:
- `search`:
- `taxonomy`:
- `stats`:

## Usage

First of all, you need to get an API key from the [PISTE](https://piste.gouv.fr/) website. Once you have your API key, you can use it to initialize the `Judilibre` class.

```python
from py_judilibre import Judilibre

api = Judilibre(api_key=KEY_PISTE)
```

You can then use the various methods provided by the `Judilibre` class to interact with the API.

## Documentation de l'API

All the informations concerning Julibre API are available on the [PISTE](https://piste.gouv.fr/) website at this url : [Documentation Judilibre](https://piste.gouv.fr/index.php?option=com_apiportal&view=apitester&usage=api&apitab=tests&apiName=JUDILIBRE&apiId=34c6d930-c6da-470f-b30b-a6ffa5dee6b3&managerId=3&type=rest&apiVersion=1.0.0&Itemid=179&swaggerVersion=2.0&lang=fr).

En principe, l'ensemble des paramètres par défaut et des restrictions ont été implémentées dans les fonctions Python. Cependant, pour plus de détails sur les paramètres disponibles, veuillez vous référer à la documentation officielle de l'API.

## To-DO

- Eventually, implement all restriction from the API on the codebase (is it flex enough for long term maintenance ? => Maybe implement some rules with taxonomy call ?)
- Expand the API to more services than Judilibre => other justice related API (for Open Data access)
- implement a Makefile and functions to deploy the repository (mainly for key management)
- deploy the package on PyPI
- add more examples and documentation