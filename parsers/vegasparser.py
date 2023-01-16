import urllib.request, json 

url_dict = {
    "points": "https://sportsbook.draftkings.com//sites/US-NJ-SB/api/v5/eventgroups/42648/categories/1215?format=json",
    "rebounds": "https://sportsbook.draftkings.com//sites/US-NJ-SB/api/v5/eventgroups/42648/categories/1216?format=json",
    "assists": "https://sportsbook.draftkings.com//sites/US-NJ-SB/api/v5/eventgroups/42648/categories/1217?format=json",
    "threes": "https://sportsbook.draftkings.com//sites/US-NJ-SB/api/v5/eventgroups/42648/categories/1218?format=json",
    "double-doubles": "https://sportsbook.draftkings.com//sites/US-NJ-SB/api/v5/eventgroups/42648/categories/583/subcategories/7136?format=json",
    "triple-doubles": "https://sportsbook.draftkings.com//sites/US-NJ-SB/api/v5/eventgroups/42648/categories/583/subcategories/7137?format=json",
    "blocks": "https://sportsbook.draftkings.com//sites/US-NJ-SB/api/v5/eventgroups/42648/categories/1219/subcategories/12499?format=json",
    "steals": "https://sportsbook.draftkings.com//sites/US-NJ-SB/api/v5/eventgroups/42648/categories/1219/subcategories/12500?format=json",
    "turnovers": "https://sportsbook.draftkings.com//sites/US-NJ-SB/api/v5/eventgroups/42648/categories/1220?format=json",
}

# get JSON file from web, convert into Python dictionary
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
                    subcategory = descriptor.get("offerSubcategory")
                    offers = subcategory.get("offers")
                    for gameOffers in offers:
                        for offer in gameOffers:
                            # this outcomes get is index out of bounds sometimes, investigate this
                            # if possible
                            outcomesList = offer.get("outcomes")
                            if len(outcomesList) == 0:
                                # print out info to avoid index out of bounds
                                print("No outcomes found")
                                print("Here is the offers object: ")
                                print(offers)
                                return

                            outcome = outcomesList[0]
                            # this covers double doubles and triple doubles for now, as those come in as "None"
                            if subcategory.get("name") == "Double-Double" or subcategory.get("name") == "Triple-Double":
                                props_dict[outcome.get("participant")] = 1 / outcome.get("oddsDecimal")
                            else:
                                props_dict[outcome.get("participant")] = outcome.get("line") or 0

    return props_dict

# def get_points():
#     return get_props_base(url_dict.get("points"))

def get_points():
    # change URL
    url = url_dict.get("points");
    props_dict = {}
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())
    categories = data.get("eventGroup").get("offerCategories")
    # need category with player props
    for category in categories:
        # change category name
        if category.get("name") == "Player Points":
            descriptors = category.get("offerSubcategoryDescriptors")
            for descriptor in descriptors:
                if "offerSubcategory" in descriptor:
                    # offers broken up by game
                    subcategory = descriptor.get("offerSubcategory")
                    offers = subcategory.get("offers")
                    for gameOffers in offers:
                        for offer in gameOffers:
                            # this outcomes get is index out of bounds sometimes, investigate this
                            # if possible
                            outcomesList = offer.get("outcomes")
                            if len(outcomesList) == 0:
                                # print out info to avoid index out of bounds
                                print("No outcomes found")
                                print("Here is the offers object: ")
                                print(offers)
                                return

                            outcome = outcomesList[0]
                            # this covers double doubles and triple doubles for now, as those come in as "None"
                            if subcategory.get("name") == "Double-Double" or subcategory.get("name") == "Triple-Double":
                                props_dict[outcome.get("participant")] = 1 / outcome.get("oddsDecimal")
                            else:
                                # confirm output makes sense
                                # print(outcome.get("participant"))
                                # print(outcome.get("line"))
                                props_dict[outcome.get("participant")] = outcome.get("line") or 0

    return props_dict

# def get_rebounds():
#     return get_props_base(url_dict.get("rebounds"))

def get_rebounds():
    # change URL
    url = url_dict.get("rebounds");
    props_dict = {}
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())
    categories = data.get("eventGroup").get("offerCategories")
    # need category with player props
    for category in categories:
        # change category name
        if category.get("name") == "Player Rebounds":
            descriptors = category.get("offerSubcategoryDescriptors")
            for descriptor in descriptors:
                if "offerSubcategory" in descriptor:
                    # offers broken up by game
                    subcategory = descriptor.get("offerSubcategory")
                    offers = subcategory.get("offers")
                    for gameOffers in offers:
                        for offer in gameOffers:
                            # this outcomes get is index out of bounds sometimes, investigate this
                            # if possible
                            outcomesList = offer.get("outcomes")
                            if len(outcomesList) == 0:
                                # print out info to avoid index out of bounds
                                print("No outcomes found")
                                print("Here is the offers object: ")
                                print(offers)
                                return

                            outcome = outcomesList[0]
                            # this covers double doubles and triple doubles for now, as those come in as "None"
                            if subcategory.get("name") == "Double-Double" or subcategory.get("name") == "Triple-Double":
                                props_dict[outcome.get("participant")] = 1 / outcome.get("oddsDecimal")
                            else:
                                # confirm output makes sense
                                # print(outcome.get("participant"))
                                # print(outcome.get("line"))
                                props_dict[outcome.get("participant")] = outcome.get("line") or 0

    return props_dict

