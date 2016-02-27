# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time

from graphite_api.intervals import Interval, IntervalSet
from graphite_api.node import LeafNode
import requests


class Finder(object):
    def __init__(self, config=None):
        self.api_url = config['plugin'].get('api_url')
        self.path = config['plugin'].get('path')

        if not all([self.api_url, self.path]):
            raise KeyError("Both 'api_url' and 'path' variables must be "
                           "present in configuration file.")

    def find_nodes(self, query):
        reader = Reader(self.path, self.api_url)
        yield LeafNode(self.path, reader)


class Reader(object):
    __slots__ = ('path', 'api_url')

    def __init__(self, path, api_url):
        self.path = path
        self.api_url = api_url

    def fetch(self, start_time, end_time):
        step = 60
        time_info = start_time, end_time, step
        resp = requests.get(self.api_url)
        return time_info, resp.json()

    def get_intervals(self):
        return IntervalSet([Interval(0, int(time.time()))])
