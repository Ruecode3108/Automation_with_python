import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/moviemeter/"

# 1. Fetch the page content
response = requests.get(url)

# 2. Parse the content
soup = BeautifulSoup(response.content, "html.parser")

# 3. Select all movie rows
# NOTE: The class names for the structure have changed on IMDb's site.
# It's more reliable to select all <tr> elements within the main list.
movies = soup.select("ul.ipc-metadata-list > li")

print("Top Trending movies on IMDb:\n")

# 4. Iterate and extract data (up to the first 10)
for movie in movies[:10]:
    # Extract Title and Year (these are often in the same tag structure)
    try:
        # Find the main title/year div
        title_tag = movie.find("div", class_="ipc-title")
        if title_tag:
            # The title text is usually the last child element's text
            title = title_tag.find("h3", class_="ipc-title__text").text.split('.', 1)[-1].strip()
            
            # Find the year/duration/certificate info div
            metadata_tag = movie.find("div", class_="ipc-metadata-list-item__content")
            
            # The year is often the first span in the metadata section
            year = metadata_tag.find("span", class_="sc-b069d2a6-5")
            year = year.text.strip() if year else "N/A"
            
            # The rating is in a separate span within the rating div
            rating_tag = movie.find("span", class_="ipc-rating-star--imdb")
            rating = rating_tag.find("span").text.split('(')[0].strip() if rating_tag else "N/A"

            # 5. Print the result INSIDE the loop
            print(f"🎬 {title} ({year}) - ⭐ {rating}")

    except AttributeError:
        # Simple error handling in case a movie entry is malformed or structure changes
        print("Could not extract data for one of the movies due to structure change.")