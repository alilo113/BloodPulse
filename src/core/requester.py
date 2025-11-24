import requests

def send_request(url, max_requests):
    for request_attempt in range(max_requests):
        try:
            response = requests.post(url, auth=('user', 'pass'))
            print(f"Request attempt {request_attempt + 1}: Status Code {response.status_code}")
            if response.status_code == 429:
                print("Received 429 Too Many Requests. Stopping further attempts.")
                break

            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Request attempt {request_attempt + 1} failed: {e}")
    return None