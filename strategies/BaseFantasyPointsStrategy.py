from pydfs_lineup_optimizer.player import Player
from pydfs_lineup_optimizer.lineup import Lineup

# duplicated file so we can reference in our custom strategies
class BaseFantasyPointsStrategy:
    def get_player_fantasy_points(self, player: Player) -> float:
        raise NotImplementedError

    def set_previous_lineup(self, lineup: Lineup):
        pass 