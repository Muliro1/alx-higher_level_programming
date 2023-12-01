#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in
the header of the response.
"""
from requests import post
from sys import argv

if __name__ == "__main__":

    html = post(argv[1], data={'email': argv[2]})
    print(html.text)
