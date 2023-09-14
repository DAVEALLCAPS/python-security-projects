import requests 
from bs4 import BeautifulSoup 

# TODO: Need to implement dupe removal for links.

def get_links(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    links = []
    for link in soup.find_all('a', href=True):
        if link['href'].startswith('http'):
            links.append(link['href'])
        else:
            links.append(url + link['href'])
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
