import argparse
import json

from decision_making import make_decision

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', required=True)
    parser.add_argument('--turn', required=True, type=int)

    args = parser.parse_args()
    key = args.key
    turn = args.turn

    with open('../recorded_games/' + key + '/' + str(turn) + '.json', 'r') as f:
        file_content = f.read()

    response_json = json.loads(file_content)
    print(key, turn, make_decision(response_json))
