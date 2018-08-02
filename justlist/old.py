# just get list of BP via API
import json
import requests

class Quality_Check:
    def check_broken_link(self,data):
        try:
            url = requests.head(data)
            if url.status_code in (200,302,301):
                return True
        except requests.exceptions.SSLError as e:
            return False

def get_location_info(ip_address):
    api_token = '6425cd9ff3ddf98d10baa03d9ad2b121'
    api_url_base = 'http://api.ipstack.com/'
    api_url_request = api_url_base + ip_address + '?access_key=' + api_token

    response = requests.get(api_url_request)
    # print(response.text)
    
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
    # print(bp_url)
    qc=Quality_Check()
    #if qc.check_broken_link(bp_url):
    #    print("%s true" % (bp_url))
    #else:
        # print("%s false" % (bp_url))
    #    return None
    if not qc.check_broken_link(bp_url):
        return None

    try:
        r = requests.get(bp_url)
    except requests.exceptions.ConnectionError:
        r.status_code = "Connection refused"
        return None
    
    # print(r.text)
    # print(r.status_code)
    

    

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
        try:
            return json.loads(r.content.decode('utf-8'))
        except ValueError:  # includes simplejson.decoder.JSONDecodeError
            # print ('Decoding JSON has failed')
            return None
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(r.status_code, r.content))
    return None


# Main Program
# get the current BP list calling a script with curl
import subprocess
subprocess.call(['./getBP'])

with open('BPout') as data_file:
    data = json.load(data_file)

print("Rank, BPname, OrgLoc, OrgCtry, Website")

i=0
rank=1
while True:

    try :
        bpurl = data["rows"][i]["url"]
        bpowner = data["rows"][i]["owner"]
    except IndexError:
        break
    # bpurlwjson = bpurl + "/bp.json"
    
    # Get json file
    # r_bp_json = get_bp_json(bpurlwjson)
    # if r_bp_json is not None:
    #    org_loc_name = r_bp_json["org"]["location"]["name"]
    #    org_loc_cont = r_bp_json["org"]["location"]["country"]
        
    #    try :
            # nodes_p2p_endpoint = r_bp_json["nodes"][0]["p2p_endpoint"]
            #org_loc_name = r_bp_json["org"]["location"]["name"]
        #except KeyError:
            #print("The key does not exist!")
            # nodes_p2p_endpoint = ""
            #org_loc_name = ""

        
        #n_p_e = nodes_p2p_endpoint.split(':')
        #nod_loc_name = r_bp_json["nodes"][0]["location"]["name"]    
        #nod_loc_cont = r_bp_json["nodes"][0]["location"]["country"]
        # Get real location lookup
        #location_info = get_location_info(n_p_e[0])
        #if location_info is not None:
            #print(location_info.items())
            #real_cont_code = location_info["country_code"]
            #real_cont_name = location_info["country_name"]
        #else:
            #print('[!] Request Failed')

        #print(rank, bpowner, org_loc_name, org_loc_cont)
    print("%d, %s, %s" % (rank, bpowner, bpurl))
        
    #else:
        # print('[!] Request Failed')
        #print("%d, %s, %s, %s, %s Website or JSON Error" % (rank, bpowner, "NONE", "NONE", bpurl ))

    i += 1
    rank += 1
    
    

#test = "eos-bp.bitfinex.com:9876"
#test2 = test.split(':')
#print(test2[0])




