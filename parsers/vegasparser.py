import urllib.request, json 

# TODO: figure out a plan for double doubles and triple doubles, all being assigned "None" right now since they're yes/no
# idea for above: gather points, rebounds, assists, blocks, steals for each player and see which of those are >10

url_dict = {
    "points": "https://sportsbook-us-nh.draftkings.com//sites/US-NH-SB/api/v4/eventgroups/88670846/categories/583/subcategories/4991?format=json",
    "rebounds": "https://sportsbook-us-nh.draftkings.com//sites/US-NH-SB/api/v4/eventgroups/88670846/categories/583/subcategories/4992?format=json",
    "assists": "https://sportsbook-us-nh.draftkings.com//sites/US-NH-SB/api/v4/eventgroups/88670846/categories/583/subcategories/5000?format=json",
    "threes": "https://sportsbook-us-nh.draftkings.com//sites/US-NH-SB/api/v4/eventgroups/88670846/categories/583/subcategories/6209?format=json",
    "double-doubles": "https://sportsbook-us-nh.draftkings.com//sites/US-NH-SB/api/v4/eventgroups/88670846/categories/583/subcategories/7136?format=json",
    "triple-doubles": "https://sportsbook-us-nh.draftkings.com//sites/US-NH-SB/api/v4/eventgroups/88670846/categories/583/subcategories/7137?format=json",
    "blocks": "https://sportsbook-us-nh.draftkings.com//sites/US-NH-SB/api/v4/eventgroups/88670846/categories/583/subcategories/7346?format=json",
    "steals": "https://sportsbook-us-nh.draftkings.com//sites/US-NH-SB/api/v4/eventgroups/88670846/categories/583/subcategories/9971?format=json",
    "turnovers": "https://sportsbook-us-nh.draftkings.com//sites/US-NH-SB/api/v4/eventgroups/88670846/categories/583/subcategories/7965?format=json",
}

# get JSON file from web, convert into Python dictionary
# TODO: check if anything about this URL changes day-by-day (ex. the 88670846)
def get_props_base(url):
    props_dict = {}
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())
    categories = data.get("eventGroup").get("offerCategories")
    # need category with player props
    for category in categories:
        if category.get("name") == "Player Props":
            descriptors = category.get("offerSubcategoryDescriptors")
            for descriptor in descriptors:
                if "offerSubcategory" in descriptor:
                    # offers broken up by game
                    offers = descriptor.get("offerSubcategory").get("offers")
                    for gameOffers in offers:
                        for offer in gameOffers:
                            outcome = offer.get("outcomes")[0]
                            # this covers double doubles and triple doubles for now, as those come in as "None"
                            props_dict[outcome.get("participant")] = outcome.get("line") or 0

    return props_dict

def get_points():
    return get_props_base(url_dict.get("points"))

def get_rebounds():
    return get_props_base(url_dict.get("rebounds"))

def get_assists():
    return get_props_base(url_dict.get("assists"))

def get_threes():
    return get_props_base(url_dict.get("threes"))

def get_double_doubles():
    return get_props_base(url_dict.get("double-doubles"))

def get_triple_doubles():
    return get_props_base(url_dict.get("triple-doubles"))

def get_blocks():
    return get_props_base(url_dict.get("blocks"))

def get_steals():
    return get_props_base(url_dict.get("steals"))

def get_turnovers():
    return get_props_base(url_dict.get("turnovers"))
