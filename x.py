from selenium import webdriver
from selenium.webdriver.common.by import By
import pytesseract
from PIL import Image
import io
import re

def main():
    url1 = 'http://ctf.b01lers.com:5125/'
    driver = webdriver.Firefox()
    visited = set()
    url = url1
    
    while True:
        if url not in visited:
            visited.add(url)
            print('Crawling: ', url)
            driver.get(url)
            link = driver.find_element(By.TAG_NAME, 'span').text
            if '.' in link:
                ss = driver.get_screenshot_as_png()
                im = Image.open(io.BytesIO(ss))
                text = pytesseract.image_to_string(im, lang='eng')
                print(text)
                link = re.search('"(.*)’', text).group(1)
            url = url1+link+'.html'

    driver.quit()


if __name__ == '__main__':
    main()