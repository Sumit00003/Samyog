# crawler.py

import urllib.parse as urlparse
import requests
from bs4 import BeautifulSoup

class SimpleCrawler:
    def __init__(self, base_url,output_file=None):
        self.base_url = base_url
        self.visited_links = set()
        self.output_file = output_file

    def extract_links_from(self, url):
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.content, "html.parser")
            return [
                urlparse.urljoin(url, a.get("href"))
                for a in soup.find_all("a", href=True)
            ]
        except requests.RequestException as e:
            print(f"[!] Request failed: {e}")
            return []

    def crawl(self, url=None):
        if url is None:
            url = self.base_url

        if url in self.visited_links or not url.startswith(self.base_url):
            return

        print(url)
        self.visited_links.add(url)
        
        with open(self.output_file, "a") as f:
            f.write(url + "\n")

        for link in self.extract_links_from(url):
            link = link.split("#")[0]  # Remove fragment
            self.crawl(link)

