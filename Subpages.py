import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_all_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = set()
        for a_tag in soup.find_all('a', href=True):
            href = a_tag.get('href')
            full_url = urljoin(url, href)
            if url in full_url:
                links.add(full_url)
        return links
    except requests.RequestException as e:
        print(f"Error: {e}")
        return set()


website_url = 'https://example.com'
subpages = get_all_links(website_url)

for link in subpages:
    print(link)
