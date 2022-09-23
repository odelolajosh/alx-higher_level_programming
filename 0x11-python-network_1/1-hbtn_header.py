#!/usr/bin/python3
""" Takes a URL and retrieve the header value of the X-Request-Id """
from urllib import request
import sys

with request.urlopen(sys.argv[1]) as response:
    print(response.getheader("X-Request-Id"))
