import requests

def send_request(url):
    r = requests.post(url, auth=('user', 'pass'))
    
    while r.status_code != 429:
        print(f"Response Code: {r.status_code}")
        r = requests.post(url, auth=('user', 'pass'))
    
    print("Received 429 Too Many Requests")