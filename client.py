"""
Test client for the Robotic Lawnmower Simulator GraphQL API.
This script allows you to run GraphQL queries against the simulator's API.
It uses the requests library to send HTTP POST requests to the GraphQL endpoint.
It can be used to test various scenarios such as simulating mower paths, checking grass cutting status, and handling crashes.
It includes error handling for HTTP requests and prints the results in a formatted JSON output.

To use this script, run it from the command line with a GraphQL query as an argument:
For Windows cmd:
python client.py "query { simulate(width: 3, height: 3, rocks: [[1,1]], path: [\"right\", \"right\", \"down\", \"left\", \"left\", \"up\"]) { allGrassCut uncutGrassRemaining crashed crashReason } }

For Linux:
python client.py 'query { simulate(width: 3, height: 3, rocks: [[1,1]], path: ["right", "right", "down", "left", "left", "up"]) { allGrassCut uncutGrassRemaining crashed crashReason } }'
"""
import sys
import json
import requests

API_URL = "http://localhost:8000/graphql"

def run_graphql_query(query: str):
    """Run a GraphQL query against the Robotic Lawnmower Simulator API."""
    payload = {"query": query}
    response = requests.post(API_URL, json=payload, timeout=10)
    try:
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"HTTP error: {e}")
        print(response.text)
        sys.exit(1)
    return response.json()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python client.py '<graphql_query>'")
        sys.exit(1)
    query = sys.argv[1]
    result = run_graphql_query(query)
    print(json.dumps(result, indent=2))
