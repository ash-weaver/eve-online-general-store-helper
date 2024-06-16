import requests

# requests data from EVE ESI for route
# returns dictionary from json response
# route example: "/regions/" or "/regions/10000003/"
def request_data(route):
    url_head = "https://esi.evetech.net/latest"
    datasource = "?datasource=tranquility"
    url = url_head + route + datasource
    print("requesting " + route + "...")
    return requests.get(url).json()