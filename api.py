import requests
# import json
from exceptions import ValidationError, ResponseError
from responseFormater import formatTournamentResponse, formatBracketResponse, formatPlayerResponse
from constants import TOURNAMENT_PREFIX, VALID_TOURNAMENT_PARAMS, VALID_BRACKET_PARAMS, VALID_EVENTS
from utils import merge_two_dicts, get_event_url, get_tournament_url, get_bracket_url


# This library currently only supports Wii-u SINGLES
def get_tournament(name, params=[], formatResponse=True):
    """
    :name s: name of the tournament
    :params l: list of string parameters
    :returns: integer at *index* in *l*
    :rtype: json
    """
    for param in params:
        if param not in VALID_TOURNAMENT_PARAMS:
            error_msg = "'" + param + "'" + ' is not a valid query param for a tournament route. Valid type are [' + ', '.join(VALID_TOURNAMENT_PARAMS) + '].'
            raise ValidationError(error_msg)

    tournament_url = get_tournament_url(name)
    payload = {'expand': params}
    r = requests.get(tournament_url, params=payload)

    data = r.json()
    if r.status_code == 200:
        if formatResponse:
            return formatTournamentResponse(data)
        return data
    raise ResponseError(data['message'], r.status_code)


def get_tournament_brackets(name, event_name='wii-u-singles', formatResponse=True):
    if event_name not in VALID_EVENTS:
        error_msg = event_name + ' is not a valid event. Valid events are [' + ', '.join(VALID_EVENTS) + '].'
        raise ValidationError(error_msg)

    events_url = get_event_url(name, event_name)
    payload = {'expand': ['groups']}

    r = requests.get(events_url, params=payload)

    data = r.json()
    if r.status_code == 200:
        if formatResponse:
            return formatBracketResponse(data)
        return data
    raise ResponseError(data['message'], r.status_code)


def get_tournament_with_brackets(name, tournement_params=[], event_name='wii-u-singles'):
    tournament_meta_data = get_tournament(name, tournement_params)
    brackets = get_tournament_brackets(name, event_name)
    results = merge_two_dicts(tournament_meta_data, brackets)
    return results


def get_players_from_bracket(bracket_id, formatResponse=True):
    bracket_url = get_bracket_url(bracket_id)

    r = requests.get(bracket_url + "?expand[]=entrants&expand[]=sets")
    data = r.json()

    if r.status_code == 200:
        if formatResponse:
            return formatPlayerResponse(data)
        return data
    raise ResponseError(data['message'], r.status_code)


def get_players_for_tournament(tournament_name, tournament_params=[]):
    tournament = get_tournament_with_brackets(tournament_name, tournament_params)

    results = []
    for bracket_id in tournament['bracket_ids']:
        bracket_players = get_players_from_bracket(bracket_id)
        for player in bracket_players:
            results.append(player)
    return list({v['tag']: v for v in results}.values())


def main(name, params):
    # return get_tournament(name, params)
    # result = get_tournament_brackets(name)
    # result = get_tournament_with_brackets(name)
    # result = get_players_from_bracket('224997', ['entrants', 'sets'])
    result = get_players_for_tournament(name)
    print(result)

if __name__ == "__main__":
    name = "hidden-bosses-4-0"
    params = ['groups']
    main(name, params)
