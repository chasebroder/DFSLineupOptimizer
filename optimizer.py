from pydfs_lineup_optimizer import get_optimizer, Site, Sport, RandomFantasyPointsStrategy

# TODO make site and sport configurable via command line arguments
optimizer = get_optimizer(Site.DRAFTKINGS, Sport.BASKETBALL)

# doesn't seem to exclude injured players: may need to create "black list" of players or import player injury info from elsewhere
optimizer.load_players_from_csv("dk_salaries.csv")

# add randomness
optimizer.set_fantasy_points_strategy(RandomFantasyPointsStrategy(max_deviation=0.2))  # set random strategy with custom max_deviation

# optimize lineups and print results
lineups = set(optimizer.optimize(n=10))
lineups.update(optimizer.optimize(5, exclude_lineups=lineups)) # remove duplicates
for lineup in lineups:
    print(lineup)

# export lineups to csv
optimizer.export('lineups.csv')
