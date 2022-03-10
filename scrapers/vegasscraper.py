import requests
from bs4 import BeautifulSoup

# this file will grab player props from DraftKings Sportsbook and use those projections,
# along with scoring rules, to calculate a projected DFS score for each player 
# We'll end up needing 9 scraping functions that call the base
# Putting this on pause for now, as we're going to attempt to parse a json feed with the lines

# base scraping function: other functions will call on this and pass in proper URL
# returns a Dictionary<PlayerName, Float>, where float is projected value
def get_base_props(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    #dictionary
    prop_dict = {}

    print(soup)
    #tables = soup.find_all("table", class_="sportsbook-table")
    tables = soup.find_all("table")
    #print(tables.count)
    for table in tables:
        print("tables!!!!!")
    
    print("oof")
    #body = table.find("tbody", class_="sportsbook-table__body")
    #rows = body.find_all("tr")

# TODO: need to check if this number in here (88670846) changes daily
get_base_props("https://sportsbook.draftkings.com/leagues/basketball/88670846?category=player-props&subcategory=points")