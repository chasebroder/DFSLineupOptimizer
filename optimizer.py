from pydfs_lineup_optimizer import get_optimizer, Site, Sport

optimizer = get_optimizer(Site.DRAFTKINGS, Sport.BASKETBALL)

optimizer.load_players_from_csv("dk_salaries.csv")

lineups = optimizer.optimize(n=10)
for lineup in lineups:
    print(lineup)