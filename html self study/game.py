import action
import basic
import infection
import player


# Set up a new game, include map and player hand.
def game_init(difficulty,num_player):
    basic.set_up_map()
    basic.set_up_player_deck(difficulty, num_player)

def gameLogic(command_1, command_2):
    computerInfo = []
    if command_1 == "gameInit":
        game_init(5,2)
    else:
        current_player, action_point = basic.return_current_player_info()
        move_data  = action.move_check(current_player)
        treat_data = action.treat_check(current_player)
        cure_data = action.cure_check(current_player)
        if command_1 == 'move':
            destination_id = command_2
            action.move_execute(current_player, destination_id, move_data)
        elif command_1 == 'treat':
            action.treat_execute(current_player, int(command_2), treat_data)
        elif command_1 == 'build':
            action.build_execute(current_player)
        elif command_1 == 'cure':
            action.cure_execute(current_player,cure_data,command_2)
        if action_point == 1:
            computerInfo.append(player.draw(current_player))
            computerInfo.append(player.draw(current_player))
            computerInfo += infection.infect()
        basic.update_player_turn(current_player)
        win_lose = basic.check_win()

    return gameData(computerInfo)


def gameData(computerInfo):
    current_player, action_point = basic.return_current_player_info()
    return_data = {
        'action': {
            'move': action.move_check_info(current_player),
            'treat': action.treat_check(current_player),
            'build': action.build_check(current_player),
            'cure': action.cure_check(current_player)
                },
        'player': basic.return_player_coordinate(),
        'city'  : basic.return_all_city_situation(),
        'game'  : basic.return_game_info(),
        'own'   : action.player_own_info(current_player),
        'computerInfo': computerInfo
    }
    return return_data

