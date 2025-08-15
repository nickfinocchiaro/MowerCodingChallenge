"""
Test client for the Robotic Lawnmower Simulator GraphQL API.
This script allows you to run GraphQL queries against the simulator's API.
It uses the requests library to send HTTP POST requests to the GraphQL endpoint.
It can be used to test various scenarios such as simulating mower paths, checking grass cutting status, and handling crashes.
It includes error handling for HTTP requests and prints the results in a formatted JSON output.

To use this script, run it from the command line. Edit the user-editable constants at the top of the file to configure the query parameters.
"""
import json
import requests

# User-editable constants
API_URL = "http://localhost:8000/graphql"
WIDTH = 3
HEIGHT = 3
ROCKS = [[1, 1]]
PATH = ["right", "right", "down", "left", "left", "up"]
FIELDS = ["allGrassCut", "uncutGrassRemaining", "crashed", "crashReason"]

# Build the GraphQL query string
query = f"""query {{ simulate(width: {WIDTH}, height: {HEIGHT}, rocks: {ROCKS}, path: {json.dumps(PATH)}) {{ {' '.join(FIELDS)} }} }}"""

def run_graphql_query(query: str):
    """Run a GraphQL query against the Robotic Lawnmower Simulator API."""
    payload = {"query": query}
    response = requests.post(API_URL, json=payload, timeout=10)
    try:
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"HTTP error: {e}")
        print(response.text)
        exit(1)
    return response.json()

if __name__ == "__main__":
    result = run_graphql_query(query)
    print(json.dumps(result, indent=2))
