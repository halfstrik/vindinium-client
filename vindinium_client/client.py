import argparse

import requests

from turn_processor import process_turn, GameFinished

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['training', 'arena'], required=True)
    parser.add_argument('--key', required=True)
    parser.add_argument('--map', choices=['m1', 'm2', 'm3', 'm4', 'm5', 'm6'])
    parser.add_argument('--turns', type=int, choices=range(1, 5000), metavar='{1..5000}')
    args = parser.parse_args()

    payload = {'key': args.key}
    if args.mode == 'training':
        url = 'http://vindinium.org/api/training'
        if args.map:
            payload['map'] = args.map
        if args.turns:
            payload['turns'] = args.turns
    else:
        url = 'http://vindinium.org/api/arena'

    response = requests.post(url, data=payload, timeout=30)

    while True:
        try:
            play_url, direction = process_turn(response)
            response = requests.post(play_url, data={'dir': direction}, timeout=10)
        except GameFinished:
            break
