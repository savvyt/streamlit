import streamlit as st

def display_photobook():
    # Displaying the provided birthday card image as the first photo
    st.image("https://img.freepik.com/premium-vector/cute-happy-birthday-card-template_129604-1351.jpg", use_column_width=True)
    
    # Dictionary of birthday quotes
    birthday_quotes = {
        "photo2.jpg": "Age is merely the number of years the world has been enjoying you. Happy birthday!",
        "photo3.jpg": "Wishing you a day filled with love, laughter, and unforgettable memories. Happy birthday!",
        "photo4.jpg": "On your special day, may all your dreams and wishes come true. Happy birthday!",
        "photo5.jpg": "Cheers to another year of adventures, laughter, and love. Happy birthday!",
        "photo6.jpg": "May your birthday be as amazing as you are! Wishing you all the happiness in the world.",
        "photo7.jpg": "You're not getting older, you're getting wiser. Happy birthday!",
        "photo8.jpg": "Another year older, another year bolder. Happy birthday!",
        "photo9.jpg": "Age is just a number, but life is the real celebration. Happy birthday!",
        "photo10.jpg": "Here's to growing older and still rocking it! Happy birthday!",
        "photo11.jpg": "Every year with you is better than the last. Happy birthday, my love!",
        "photo12.jpg": "Happy birthday to the one who fills my life with joy and love.",
        "photo13.jpg": "You're not just a year older, you're a year more awesome. Happy birthday!",
        "photo14.jpg": "May your birthday be the start of a year filled with good luck, good health, and much happiness."
    }

    # Displaying each photo with its corresponding birthday quote
    for photo, quote in birthday_quotes.items():
        st.image(photo, use_column_width=True)
        st.write(f"\"{quote}\"")

    # Personalized happy birthday greeting
    st.header("🎂 Happy 37th Birthday!")
    st.write("Wishing you a fantastic birthday filled with love, laughter, and cherished moments. May this year be your best one yet!")

# Title and Introduction
st.title("📸 Birthday Photobook 🎉")
st.write("Explore the pages of this photobook to celebrate your special day!")

# Display the photobook
display_photobook()
