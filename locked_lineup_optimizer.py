from pydfs_lineup_optimizer import AfterEachExposureStrategy, get_optimizer, Site, Sport
from strategies.VegasStrategy import VegasStrategy

# This file is meant to optimize late swaps for lineups that have already been submitted
# The library implementation is buggy, so this should not be used currently

salary_csv = "dk_salaries.csv"
lineup_csv = "DKEntries.csv"

# TODO make site and sport configurable via command line arguments
optimizer = get_optimizer(Site.DRAFTKINGS, Sport.BASKETBALL)

optimizer.load_players_from_csv(salary_csv)
lineups = optimizer.load_lineups_from_csv(lineup_csv)
optimizer.set_fantasy_points_strategy(VegasStrategy()) 
# can we definitely include strategy? is optimizer getting confused and not able to create possibilities,
# particularly with smaller pool of unlocked players? if I see this again, maybe increase max exposure
for lineup in optimizer.optimize_lineups(lineups, max_exposure=0.5, exposure_strategy = AfterEachExposureStrategy):
    print(lineup)

# export lineups to csv
optimizer.export('updated_lineups.csv')
