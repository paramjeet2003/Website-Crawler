#!/bin/bash
name=$1
if [ $# -ne 1 ]; then
	echo "Usage: ./web_crawler.sh example.com"
	exit 1
fi
python3 web_crawler.py $name
