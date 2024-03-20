from pywebio.input import input, TEXT
from pywebio.output import put_html
import requests
from bs4 import BeautifulSoup
import random
import time

def fetch_gifs(keyword):
    url = f"https://www.google.com/search?q={keyword}&tbm=isch"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    return [image['src'] for image in images]

def display_slideshow(gifs):
    html_code = ""
    for gif in gifs:
        html_code += f'<img src="{gif}" width="300" height="300">'
    put_html(html_code)

def main():
    keyword = input("Enter the keyword to search for GIFs:", type=TEXT, placeholder="e.g., cute birthday gif").strip()
    gifs = fetch_gifs(keyword)
    if len(gifs) >= 3:
        display_slideshow(random.sample(gifs, 3))
    else:
        put_html("<p>No GIFs found. Please try again with different keywords.</p>")

if __name__ == "__main__":
    main()
