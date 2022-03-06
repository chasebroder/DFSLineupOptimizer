from pydfs_lineup_optimizer.player import Player
from pydfs_lineup_optimizer.lineup import Lineup
from typing import Dict

# The purpose of this file is to create custom strategies 

class BaseFantasyPointsStrategy:
    def get_player_fantasy_points(self, player: Player) -> float:
        raise NotImplementedError

    def set_previous_lineup(self, lineup: Lineup):
        pass 

# uses numberfire scraper to get projections and use them in the strategy
class ScrapedProjectedPointsStrategy(BaseFantasyPointsStrategy):
    def __init__(self, projected_player_dict: Dict = {}):
        self.projected_player_dict = projected_player_dict

    def get_player_fantasy_points(self, player: Player) -> float:
        # use projections if available, else use fppg
        if player.full_name in self.projected_player_dict:
            return self.projected_player_dict[player.full_name]
        else:
            return 0

    def set_previous_lineup(self, lineup: Lineup):
        pass