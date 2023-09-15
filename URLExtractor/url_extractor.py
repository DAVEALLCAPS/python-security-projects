import requests 
from bs4 import BeautifulSoup 

def get_links(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    links = set()  # Initialize as a set
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('http'):
            links.add(href)  # Add URL to the set
        else:
            links.add(url + href)  # Add URL to the set
    return links

if __name__ == "__main__" : 
    url = input("Enter URL: ")
    if 'http' not in url: 
        url = 'http://' + url 
    links = get_links(url)

    # Save to file
    with open('extracted_links.txt', 'w') as f:
        for link in links:
            f.write(link + '\n')

    print("\nLINKS saved to extracted_links.txt:")
    for link in links:
        print(link)
