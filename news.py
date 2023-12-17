import requests
import json
from bs4 import BeautifulSoup

# URL of the movie news page to scrape
url = 'https://www.hollywoodreporter.com/c/movies/movie-news/'

# Headers to mimic a browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


# Send get request to the website
response = requests.get(url, headers=headers)

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(response.text, 'html.parser')

# Select the common parent elements of titles and descriptions
news_items = soup.select('.lrv-a-grid')

# Initialize an empty list to hold the news items
news_data = []

# Loop through each news item
for item in news_items:
    title = item.select_one('.c-title')
    description = item.select_one('.c-dek')
    img = item.select_one('.c-lazy-image__img')

    if title and description:
        news_dict = {
            "Title": title.get_text(strip=True),
            "Description": description.get_text(strip=True),
            "Img Link": img.get('data-src') or img.get('src')  # Get the image URL
        }
        # print(f"Title: {title.get_text(strip=True)}")
        # print(f"Description: {description.get_text(strip=True)}\n")
        # img_url = img.get('data-lazy-src')  # Get the 'src' attribute of the image tag
        # print(f"Img Link: {img_url}\n")
        news_data.append(news_dict)

# Convert the list of dictionaries to a JSON string
json_output = json.dumps(news_data)

# Print the JSON string
print(json_output)