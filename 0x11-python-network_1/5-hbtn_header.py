#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in
the header of the response.
"""
from requests import get
from sys import argv

if __name__ == "__main__":

    html = get(argv[1])
    print(html.headers.get('X-Request-Id'))
