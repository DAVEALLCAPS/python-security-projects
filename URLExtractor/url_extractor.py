import requests 
from bs4 import BeautifulSoup 
from urllib.parse import urlparse
from collections import Counter
from urllib.parse import urljoin
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

MAX_DEPTH = 2

def get_links_recursive(url, base_domain, depth=0, visited=None):
    if visited is None:
        visited = set()
    
    logging.info(f"Crawling URL: {url} at depth: {depth}")
    
    if url in visited:
        logging.debug(f"URL already visited: {url}")
        return set()
    if depth > MAX_DEPTH:
        logging.debug(f"Max depth reached: {url} at depth {depth}")
        return set()
    
    visited.add(url)
    
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    links = set()

    for link in soup.find_all('a', href=True):
        href = link['href']
        full_link = urljoin(url, href)
        domain = urlparse(full_link).netloc

        if base_domain in domain:
            links.add(full_link)
            if full_link not in visited:
                logging.debug(f"Adding link to crawl: {full_link}")
                links.update(get_links_recursive(full_link, base_domain, depth+1, visited))
            else:
                logging.debug(f"Link already visited: {full_link}")

    return links

def summarize_links(links):
    SEPARATOR = "-" * 75
    HEADER = "LINK SUMMARY"
    FOOTER = "=" * 75

    total_links = len(links)
    http_count = sum(1 for link in links if link.startswith('http://'))
    https_count = sum(1 for link in links if link.startswith('https://'))

    domains = [urlparse(link).netloc for link in links]
    most_common_domain = Counter(domains).most_common(1)[0]
    unique_domains = sorted(set(domains))
    domain_count = len(unique_domains)

    print(SEPARATOR)
    print(HEADER.center(75))
    print(SEPARATOR)
    print(f"Total links: {total_links}")
    print(f"Protocols - HTTP: {http_count} | HTTPS: {https_count}")
    print(f"Most common domain: {most_common_domain[0]} (found {most_common_domain[1]} times)")
    print(f"Unique domains: {domain_count}")
    print(SEPARATOR)
    for domain in unique_domains:
        print(domain)
    print(FOOTER)

if __name__ == "__main__": 
    url = input("Enter URL: ").strip()
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url 

    base_domain = urlparse(url).netloc
    links = get_links_recursive(url, base_domain)

    with open('extracted_links.txt', 'w') as f:
        for link in links:
            f.write(link + '\n')

    print("=" * 75)
    print(f'Successfully grabbed links from {url} and saved to extracted_links.txt!')
    summarize_links(links)
