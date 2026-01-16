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