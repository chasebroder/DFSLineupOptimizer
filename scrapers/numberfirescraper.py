import requests
from bs4 import BeautifulSoup

def get_name(row):
    # using one of three possible classes: 'team-player', 'cta', 'left-aligned'
    player = row.find("td", class_="team-player")
    player_info = player.find("span", class_="player-info")
    full_name = player_info.find("a", class_="full")
    return full_name.text.strip()

def get_projections():
    # Dictionary: player name -> projection
    proj_dict = {}
    # Following tutorial from https://realpython.com/beautiful-soup-web-scraper-python/
    url = "https://www.numberfire.com/nba/daily-fantasy/daily-basketball-projection/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    # this is a class, so need to access class name
    results = soup.find("div", class_="stat-table--wrap")
    body = results.find("tbody")
    rows = body.find_all("tr")
    for row in rows:
        name = get_name(row)
        projection = row.find("td", class_="fp").text
        proj_dict[name] = float(projection)

    return proj_dict

