import random


def make_decision(response_json):
    direction = random.choice(['Stay', 'North', 'South', 'East', 'West'])
    return direction
