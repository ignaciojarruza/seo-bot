from openai import OpenAI
import argparse
import os

api_key = os.environ.get('OPENAI_API_KEY')

intro_message = """
Welcome to the SEO Bot!

This command-line tool is designed to assist you in optimizing your content for 
search engines. By leveraging OpenAI's powerful language models, the SEO Bot 
generates recommended titles, summaries, and keywords based on your article or 
text descriptions. Whether you're a content creator, marketer, or SEO enthusiast,
this tool aims to streamline the process of crafting engaging and discoverable content.

Simply input your article or text description, and let the SEO Bot provide you with valuable
insights to enhance your online visibility and drive organic traffic. Let's get started!\n
"""

def generate_recommendations(text):
    # Call openai API
    client = OpenAI(
        api_key = os.environ.get("OPENAI_API_KEY"),
    )
    seo_recommendations = client.chat.completions.create(
        messages = [
            {
                "role":"user",
                "content": text,
            }
        ],
        model="gpt-3.5-turbo",
    )
    return seo_recommendations

def main():
    print(intro_message)
    while True:
        user_input = input("Please enter your article or text description below:\n")

        if user_input.lower() == 'exit':
            print("Exiting the program...")
            break

        print(user_input)

    #seo_recommendations = generate_recommendations(text)

    #Output
    print(seo_recommendations)

if __name__ == "__main__":
    main()