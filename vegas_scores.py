from rules_and_scoring.nba_classic import scoring_multiplier_dict
from parsers.vegasparser import *

# return dictionary of projected scores using Sportsbook data
def get_projections():
    # these are all dictionaries
    # deliberately excluding double-doubles and triple-doubles for now
    points = get_points()
    rebounds = get_rebounds()
    assists = get_assists()
    threes = get_threes()
    blocks = get_blocks()
    steals = get_steals()
    turnovers = get_turnovers()
    double_doubles = get_double_doubles()
    triple_doubles = get_triple_doubles()

    # dictionary to be returned
    projections_dict = {}

    # don't need to check if key exists because adding for first time
    for name in points:
        projections_dict[name] = points[name] * scoring_multiplier_dict.get("points")
    
    for name in rebounds:
        if name in projections_dict:
            projections_dict[name] += rebounds[name] * scoring_multiplier_dict.get("rebounds")
        else:
            projections_dict[name] = rebounds[name] * scoring_multiplier_dict.get("rebounds")

    for name in assists:
        if name in projections_dict:
            projections_dict[name] += assists[name] * scoring_multiplier_dict.get("assists")
        else:
            projections_dict[name] = assists[name] * scoring_multiplier_dict.get("assists")

    for name in threes:
        if name in projections_dict:
            projections_dict[name] += threes[name] * scoring_multiplier_dict.get("threes")
        else:
            projections_dict[name] = threes[name] * scoring_multiplier_dict.get("threes")

    for name in blocks:
        if name in projections_dict:
            projections_dict[name] += blocks[name] * scoring_multiplier_dict.get("blocks")
        else:
            projections_dict[name] = blocks[name] * scoring_multiplier_dict.get("blocks")

    for name in steals:
        if name in projections_dict:
            projections_dict[name] += steals[name] * scoring_multiplier_dict.get("steals")
        else:
            projections_dict[name] = steals[name] * scoring_multiplier_dict.get("steals")

    for name in turnovers:
        if name in projections_dict:
            projections_dict[name] += turnovers[name] * scoring_multiplier_dict.get("turnovers")
        else:
            projections_dict[name] = turnovers[name] * scoring_multiplier_dict.get("turnovers")

    for name in double_doubles:
        if name in projections_dict:
            projections_dict[name] += double_doubles[name] * scoring_multiplier_dict.get("double-doubles")
        else:
            projections_dict[name] = double_doubles[name] * scoring_multiplier_dict.get("double-doubles")

    for name in triple_doubles:
        if name in projections_dict:
            projections_dict[name] += triple_doubles[name] * scoring_multiplier_dict.get("triple-doubles")
        else:
            projections_dict[name] = triple_doubles[name] * scoring_multiplier_dict.get("triple-doubles")

    return projections_dict
