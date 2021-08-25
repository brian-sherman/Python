import requests
import base64
import json

access_id = '***********'
secret_key = '***********************'

systems_url = "https://us1.app.liongard.com/api/v1/systems"
inspectors_url = "https://us1.app.liongard.com/api/v1/launchpoints"

id_secret = access_id + ':' + secret_key
enc_id_secret = base64.b64encode(id_secret.encode())

url_headers = {
    "X-ROAR-API-KEY":enc_id_secret,
}

systems_path = "C:\\Filepath\\Systems.json"
inspectors_path = "C:\\Filepath\\Inspectors.json"

systems_response = requests.get(systems_url, headers=url_headers)
systems_json_response = json.loads(systems_response.text)
with open(systems_path, "w+") as f:
    f.write(json.dumps(systems_json_response, indent=4, sort_keys=True))

inspectors_response = requests.get(inspectors_url, headers=url_headers)
inspectors_json_response = json.loads(inspectors_response.text)
with open(inspectors_path, "w+") as f:
    f.write(json.dumps(inspectors_json_response, indent=4, sort_keys=True))