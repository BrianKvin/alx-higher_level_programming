#!/bin/bash
# send a request to an URL with curl and display response size body
curl -s "$1" | wc -c
