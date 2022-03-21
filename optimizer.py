import argparse
from pydfs_lineup_optimizer import get_optimizer, Site, Sport, AfterEachExposureStrategy, RandomFantasyPointsStrategy
from parser import MyParser

from strategies.ScrapedProjectedPointsStrategy import ScrapedProjectedPointsStrategy
from strategies.VegasStrategy import VegasStrategy

# makes program easy to run with customizable command line inputs
# Wants to configure: showdown vs classic, input salary file, name of output lineups file,
# name of entries file (for late swap)
# use existing defaults
# TODO: move this into a class (used in multiple places)
parser = MyParser()
args = parser.get_args()
print(args.input)

# figure out contest type from input
# TODO: make this more flexible call later
site = None
if args.type == "classic":
    site = Site.DRAFTKINGS
elif args.type == "showdown" or args.type == "captain":
    site = Site.DRAFTKINGS_CAPTAIN_MODE
elif args.type == "tiers":
    site = Site.DRAFTKINGS_TIERS


optimizer = get_optimizer(site, Sport.BASKETBALL)

# doesn't seem to exclude injured players: may need to create "black list" of players or import player injury info from elsewhere
optimizer.load_players_from_csv(args.sal)

# add randomness
# optimizer.set_fantasy_points_strategy(RandomFantasyPointsStrategy(max_deviation=0.2))  # set random strategy with custom max_deviation

#optimizer.set_fantasy_points_strategy(ScrapedProjectedPointsStrategy())  # set scraped projections
optimizer.set_fantasy_points_strategy(
    VegasStrategy())  # set scraped projections


# optimize lineups and print results
lineups = set(optimizer.optimize(n=4, max_exposure=0.5,
                                 exposure_strategy=AfterEachExposureStrategy))
for lineup in lineups:
    print(lineup)

# export lineups to csv
optimizer.export(args.line)

