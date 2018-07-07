import json
import requests

def get_location_info(ip_address):
    api_token = '6425cd9ff3ddf98d10baa03d9ad2b121'
    api_url_base = 'http://api.ipstack.com/'
    api_url_request = api_url_base + ip + '?access_key=' + api_token

    response = requests.get(api_url_request)

    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code,api_url))
        return None  
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code == 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected Redirect'.format(response.status_code))
        return None
    elif response.status_code == 104:
        print('[!] [{0} monthly_limit_reached'.format(response.status_code))
        return None
    elif response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
    return None

def get_bp_json(bp_url):
    print(bp_url)

    response = requests.get(bp_url)

    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code,api_url))
        return None  
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code == 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected Redirect'.format(response.status_code))
        return None
    elif response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
    return None


ip = 'node1.eosnewyork.io'
bp_url = 'https://bp.eosnewyork.io/bp.json'

bp_json = get_bp_json(bp_url)
location_info = get_location_info(ip)

data = '{"json":true,"limit":500}'

response = requests.post('https://api.eosnewyork.io:443/v1/chain/get_producers', data=data).json()

print(response.items())

if bp_json is not None:
    print(bp_json.items())
else:
    print('[!] Request Failed')

if location_info is not None:
    print(location_info.items())
else:
    print('[!] Request Failed')


