#!/bin/bash
# Displays all the HTTP mettods the server will accept
curl -sIX OPTIONS "$1" | grep "Allow: " | cut -d " " -f 2-
