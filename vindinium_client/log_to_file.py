import json

import os


def log_turn_to_file(response_json):
    game = response_json['game']
    game_id = game['id']
    turn = game['turn']

    os.makedirs('../recorded_games/' + game_id, exist_ok=True)
    with open('../recorded_games/' + game_id + '/' + str(turn) + '.json', 'w') as f:
        f.write(json.dumps(response_json, indent=2))
