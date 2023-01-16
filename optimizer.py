from pydfs_lineup_optimizer import get_optimizer, Site, Sport, AfterEachExposureStrategy, RandomFantasyPointsStrategy

from strategies.ScrapedProjectedPointsStrategy import ScrapedProjectedPointsStrategy
from strategies.VegasStrategy import VegasStrategy

# TODO make site and sport configurable via command line arguments
optimizer = get_optimizer(Site.DRAFTKINGS, Sport.BASKETBALL)

# doesn't seem to exclude injured players: may need to create "black list" of players or import player injury info from elsewhere
optimizer.load_players_from_csv("DKSalaries.csv")

# add randomness
# optimizer.set_fantasy_points_strategy(RandomFantasyPointsStrategy(max_deviation=0.2))  # set random strategy with custom max_deviation

#optimizer.set_fantasy_points_strategy(ScrapedProjectedPointsStrategy())  # set scraped projections
optimizer.set_fantasy_points_strategy(VegasStrategy())  # set scraped projections


# optimize lineups and print results
lineups = set(optimizer.optimize(n=6, max_exposure=0.5, exposure_strategy = AfterEachExposureStrategy))
for lineup in lineups:
    print(lineup)

# export lineups to csv
optimizer.export('lineups.csv')
