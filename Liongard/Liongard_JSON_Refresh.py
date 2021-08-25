import requests
import base64
import json

access_id = '****************'
secret_key = '**********************************'

id_secret = access_id + ':' + secret_key
enc_id_secret = base64.b64encode(id_secret.encode())

url_headers = {
    "X-ROAR-API-KEY":enc_id_secret,
}

def get_data(url, path):
    response = requests.get(url, headers=url_headers)
    json_response = json.loads(response.text)
    with open(path, "w+") as f:
        f.write(json.dumps(json_response, indent=4, sort_keys=True))

systems_url = "https://us1.app.liongard.com/api/v1/systems"
inspectors_url = "https://us1.app.liongard.com/api/v1/launchpoints"
agents_url = "https://us1.app.liongard.com/api/v1/agents"

systems_path = "C:\\Filepath\\Systems.json"
inspectors_path = "C:\\Filepath\\Inspectors.json"
agents_path = "C:\\Filepath\\Agents.json"

get_data(systems_url, systems_path)
get_data(inspectors_url, inspectors_path)
get_data(agents_url, agents_path)