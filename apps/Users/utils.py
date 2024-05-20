import random
import requests

def default_token_generator():
    return random.randint(1000, 9999)

def get_user_region(ip_address):
    # Use ipinfo.io API to get geolocation data
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    data = response.json()
    # Extract the region from the response
    region = data.get('region')
    return region