# def get_assists():
#     return get_props_base(url_dict.get("assists"))

def get_assists():
    # change URL
    url = url_dict.get("assists");
    props_dict = {}
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())
    categories = data.get("eventGroup").get("offerCategories")
    # need category with player props
    for category in categories:
        # change category name
        if category.get("name") == "Player Assists":
            descriptors = category.get("offerSubcategoryDescriptors")
            for descriptor in descriptors:
                if "offerSubcategory" in descriptor:
                    # offers broken up by game
                    subcategory = descriptor.get("offerSubcategory")
                    offers = subcategory.get("offers")
                    for gameOffers in offers:
                        for offer in gameOffers:
                            # this outcomes get is index out of bounds sometimes, investigate this
                            # if possible
                            outcomesList = offer.get("outcomes")
                            if len(outcomesList) == 0:
                                # print out info to avoid index out of bounds
                                print("No outcomes found")
                                print("Here is the offers object: ")
                                print(offers)
                                return

                            outcome = outcomesList[0]
                            # this covers double doubles and triple doubles for now, as those come in as "None"
                            if subcategory.get("name") == "Double-Double" or subcategory.get("name") == "Triple-Double":
                                props_dict[outcome.get("participant")] = 1 / outcome.get("oddsDecimal")
                            else:
                                # confirm output makes sense
                                # print(outcome.get("participant"))
                                # print(outcome.get("line"))
                                props_dict[outcome.get("participant")] = outcome.get("line") or 0

    return props_dict

# def get_threes():
#     return get_props_base(url_dict.get("threes"))

def get_threes():
    # change URL
    url = url_dict.get("threes");
    props_dict = {}
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())
    categories = data.get("eventGroup").get("offerCategories")
    # need category with player props
    for category in categories:
        # change category name
        if category.get("name") == "Player Threes":
            descriptors = category.get("offerSubcategoryDescriptors")
            for descriptor in descriptors:
                if "offerSubcategory" in descriptor:
                    # offers broken up by game
                    subcategory = descriptor.get("offerSubcategory")
                    offers = subcategory.get("offers")
                    for gameOffers in offers:
                        for offer in gameOffers:
                            # this outcomes get is index out of bounds sometimes, investigate this
                            # if possible
                            outcomesList = offer.get("outcomes")
                            if len(outcomesList) == 0:
                                # print out info to avoid index out of bounds
                                print("No outcomes found")
                                print("Here is the offers object: ")
                                print(offers)
                                return

                            outcome = outcomesList[0]
                            # this covers double doubles and triple doubles for now, as those come in as "None"
                            if subcategory.get("name") == "Double-Double" or subcategory.get("name") == "Triple-Double":
                                props_dict[outcome.get("participant")] = 1 / outcome.get("oddsDecimal")
                            else:
                                # confirm output makes sense
                                # print(outcome.get("participant"))
                                # print(outcome.get("line"))
                                props_dict[outcome.get("participant")] = outcome.get("line") or 0

    return props_dict

# def get_double_doubles():
#     return get_props_base(url_dict.get("double-doubles"))

def get_double_doubles():
    # change URL
    url = url_dict.get("double-doubles");
    props_dict = {}
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())
    categories = data.get("eventGroup").get("offerCategories")
    # need category with player props
    for category in categories:
        # change category name
        if category.get("name") == "Player Rebounds":
            descriptors = category.get("offerSubcategoryDescriptors")
            for descriptor in descriptors:
                if "offerSubcategory" in descriptor:
                    # offers broken up by game
                    subcategory = descriptor.get("offerSubcategory")
                    offers = subcategory.get("offers")
                    for gameOffers in offers:
                        for offer in gameOffers:
                            # this outcomes get is index out of bounds sometimes, investigate this
                            # if possible
                            outcomesList = offer.get("outcomes")
                            if len(outcomesList) == 0:
                                # print out info to avoid index out of bounds
                                print("No outcomes found")
                                print("Here is the offers object: ")
                                print(offers)
                                return

                            outcome = outcomesList[0]
                            # this covers double doubles and triple doubles for now, as those come in as "None"
                            if subcategory.get("name") == "Double-Double" or subcategory.get("name") == "Triple-Double":
                                props_dict[outcome.get("participant")] = 1 / outcome.get("oddsDecimal")
                            else:
                                # confirm output makes sense
                                # print(outcome.get("participant"))
                                # print(outcome.get("line"))
                                props_dict[outcome.get("participant")] = outcome.get("line") or 0

    return props_dict

def get_triple_doubles():
    return get_props_base(url_dict.get("triple-doubles"))

def get_blocks():
    return get_props_base(url_dict.get("blocks"))

def get_steals():
    return get_props_base(url_dict.get("steals"))

def get_turnovers():
    return get_props_base(url_dict.get("turnovers"))
