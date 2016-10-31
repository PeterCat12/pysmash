# from pysmash2 import api, exceptions
import api
import brackets
import utils

TOURNAMENT_PREFIX = '/tournament/'
EVENT_URL = '/event/'

VALID_PARAMS = ['event', 'phase', 'groups', 'stations']
VALID_EVENTS = ['wii-u-singles', 'wii-u-doubles']


def show(tournament_name, params=[], filter_response=True):
    """Retrieve a single tournament record by `tournament name`"""
    utils._validate_query_params(params=params, valid_params=VALID_PARAMS, route_type='tournament')
    uri = TOURNAMENT_PREFIX + tournament_name

    response = api.get(uri, params)

    if filter_response:
        response = _filter_tournament_response(response)

    return response


def show_with_brackets(tournament_name, tournament_params=[], event_name='wii-u-singles'):
    """Returns tournament meta information along with a list of bracketIds for an event"""
    tournament = show(tournament_name, tournament_params)
    brackets = event_brackets(tournament_name, event_name)

    return utils.merge_two_dicts(tournament, brackets)


def show_sets(tournament_name, tournament_params=[]):
    """Returns all sets from a tournament"""
    tournament = show_with_brackets(tournament_name, tournament_params)

    results = []
    for bracket_id in tournament['bracket_ids']:
        bracket_sets = brackets.sets(bracket_id)
        for _set in bracket_sets:
            if len(_set) > 0:
                results.append(_set)

    return results


def show_players(tournament_name, tournament_params=[]):
    """Returns all players from a tournament"""
    tournament = show_with_brackets(tournament_name, tournament_params)

    results = []
    for bracket_id in tournament['bracket_ids']:
        bracket_players = brackets.players(bracket_id)
        for player in bracket_players:
            results.append(player)
    return list({v['tag']: v for v in results}.values())


def event_brackets(tournament_name, event='wii-u-singles', filter_response=True):
    """Returns a list of brackets ids for an event"""
    utils._validate_query_params(params=[event], valid_params=VALID_EVENTS, route_type='event')

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


def _filter_tournament_response(response):
    """Filters the Smash.gg response to something more managable"""
    return {
        'tournament_id': response['entities']['tournament']['id'],
        'venue_name': response['entities']['tournament']['venueName'],
        'venue_addresss': response['entities']['tournament']['venueAddress'],
        'name': response['entities']['tournament']['name'],
        'tournament_full_source_url': response['entities']['tournament']['slug'],
        'links': response['entities']['tournament']['links'],
        'state_short': response['entities']['tournament']['regionDisplayName'],
        'details': response['entities']['tournament']['details']
    }
