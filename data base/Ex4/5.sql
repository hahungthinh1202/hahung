select goal.name, game.screen_name
from goal left join goal_reached on goal.id = goal_reached.goal_id
    left join game on game.id = goal_reached.game_id;
