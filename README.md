# APKMirror Crawler

APKMirror Crawler is a project developed for the Short Project Programming course. The purpose of the crawler is to crawl and scrape the [apkmirror](https://www.apkmirror.com) website.

## Features

1. Scrape the website given an application link
2. Scrape the website given a category link
3. Scrape the whole category section
4. Choose the number of versions of an application to download
5. Choose which spider to run
6. Append/Overwrite the output file

## Installation

Git clone the repository, switch current directory to the cloned repository and follow the installation commands

```bash 
python3 -m venv venv # Create a Python virtual environment
source venv/bin/activate # Access the Python virtual env
pip3 install -r requirements.txt # Install the requirements 
cd apkmirror_crawler/ # Switch current directory to the scraper repo
```

## Usage

```bash
python3 apkmirror_script.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
