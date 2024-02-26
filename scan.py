import requests
from bs4 import BeautifulSoup

def append_text_to_file(website, output):
    response = requests.get(website)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()

    with open(output, 'a', encoding='utf-8') as file:
        file.write(text)

website = "https://tr.wikipedia.org/wiki/%C3%96zel:Rastgele"
output = "output.txt"

append_text_to_file(website, output)
