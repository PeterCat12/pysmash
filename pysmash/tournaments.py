from pysmash import api, brackets, utils

TOURNAMENT_PREFIX = 'tournament/'
EVENT_URL = '/event/'

VALID_PARAMS = ['event', 'phase', 'groups', 'stations']


def show(tournament_name, params=[], filter_response=True):
    """Retrieve a single tournament record by `tournament name`"""
    utils._validate_query_params(params=params, valid_params=VALID_PARAMS, route_type='tournament')
    uri = TOURNAMENT_PREFIX + tournament_name

    response = api.get(uri, params)

    if filter_response:
        response = _filter_tournament_response(response, params)

    return response


def show_events(tournament_name):
    """Returns a list of events for a tournament"""
    uri = TOURNAMENT_PREFIX + tournament_name

    response = api.get(uri, ['event'])

    result = {}
    result = _append_events(response, result)
    return result


def show_with_brackets(tournament_name, event, tournament_params=[], ):
    """Returns tournament meta information along with a list of bracketIds for an event"""
    tournament = show(tournament_name, tournament_params)
    brackets = event_brackets(tournament_name, event)

    return utils.merge_two_dicts(tournament, brackets)


def show_sets(tournament_name, event, tournament_params=[]):
    """Returns all sets from a tournament"""
    tournament = show_with_brackets(tournament_name, event, tournament_params)

    results = []
    for bracket_id in tournament['bracket_ids']:
        bracket_sets = brackets.sets(bracket_id)
        for _set in bracket_sets:
            if len(_set) > 0:
                results.append(_set)

    return results


def show_players(tournament_name, event_name, tournament_params=[]):
    """Returns all players from a tournament"""
    tournament = show_with_brackets(tournament_name, tournament_params)

    results = []
    for bracket_id in tournament['bracket_ids']:
        bracket_players = brackets.players(bracket_id)
        for player in bracket_players:
            results.append(player)
    return list({v['tag']: v for v in results}.values())


def show_player_sets(tournament_name, event, player_tag):
    """Returns all players from a tournament"""
    tournament = show_with_brackets(tournament_name, event)

    player = None
    bracket_sets = []

    for bracket_id in tournament['bracket_ids']:
        player_sets = brackets.sets_played_by_player(bracket_id, player_tag)
        if len(player_sets) == 0:
            continue

        if player is None:
            player = player_sets['player']

        _sets = player_sets['sets']
        bracket_sets = bracket_sets + _sets

    return {
        'player': player,
        'sets': bracket_sets
    }


def show_head_to_head(tournament_name, event, player1_tag, player2_tag):
    """Returns sets played between 2 players"""
    player1_sets = show_player_sets(tournament_name, event, player1_tag)
    result_sets = {
        'player': player1_sets['player'],
        'sets': []
    }
    for _set in player1_sets['sets']:
        if _set['opponent_info']['tag'].lower() == player2_tag:
            result_sets['sets'].append(_set)
    return result_sets


def event_brackets(tournament_name, event='wii-u-singles', filter_response=True):
    # first, get the events for the tournament...
    events = show_events(tournament_name)

    """Returns a list of brackets ids for an event"""
    utils._validate_query_params(params=[event], valid_params=events['events'], route_type='event')

    uri = TOURNAMENT_PREFIX + tournament_name + '/event/' + event

    response = api.get(uri, ['groups'])

    if filter_response:
        response = _filter_event_bracket_response(response)

    return response


def _filter_event_bracket_response(response):
    """Filters the Smash.gg response to something more managable"""
    bracket_ids = []
    for bracket in response['entities']['groups']:
        bracket_ids.append(str(bracket['id']))

    return {
        'bracket_ids': bracket_ids,
        'event_name': response['entities']['event']['typeDisplayStr'],
        'bracket_full_source_url': response['entities']['event']['slug']
    }


def _filter_tournament_response(response, params=[]):
    """Filters the Smash.gg response to something more managable"""
    result = {
        'tournament_id': response['entities']['tournament']['id'],
        'venue_name': response['entities']['tournament']['venueName'],
        'venue_address': response['entities']['tournament']['venueAddress'],
        'name': response['entities']['tournament']['name'],
        'tournament_full_source_url': response['entities']['tournament']['slug'],
        'links': response['entities']['tournament']['links'],
        'state_short': response['entities']['tournament']['regionDisplayName'],
        'start_at': response['entities']['tournament']['startAt'],
        'end_at': response['entities']['tournament']['endAt'],
        'details': response['entities']['tournament']['details']
    }

    if 'event' in params:
        result = _append_events(response, result)
    if 'phase' in params:
        result = _append_phases(response, result)
    if 'groups' in params:
        result = _append_groups(response, result)
    return result


def _append_groups(response, result):
    result['groups'] = []
    groups = response['entities'].get('groups', [])
    for group in groups:
        group_dict = {
            "group_id": group['id'],
            'phase_id': group['phaseId'],
            'title': group['title'],
            'winners_target_phase': group['winnersTargetPhaseId'],
        }
        result['groups'].append(group_dict)
    return result


def _append_phases(response, result):
        result['phases'] = []
        phases = response['entities'].get('phase', [])
        for phase in phases:
            phase_dict = {
                "phase_id": phase['id'],
                'event_id': phase['eventId'],
                'phase_name': phase['name'],
                'is_exhibition': phase['isExhibition'],
                'type_id': phase['typeId']
            }
            result['phases'].append(phase_dict)
        return result


def _append_events(response, result):
        result['events'] = []
        events = response['entities'].get('event', [])
        for event in events:
            slug = event['slug']
            slug = slug.split("/")
            result['events'].append(slug[-1])
        return result
