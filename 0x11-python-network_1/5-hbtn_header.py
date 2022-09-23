#!/usr/bin/python3
""" Takes a URL and retrieve the header value of the X-Request-Id """
import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print(response.headers.get("X-Request-Id"))
