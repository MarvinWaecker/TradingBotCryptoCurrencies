import requests
import pprint

bitmex_base_api_url = "https://www.bitmex.com/api/v1"

# https://www.bitmex.com/api/explorer/#!/Stats/Stats_history

def get_contracts(print_obj=False):
    
    # get Info from bitmex
    response_object = requests.get(bitmex_base_api_url + "/instrument/active")
    # check status
    #print(response_object.status_code)
    # save return object as json
    obj_json = response_object.json()
    # initialize list for contracts
    contracts = []
    # print whole return_obj if wanted
    if print_obj:
        pprint.pprint(obj_json)
    # get contracts and save inside list
    for contract in obj_json:
        contracts.append(contract['symbol'])

    return contracts
