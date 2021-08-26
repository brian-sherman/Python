import requests
import base64
import json

access_id = '****************'
secret_key = '**********************************'

def get_header(id, secret):
    id_secret = id + ':' + secret
    enc_id_secret = base64.b64encode(id_secret.encode())
    url_header = {
        "X-ROAR-API-KEY":enc_id_secret,
    }
    return url_header

def get_data(url, path, header):
    response = requests.get(url, headers=header)
    json_response = json.loads(response.text)
    with open(path, "w+") as f:
        f.write(json.dumps(json_response, indent=4, sort_keys=True))

systems_url = "https://us1.app.liongard.com/api/v1/systems"
inspectors_url = "https://us1.app.liongard.com/api/v1/launchpoints"
agents_url = "https://us1.app.liongard.com/api/v1/agents"

systems_path = "C:\\Filepath\\Systems.json"
inspectors_path = "C:\\Filepath\\Inspectors.json"
agents_path = "C:\\Filepath\\Agents.json"

header = get_header(access_id, secret_key)

get_data(systems_url, systems_path, header)
get_data(inspectors_url, inspectors_path, header)
get_data(agents_url, agents_path, header)