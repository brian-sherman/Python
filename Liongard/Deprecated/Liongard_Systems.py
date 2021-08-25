import requests
import base64
import json

access_id = '***********'
secret_key = '***********'
url = "https://us1.app.liongard.com/api/v1/systems"
id_secret = access_id + ':' + secret_key
enc_id_secret = base64.b64encode(id_secret.encode())

url_headers = {
    "X-ROAR-API-KEY":enc_id_secret,
}

response = requests.get(url, headers=url_headers)
json_response = json.loads(response.text)
f = open("C:\\Filepath\\Systems.json", "w+")
f.write(json.dumps(json_response, indent=4, sort_keys=True))