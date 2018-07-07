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

    r = requests.get(bp_url)
    # print(r.text)

    if r.status_code >= 500:
        print('[!] [{0}] Server Error'.format(r.status_code))
        return None
    elif r.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(r.status_code,api_url))
        return None  
    elif r.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(r.status_code))
        return None
    elif r.status_code == 400:
        print('[!] [{0}] Bad Request'.format(r.status_code))
        return None
    elif r.status_code >= 300:
        print('[!] [{0}] Unexpected Redirect'.format(r.status_code))
        return None
    elif r.status_code == 200:
        return json.loads(r.content.decode('utf-8'))
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(r.status_code, r.content))
    return None


# Main Program
with open('BPout') as data_file:
    data = json.load(data_file)

i=0
rank=1
while i < 10:
    bpurl = data["rows"][i]["url"]
    bpowner = data["rows"][i]["owner"]
    bpurlwjson = bpurl + "/bp.json"
    
    # Get json file
    r_bp_json = get_bp_json(bpurlwjson)
    if r_bp_json is not None:
    #    print(r_bp_json.items())
        print()
    else:
        print('[!] Request Failed')

    print(rank, bpowner, r_bp_json["org"]["location"]["name"],r_bp_json["org"]["location"]["country"])
    i += 1
    rank += 1




#print(response)


#
#if location_info is not None:
#    print(location_info.items())
#else:
#    print('[!] Request Failed')


