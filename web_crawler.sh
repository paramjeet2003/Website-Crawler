#!/bin/bash
name=$1
if [ $# -ne 1 ]; then
	echo "Usage: $0 example.com"
	exit 1
fi
python3 web_crawler.py $name
