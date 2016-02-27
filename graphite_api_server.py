from __future__ import print_function
from __future__ import unicode_literals

import sys
from wsgiref.simple_server import make_server

from graphite_api.app import app

if __name__ == u"__main__":
    try:
        host = sys.argv[1]
        port = int(sys.argv[2])
    except IndexError:
        print(
            u"Graphite API server execution options:\n\n{0} HOST PORT\n".format(
                sys.argv[0]))
        sys.exit(1)

    httpd = make_server(host, port, app)
    print(u"Graphite API server is running on {0}:{1}".format(host, port))
    httpd.serve_forever()
