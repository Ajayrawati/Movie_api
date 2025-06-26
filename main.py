import requests
from bs4 import BeautifulSoup
import json


def format_imdb_url(url):
    """Ensure full IMDb URL"""
    trimmed_url = url.split('?')[0]
    if not trimmed_url.startswith("https://www.imdb.com/"):
        trimmed_url = "https://www.imdb.com" + trimmed_url
    return trimmed_url


def extract_next_page(url):
    """Fetch movie description from individual IMDb page"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Try plot-l, then plot-xl (IMDb changes frequently)
        description_tag = soup.find('span', {'data-testid': 'plot-l'})
        if not description_tag:
            description_tag = soup.find('span', {'data-testid': 'plot-xl'})

        return description_tag.text.strip() if description_tag else 'No description available.'
    except Exception as e:
        return f"Failed to fetch description: {str(e)}"


def extract_info(query):
    """Search IMDb and extract top movie results"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    # Construct search URL
    search_url = f"https://www.imdb.com/find/?q=inception"
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # IMDb results are in <li> with class 'ipc-metadata-list-summary-item'
    results = soup.find_all('li', class_='ipc-metadata-list-summary-item')
    extracted_data = []

    for result in results[:5]:  # Limit to top 5
        # Title
        title_tag = result.find('a', class_='ipc-metadata-list-summary-item__t')
        if not title_tag:
            continue

        title = title_tag.text.strip()
        partial_url = title_tag['href']
        full_url = format_imdb_url(partial_url)

        # Year
        year_tag = result.find('span', class_='ipc-metadata-list-summary-item__li')
        year = year_tag.text.strip() if year_tag else "Unknown"

        # Actors
        actors = "Unknown"
        actor_ul = result.find_all(
            'ul',
            class_='ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--no-wrap ipc-inline-list--inline ipc-metadata-list-summary-item__stl base'
        )
        if actor_ul:
            actor_lis = actor_ul[0].find_all('li')
            actors = ", ".join(li.text.strip() for li in actor_lis)

        # Description from detail page
        description = extract_next_page(full_url)

        # Append all
        extracted_data.append({
            'title': title,
            'url': full_url,
            'year': year,
            'actors': actors,
            'description': description
        })

    return extracted_data

# Uncomment to test as a script
# if __name__ == "__main__":
#     query = input("Enter movie name: ")
#     data = extract_info(query)
#     print(json.dumps(data, indent=4))
#     with open("imdb_results.json", "w") as f:
#         json.dump(data, f, indent=4)
