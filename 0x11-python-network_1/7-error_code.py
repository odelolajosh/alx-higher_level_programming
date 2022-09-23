#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response
handling error appropriately
"""
import requests
import sys

if __name__ == "__main__":
    try:
        response = requests.get(sys.argv[1])
        print(response.text)
    except requests.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
