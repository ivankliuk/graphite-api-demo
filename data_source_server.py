#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function

from wsgiref.simple_server import make_server
import sys
from random import randint
import json
import time

STEP = 60  # for each minute


def generate_fake_data():
    """This function generates fake data for testing purposes.

    :return: a dictionary with a timestamp in UNIX format as key and a random
    number from 0 to 25 as value.
    """
    now = int(time.time())
    start_date = now - 3600 * 24 * 30  # a month ago in seconds
    result = {}
    for ts in xrange(start_date, now, STEP):
        result[ts] = randint(0, 25)
    return result


def demo_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'application/json')]
    start_response(status, response_headers)
    response = json.dumps(FAKE_DATA.values())
    return [response + '\n']


if __name__ == u"__main__":
    FAKE_DATA = generate_fake_data()

    try:
        host = sys.argv[1]
        port = int(sys.argv[2])
    except IndexError:
        print(u"Data source server execution options:\n\n{0} HOST PORT\n".format(
            sys.argv[0]))
        sys.exit(1)

    httpd = make_server(host, port, demo_app)
    print(u"Data source server is running on {0}:{1}".format(host, port))
    httpd.serve_forever()
