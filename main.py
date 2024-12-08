import os
import requests
import asyncio
import aiohttp
import json
import uuid
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('API_KEY')

if not api_key:
    raise ValueError("API_KEY not found in environment variables")

# Define the URL for the API request
url = "https://proxy.webshare.io/api/proxy/list/"

# Set the headers for the request
headers = {
    "Authorization": f"Token {api_key}"
}

# Make the GET request to the API
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    proxies = response.json().get('results', [])
else:
    print(f"Failed to retrieve proxies: {response.status_code} - {response.text}")
    proxies = []

async def test_proxy(session, proxy):
    required_keys = ['username', 'password', 'proxy_address', 'ports']
    if not all(key in proxy for key in required_keys):
        return False

    proxy_url = f"http://{proxy['username']}:{proxy['password']}@{proxy['proxy_address']}:{proxy['ports']['http']}"
    try:
        async with session.get('http://www.google.com', proxy=proxy_url, timeout=10) as resp:
            if resp.status == 200:
                return True
    except Exception as e:
        print(f"Error testing proxy {proxy['proxy_address']}: {e}")
        return False
    return False

async def test_proxies(proxies):
    async with aiohttp.ClientSession() as session:
        tasks = [test_proxy(session, proxy) for proxy in proxies]
        results = await asyncio.gather(*tasks)
        return [{"proxy": proxy, "is_viable": result} for proxy, result in zip(proxies, results)]

async def main():

    if proxies:
        results = await test_proxies(proxies)
        uid = uuid.uuid4()
        stats_file = f"data/stats_{uid}.json"
        os.makedirs('data', exist_ok=True)
        with open(stats_file, 'w') as f:
            json.dump(results, f, indent=4)
        print(f"Saved stats to {stats_file}")

        # Calculate and log stats
        viable_proxies = sum(1 for result in results if result['is_viable'])
        total_proxies = len(results)
        percentage_viable = (viable_proxies / total_proxies) * 100 if total_proxies > 0 else 0
        print(f"Viable proxies: {viable_proxies}/{total_proxies} ({percentage_viable:.2f}%)")

if __name__ == "__main__":
    asyncio.run(main())