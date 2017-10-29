import requests
import base64
import hmac
from hashlib import sha384




url = "https://api.gemini.com/v1/order/status"
gemini_api_key = "oJEnnC2Xwh3i7wjG9roF"

apiSecretFile = open('API.txt', 'r') 
print(apiSecretFile.readline(1)) 
gemini_api_secret = apiSecretFile.read()


b64 = base64.b64encode(
    json.dumps({'request': '/v1/order/status', 'nonce': 123456, 'order_id': 18834}, sort_keys=True, indent=4)
)

signature = hmac.new(gemini_api_secret, b64, sha384).hexdigest()

headers = {
        'Content-Type': "text/plain",
        'Content-Length': "0",
        'X-GEMINI-APIKEY': gemini_api_key,
        'X-GEMINI-PAYLOAD': b64,
        'X-GEMINI-SIGNATURE': signature,
        'Cache-Control': "no-cache"
        }

response = requests.request("POST", url, headers=headers)

print(response.text)