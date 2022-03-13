from pydfs_lineup_optimizer import get_optimizer, Site, Sport
from strategies.VegasStrategy import VegasStrategy

salary_csv = "dk_salaries.csv"
lineup_csv = "DKEntries.csv"

# TODO make site and sport configurable via command line arguments
optimizer = get_optimizer(Site.DRAFTKINGS, Sport.BASKETBALL)

optimizer.load_players_from_csv(salary_csv)
lineups = optimizer.load_lineups_from_csv(lineup_csv)
optimizer.set_fantasy_points_strategy(VegasStrategy()) 
for lineup in optimizer.optimize_lineups(lineups):
    print(lineup)

# export lineups to csv
optimizer.export('updated_lineups.csv')
