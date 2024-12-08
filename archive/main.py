# NOT WORKING!
# Package deprecated always returning: ModuleNotFoundError: No module named 'webshareproxy'
# This is how the package is supposed to be used, but it is not working.
# Please refer to other script outside of archive folder for working example with the same affect.

import os
from dotenv import load_dotenv
from webshareproxy.client import ApiClient


# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('API_KEY')

if not api_key:
    raise ValueError("API_KEY not found in environment variables")

# Create an instance of the ApiClient class
api_client = ApiClient(api_key)

# Get a list of proxies
proxies = api_client.get_proxy_list()

# Print the proxy details
for proxy in proxies.get_results:
    print("Proxy Host:", proxy.proxy_address)
    print("Proxy Port:", proxy.port)
    print("Proxy Username:", proxy.username)
    print("Proxy Password:", proxy.password)
    print("Country Code:", proxy.country_code)
    print()
