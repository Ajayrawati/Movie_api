import requests
from bs4 import BeautifulSoup
import json


def format_imdb_url(url):
   
    # Trim everything after '?' if present
    trimmed_url = url.split('?')[0]
    # Add prefix if not present
    if not trimmed_url.startswith("https://www.imdb.com/"):
        trimmed_url = "https://www.imdb.com/" + trimmed_url
    return trimmed_url



def extract_next_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all script tags of type 'application/ld+json'
    json_ld_data = soup.find_all('script', type="application/ld+json")
    
    # Extract and return the JSON-LD data from the first script tag (if available)
    if json_ld_data:
        return json.loads(json_ld_data[0].string)
    return None



def extract_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    # Parse the HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract relevant section
    results_section = soup.find('section', class_='ipc-page-section ipc-page-section--base sc-b03627f1-0 dOfhDK')


    results_section
    # # Find all result items
    results = results_section.find_all('li', class_='ipc-metadata-list-summary-item')
    results

    # Iterate through results and extract details
    extracted_data = {}
    for result in results:
        title_tag = result.find('a', class_='ipc-metadata-list-summary-item__t')
        year_tag = result.find('span', class_='ipc-metadata-list-summary-item__li')
        actors_tag = result.find('ul', class_='ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--no-wrap ipc-inline-list--inline ipc-metadata-list-summary-item__stl base')

        actors = ", ".join([li.text for li in actors_tag.find_all('li')]) if actors_tag else "Unknown"
        year = year_tag.text if year_tag else "Unknown"
        title = title_tag.text
        url = title_tag.get('href')
        nextUrl = format_imdb_url(url)
        description = extract_next_page(nextUrl)
        extracted_data.append({
                    'title': title,
                    'url': nextUrl,
                    'year': year,
                    'actors': actors,
                    'description':description
                })
            
    return extracted_data


# query = input("Enter movie name : ")
# query = query.replace(" ","%20")
# #test for the antman
# print(query)
# # URL for IMDb search results
# url = f"https://www.imdb.com/find/?q={query}"




# with open("imdb_results.json", "a") as json_file:
#     json.dump(extracted_data, json_file, indent=4)


