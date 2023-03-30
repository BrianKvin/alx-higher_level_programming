#!/bin/bash
# sends a request to a URL and displays only the status code of the response
curl -s -0 /dev/null -w "%{http_code}" "$1"
