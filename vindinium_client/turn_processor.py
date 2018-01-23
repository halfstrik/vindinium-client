from decision_making import make_decision
from log_to_console import log_turn_to_console
from log_to_file import log_turn_to_file


class GameFinished(Exception):
    pass


def process_turn(response):
    response_json = response.json()

    log_turn_to_file(response_json)

    log_turn_to_console(response_json)

    if response_json['game']['finished'] is True:
        raise GameFinished

    play_url = response_json['playUrl']
    direction = make_decision(response_json)
    return play_url, direction
