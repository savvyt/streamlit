import streamlit as st

def display_photo_with_quote(photo_path, quote):
    col = st.columns([1, 3])
    col[0].image(photo_path, use_column_width=True)
    col[1].write(quote)

def main():
    st.title("🎉 Happy 37th Birthday!")

    # Display 14 pictures with quotes
    st.header("📸 Photobook")

    photos_with_quotes = {
        "photo1.jpg": "Wishing you a day filled with love, laughter, and all your favorite things!",
        "photo2.jpg": "May your birthday be as special and wonderful as you are.",
        "photo3.jpg": "Here's to another year of amazing adventures and unforgettable memories!",
        "photo4.jpg": "Cheers to another year of growth, happiness, and success. Happy Birthday!",
        "photo5.jpg": "On your special day, may all your dreams and wishes come true.",
        "photo6.jpg": "Sending you endless love and warm wishes on your birthday. You deserve the best!",
        "photo7.jpg": "Celebrating you today and every day. Happy 37th Birthday!",
        "photo8.jpg": "You're not just getting older, you're getting wiser and more fabulous. Happy Birthday!",
        "photo9.jpg": "Another year older, another year bolder. Keep shining bright!",
        "photo10.jpg": "Here's to celebrating the amazing person you are. Happy Birthday!",
        "photo11.jpg": "Age is just a number, but your spirit is timeless. Keep being awesome!",
        "photo12.jpg": "Life is a journey, and today, we celebrate the incredible journey you've had so far.",
        "photo13.jpg": "You make the world a better place just by being in it. Happy Birthday!",
        "photo14.jpg": "Today, we celebrate the gift of you. Wishing you a fantastic year ahead!",
    }

    for photo, quote in photos_with_quotes.items():
        display_photo_with_quote(photo, quote)
        st.write("---")

    # Happy Birthday Greeting
    st.header("🎂 Happy Birthday!")
    st.write("Wishing you a day filled with love, laughter, and unforgettable moments. Here's to another year of joy, growth, and endless possibilities. Happy 37th Birthday!")

if __name__ == "__main__":
    main()
