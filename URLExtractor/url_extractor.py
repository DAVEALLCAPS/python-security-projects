import requests 
from bs4 import BeautifulSoup 
from urllib.parse import urlparse
from collections import Counter

def get_links(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    links = set()
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('http'):
            links.add(href)
        else:
            links.add(url + href)
    return links

def summarize_links(links):
    # Styling constants
    SEPARATOR = "-" * 75
    HEADER = "LINK SUMMARY"
    FOOTER = "=" * 75

    # Total number of links
    total_links = len(links)

    # HTTP vs HTTPS count
    http_count = sum(1 for link in links if link.startswith('http://'))
    https_count = sum(1 for link in links if link.startswith('https://'))

    # Most common domain
    domains = [urlparse(link).netloc for link in links]
    most_common_domain = Counter(domains).most_common(1)[0]

    # Unique domains
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

if __name__ == "__main__" : 
    url = input("Enter URL: ")
    if 'http' not in url: 
        url = 'http://' + url 
    links = get_links(url)

    # Save to file
    with open('extracted_links.txt', 'w') as f:
        for link in links:
            f.write(link + '\n')

    print("=" * 75)
    print(f'Successfully grabbed links from {url} and saved to extracted_links.txt!')
    summarize_links(links)
