import argparse
import config.state as state
import config.env as env
from urllib.parse import urlparse,urljoin,quote_plus
from http.server import SimpleHTTPRequestHandler, HTTPServer
import webbrowser
import requests

import simple_http_server


def start():
    parser = argparse.ArgumentParser(
        description='Run APS authentication script.')
    parser.add_argument('--APS_CLIENT_ID', required=True)
    parser.add_argument('--APS_CLIENT_SECRET', required=True)
    parser.add_argument('--APS_CALLBACK_URL', required=True)

    state.args = parser.parse_args()

    authorization_url = urljoin(
        env.authorize_url,
        '?response_type=code&client_id=' +
        state.args.APS_CLIENT_ID +
        '&redirect_uri=' +
        quote_plus(state.args.APS_CALLBACK_URL) +
        '&scope=data:read%20data:write'
    )

    try:
        webbrowser.open(authorization_url, new=0, autoraise=True)
    except ImportError:
        print("Can not import webbrowser")

    print("Go to the following link in your browser if the redirection hasn't started: ")
    print(authorization_url)

    # Start the HTTP server
    simple_http_server.startHttpServer()


if __name__ == "__main__":
    start()
