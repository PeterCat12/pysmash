from pysmash import api, utils

BRACKET_URL = '/phase_group/'
VALID_BRACKET_PARAMS = ['sets', 'entrants']


def players(bracket_id, filter_response=True):
    uri = BRACKET_URL + str(bracket_id)

    response = api.get(uri, VALID_BRACKET_PARAMS)

    if filter_response:
        response = _filter_player_response(response)

    return response


def sets(bracket_id, filter_response=True):
    uri = BRACKET_URL + str(bracket_id)

    response = api.get(uri, VALID_BRACKET_PARAMS)

    if filter_response:
        response = _filter_set_response(response)

    return response


def _filter_player_response(response):
    players = []
    entrants = response['entities']['entrants']

    for entrant in entrants:
        player = _get_player_from_entrant(entrant)
        players.append(player)

    return players


def _filter_set_response(response):
    results_sets = []
    bracket_sets = response['entities']['sets']

    for bracket_set in bracket_sets:

        # don't return `projected` bracket
        if 'preview' in str((bracket_set['id'])):
            break

        _set = _get_set_from_bracket(bracket_set)
        results_sets.append(_set)

    return results_sets


def _get_set_from_bracket(bracket_set):
    return {
        'id': str(bracket_set['id']),
        'entrant_1_id': str(bracket_set['entrant1Id']),
        'entrant_2_id': str(bracket_set['entrant2Id']),
        'winner_id': str(bracket_set['winnerId']),
        'loser_id': str(bracket_set['loserId']),
        'full_round_text': bracket_set['fullRoundText'],
        'medium_round_text': bracket_set['midRoundText'],
        'short_round_text': bracket_set['shortRoundText'],
        'bracket_id': str(bracket_set['phaseGroupId'])
    }


def _get_player_from_entrant(entrant):
    participant_id = str(entrant['participantIds'][0])
    player_id = str(entrant['playerIds'][participant_id])
    player_dict = entrant['mutations']['players'][player_id]
    participant_dict = entrant['mutations']['participants'][participant_id]

    return {
        'entrant_id': entrant['id'],
        'tag': player_dict['gamerTag'],
        'fname': utils.get_subfield(participant_dict, 'contactInfo', 'nameFirst'),
        'lname': utils.get_subfield(participant_dict, 'contactInfo', 'nameLast'),
        'state': player_dict['state'],
        'country': player_dict['country'],
        'final_placement': entrant['finalPlacement'],
        'seed': entrant['initialSeedNum']
    }
