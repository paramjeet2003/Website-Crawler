# Web Crawler and Enumeration Script

This script is designed to perform web crawling, subdomain enumeration, and directory enumeration. It uses Python with the `requests`, `threading`, `sys`, `re`, and `urllib.parse` libraries.

## Features

- **Subdomain Enumeration**: Discovers potential subdomains from a given domain.
- **Directory Enumeration**: Searches for hidden or unlinked directories.
- **Web Crawling**: Extracts all unique links from the initial web page of the specified domain.

## Prerequisites

- Python 3.x
- `requests` library
- `urllib.parse` for URL handling
- `re` for regular expression operations

## Installation

First, ensure that Python 3 and pip are installed on your system. You can install the required packages using:

```bash
pip install requests
```

## Usage
```bash
git clone https://github.com/paramjeet2003/Website-Crawler.git
cd Website-Crawler
chmod +x test.sh
./test.sh example.com
```

## Output Files
- `subdomains`: Contains all discovered subdomains.
- `directories`: Contains all discovered directories.
- `spider`: Contains all unique links extracted from the website.

## Note
- Ensure you have the necessary permissions to scan or crawl the website. Unauthorized scanning can lead to legal actions.
- This script is for educational purposes only.


## Author
`Paramjeet Singh`
