# Use the Shodan internetdb API (via the requests module) to look up information about an IP address
import requests

try:
    response_API = requests.get('https://internetdb.shodan.io/17.253.144.10', timeout=1.0)
    response_API.raise_for_status()

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

else:
    print(response_API)
    data = response_API.json()
    print(data['hostnames'])