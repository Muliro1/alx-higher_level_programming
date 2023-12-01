#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in
the header of the response.
"""
from requests import get
from sys import argv

if __name__ == "__main__":

    response = get(argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
