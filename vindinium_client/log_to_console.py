def log_turn_to_console(response_json):
    if response_json['game']['turn'] == 0:
        print(response_json['viewUrl'])

    print('Turn {turn} of {max_turns}'.format(turn=response_json['game']['turn'],
                                              max_turns=response_json['game']['maxTurns']))

    if response_json['game']['finished'] is True:
        print('Game finished')
