import streamlit as st

def display_photobook():
    # Displaying the provided birthday card image as the first photo
    st.image("https://img.freepik.com/premium-vector/cute-happy-birthday-card-template_129604-1351.jpg", use_column_width=True)
    
    # Dictionary of photos and birthday quotes
    photo_quotes = {
        "photo2.jpg": "Age is merely the number of years the world has been enjoying you. Happy birthday!",
        "photo3.jpg": "Wishing you a day filled with love, laughter, and unforgettable memories. Happy birthday!",
        "photo4.jpg": "On your special day, may all your dreams and wishes come true. Happy birthday!",
    }

    # Displaying photos with corresponding birthday quotes
    for photo, quote in photo_quotes.items():
        if st.button(f"Click to reveal: {quote}"):
            st.image(photo, use_column_width=True)

    # Displaying the GIF as the third object
    st.image("https://64.media.tumblr.com/6f8c976e4b9ca4fb6ef602a209d5dc1d/75977a3f5d4ae7cd-d4/s1280x1920/edba661c8a5866ea61279b58d6dcc9c609b22b9b.gif", use_column_width=True)

    # Personalized happy birthday greeting
    st.header("🎂 Happy 37th Birthday!")
    st.write("Wishing you a fantastic birthday filled with love, laughter, and cherished moments. May this year be your best one yet!")

# Title and Introduction
st.title("📸 Birthday Photobook 🎉")
st.write("Explore the pages of this photobook to celebrate your special day!")

# Display the photobook
display_photobook()
