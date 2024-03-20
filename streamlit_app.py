import streamlit as st
import requests
from bs4 import BeautifulSoup
import random

def fetch_gifs(keyword):
    url = f"https://www.google.com/search?q={keyword}&tbm=isch"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    return [image['src'] for image in images]

def main():
    st.title("📸 Birthday GIF Slideshow 🎉")
    st.write("Enter a keyword to search for birthday GIFs:")
    keyword = st.text_input("Keyword", "cute birthday gif")
    if st.button("Generate Slideshow"):
        gifs = fetch_gifs(keyword)
        if len(gifs) >= 3:
            st.write("Here are your birthday GIFs:")
            for gif in random.sample(gifs, 3):
                st.image(gif, use_column_width=True)
        else:
            st.write("No GIFs found. Please try again with different keywords.")

if __name__ == "__main__":
    main()
