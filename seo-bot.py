from openai import OpenAI
import argparse
import json
import os

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

system_prompt = """
You are a search engine optimizer bot. You will take a description as input and output 3 different things: a list of recommended subject titles,
 a summary description for search engine optimization and a list of keywords separated by commas. These will be titled in the response as titles, description, and keywords. 
"""

def generate_recommendations(text):
    # Call openai API
    client = OpenAI(
        api_key = os.environ.get("OPENAI_API_KEY"),
    )
    seo_recommendations = client.chat.completions.create(
        messages = [
            {
                "role":"system",
                "content":system_prompt,
            },
            {
                "role":"user",
                "content": text,
            }
        ],
        model="gpt-3.5-turbo",
    )
    return seo_recommendations.json()

def main():
    print(intro_message)
    while True:
        user_input = input("Please enter your article or text description below:\n")

        if user_input.lower() == 'exit':
            print("Exiting the program...")
            break

        seo_recommendations = generate_recommendations(user_input)
        #convert response to json
        parsed_resonse = json.loads(seo_recommendations)
        response = parsed_resonse["choices"][0]["message"]["content"]
        sections = response.split('\n\n')
        titles = sections[0].replace('**Titles:**\n', '').split('\n')
        description = sections[1].replace('**Description:**\n', '')
        keywords = sections[2].replace('**Keywords:**\n', '').split(', ')

        # Print or use the extracted information
        print(titles)
        print(description)
        print(keywords)


if __name__ == "__main__":
    main()