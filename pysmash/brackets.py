from pysmash import api, utils, exceptions

BRACKET_URL = '/phase_group/'
VALID_BRACKET_PARAMS = ['sets', 'entrants']


def players(bracket_id, filter_response=True):
    uri = BRACKET_URL + str(bracket_id)

    response = api.get(uri, VALID_BRACKET_PARAMS)

    if filter_response:
        response = _filter_player_response(response)

    return response


def sets(bracket_id, filter_response=True, filter_completed=False, filter_current=True, filter_future=True):
    uri = BRACKET_URL + str(bracket_id)

    response = api.get(uri, VALID_BRACKET_PARAMS)

    if filter_response:
        response = _filter_set_response(response, filter_completed, filter_current, filter_future)

    return response


def sets_played_by_player(bracket_id, tag, filter_completed=False, filter_current=True, filter_future=True):
    try:
        tag = str(tag)
        tag = tag.lower()
    except:
        msg = "Given player tag is not and cannot be converted into a string"
        raise exceptions.ValidationError(msg)

    uri = BRACKET_URL + str(bracket_id)

    response = api.get(uri, VALID_BRACKET_PARAMS)
    return _filter_sets_given_player(response, tag, filter_completed, filter_current, filter_future)


def _filter_sets_given_player(response, tag, filter_completed=False, filter_current=True, filter_future=True):

    result_player = None
    players = _filter_player_response(response)
    for p in players:
        if p['tag'].lower() == tag:
            result_player = p

    if result_player is None:
        return []

    player_sets = []
    sets = _filter_set_response(response, filter_completed, filter_current, filter_future)

    # grab sets the player was involved in
    for _set in sets:
        player_is_entrant1 = str(result_player['entrant_id']) == _set['entrant_1_id']
        player_is_entrant2 = str(result_player['entrant_id']) == _set['entrant_2_id']
        if player_is_entrant1 or player_is_entrant2:
            _set['player_id'] = result_player['entrant_id']
            if player_is_entrant1 and not _set['entrant_2_id'] == 'None':
                _set['opponent_id'] = int(_set['entrant_2_id'])
            elif player_is_entrant2 and not _set['entrant_1_id'] == 'None':
                _set['opponent_id'] = int(_set['entrant_1_id'])
            else:
                _set['opponent_id'] = str(None)
            player_sets.append(_set)

    # grab information about player's opponents
    for item in player_sets:
        for opponent in players:
            if item['opponent_id'] == opponent['entrant_id']:
                item['opponent_info'] = opponent

    return {
        'player': result_player,
        'sets': player_sets
    }


def _filter_player_response(response):
    players = []
    entrants = response['entities']['entrants']

    for entrant in entrants:
        player = _get_player_from_entrant(entrant)
        players.append(player)

    return players


def _filter_set_response(response, filter_completed=False, filter_current=True, filter_future=True):
    entities = response.get('entities', None)

    if entities is None:
        return []

    bracket_sets = response['entities'].get('sets', None)
    if bracket_sets is None:
        return []

    groups = entities.get('groups', None)
    if groups is None:
        return []
    is_final_bracket = _is_final_bracket(groups)

    results_sets = []
    for bracket_set in bracket_sets:
        # don't return `projected` brackets
        if 'preview' in str((bracket_set['id'])):
            break

        _set, success = _get_set_from_bracket(bracket_set, is_final_bracket, filter_completed, filter_current, filter_future)
        if success:
            results_sets.append(_set)

    return results_sets


def _is_final_bracket(groups):
    is_final_bracket = False
    w_id = groups.get('winnersTargetPhaseId', None)
    if w_id == 'None' or w_id is None:
        is_final_bracket = True
    return is_final_bracket

#3 endpoints - completed sets, current sets, and future sets. We never want unreachable sets.
def _get_set_from_bracket(bracket_set, is_final_bracket, filter_completed=False, filter_current=True, filter_future=True):
    # ignore unreachable sets
    if bracket_set['unreachable'] is True:
        return None, False

    # filter completed means we do not want already completed sets
    if filter_completed:
        if not bracket_set['winnerId'] is None and not bracket_set['loserId'] is None:
            return None, False

    # filter future means we do not want sets that are not ready or completed - we do not want sets whose participants are not established
    if filter_future:
        if bracket_set['entrant1Id'] is None or bracket_set['entrant2Id'] is None:
            return None, False

    # filter current means we do not want sets that have yet to be played and that have its participants established
    # a set is current if both entrants are set but there is no winner
    if filter_current:
        if not bracket_set['entrant1Id'] is None and not bracket_set['entrant2Id'] is None and bracket_set['winnerId'] is None:
            return None, False

    _set = {
        'id': str(bracket_set['id']),  # make all IDS ints?
        'entrant_1_id': str(bracket_set['entrant1Id']),
        'entrant_2_id': str(bracket_set['entrant2Id']),
        'entrant_1_score': bracket_set['entrant1Score'],
        'entrant_2_score': bracket_set['entrant2Score'],
        'winner_id': str(bracket_set['winnerId']),
        'loser_id': str(bracket_set['loserId']),
        'full_round_text': bracket_set['fullRoundText'] if is_final_bracket else 'pools',
        'medium_round_text': bracket_set['midRoundText'] if is_final_bracket else 'pools',
        'short_round_text': bracket_set['shortRoundText'] if is_final_bracket else 'pools',
        'bracket_id': str(bracket_set['phaseGroupId'])
    }
    return _set, True


def _get_player_from_entrant(entrant):
    participant_id = str(entrant['participantIds'][0])
    player_id = str(entrant['playerIds'][participant_id])
    player_dict = entrant['mutations']['players'][player_id]

    player_name = player_dict.get('name', '')
    if player_name is None:  # Clowns at Smashgg.
        player_name = ''

    player_name_parts = utils.strip_and_split_string(
        player_name, strip_char=" ", split_char=" ")

    fname = player_name_parts[0]

    if len(player_name_parts) > 1:
        lname = player_name_parts[1]
    else:
        lname = ''

    return {
        'entrant_id': entrant['id'],
        'tag': player_dict['gamerTag'],
        'fname': fname,
        'lname': lname,
        'state': player_dict['state'],
        'country': player_dict['country'],
        'final_placement': entrant['finalPlacement'],
        'seed': entrant['initialSeedNum']
    }
