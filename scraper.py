import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citation_needed_tags = soup.find_all('sup', class_='noprint Inline-Template')
    return len(citation_needed_tags)


def get_citations_needed_report(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citation_needed_tags = soup.find_all('sup', class_='noprint Inline-Template')

    report = ''
    for tag in citation_needed_tags:
        parent = tag.find_parent()
        if parent:
            report += parent.text + '\n\n'
    return report


# Test the functions
wiki_url = 'https://en.wikipedia.org/wiki/Cayman_Islands'
print(get_citations_needed_count(wiki_url))
print(get_citations_needed_report(wiki_url))
