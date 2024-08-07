# -*- coding: utf-8 -*-
"""Naga Prasad Task-3.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10ymGnqdZtX8KnwfWgKslI1NI4Ve9jIlG
"""

#MainFlow Python Developer Internship Task-3 by Naga Prasad S

import requests
from bs4 import BeautifulSoup

# URL of the web page to scrape
url = 'https://www.parsehub.com/blog/what-is-web-scraping/'
# Replace with the URL of the web page you want to scrape

# Send a GET request to the web page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all the text from the page
    page_text = soup.get_text()

    # Extract all the links from the page
    links = [a["href"] for a in soup.find_all('a', href=True)]

    # Extract all the images from the page
    images = [img['src'] for img in soup.find_all('img', src=True)]

    #Print the extracted data
    print("Page Text:")
    print(page_text)
    print("\nLinks:")
    for link in links:
        print(link) # Indent this line to include it in the for loop
    print("\nImages:")
    for image in images:
        print(image) # Indent this line to include it in the for loop
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}") # Fix the f-string formatting