from pydfs_lineup_optimizer.player import Player
from pydfs_lineup_optimizer.lineup import Lineup

from strategies.BaseFantasyPointsStrategy import BaseFantasyPointsStrategy
from scrapers.numberfirescraper import get_projections

# uses numberfire scraper to get projections and use them in the strategy
class ScrapedProjectedPointsStrategy(BaseFantasyPointsStrategy):
    def __init__(self):
        self.projected_player_dict = get_projections()

    def get_player_fantasy_points(self, player: Player) -> float:
        # use projections if available, else use fppg
        if player.full_name in self.projected_player_dict:
            return self.projected_player_dict[player.full_name]
        else:
            return 0

    def set_previous_lineup(self, lineup: Lineup):
        pass