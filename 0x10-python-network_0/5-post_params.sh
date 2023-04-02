#!/bin/bash
# send a POST request to the passed URL using curl, and display the body
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
