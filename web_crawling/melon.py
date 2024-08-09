from bs4 import BeautifulSoup
import requests
import csv

def crawling_melon_chart():
    url = "https://www.melon.com/chart/index.htm"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15'
    }

    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    ranks = []
    titles = []
    artists = []
    albums = []

    for row in soup.select('tr[data-song-no]'):
        rank = row.select_one('.rank').text.strip()
        title = row.select_one('.ellipsis.rank01 a').text.strip()
        artist = row.select_one('.ellipsis.rank02 a').text.strip()
        album = row.select_one('.ellipsis.rank03 a').text.strip()

        ranks.append(rank)
        titles.append(title)
        artists.append(artist)
        albums.append(album)

    with open('data/melon_chart.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Rank", "Title", "Artist", "Album"])
        for i in range(len(ranks)):
            writer.writerow([ranks[i], titles[i], artists[i], albums[i]])

if __name__ == "__main__":
    crawling_melon_chart()