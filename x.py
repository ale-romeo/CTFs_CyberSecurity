import requests
from bs4 import BeautifulSoup

def main():
    url1 = 'http://ctf.b01lers.com:5125/'
    visited = set()
    url = url1

    while True:
        if url not in visited:
            visited.add(url)
            print('Crawling: ', url)
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            link = soup.find('span').get_text()
            url = url1+link+'.html'


if __name__ == '__main__':
    main()