from constants import SMASH_GG_PREFIX
from utils import get_subfield

TOURNAMENT_FIELDS = [
    "id",
    "regionDisplayName",
    "venueName",
    "venueAddress",
    "name",
    "slugs",
    "links",
    "details",
]


def formatTournamentResponse(tournament):
    results = {
        'tournament_id': tournament['entities']['tournament']['id'],
        'venue_name': tournament['entities']['tournament']['venueName'],
        'venue_addresss': tournament['entities']['tournament']['venueAddress'],
        'name': tournament['entities']['tournament']['name'],
        'tournament_full_source_url': SMASH_GG_PREFIX + tournament['entities']['tournament']['slug'],
        'links': tournament['entities']['tournament']['links'],
        'state_short': tournament['entities']['tournament']['regionDisplayName']
        # 'details': tournament['entities']['tournament']['details']
    }

    return results


def formatBracketResponse(event):
    results = {
        'event_name': event['entities']['event']['typeDisplayStr'],
        'bracket_full_source_url': SMASH_GG_PREFIX + event['entities']['event']['slug'],
    }

    bracket_ids = []
    for bracket in event['entities']['groups']:
        bracket_ids.append(str(bracket['id']))

    results['bracket_ids'] = bracket_ids
    return results


def formatPlayerResponse(bracket):
    players = []
    entrants = bracket['entities']['entrants']

    for entrant in entrants:
        player = _get_player_from_entrant(entrant)
        players.append(player)

    return players


def _get_player_from_entrant(entrant):
    participant_id = str(entrant['participantIds'][0])
    player_id = str(entrant['playerIds'][participant_id])
    player_dict = entrant['mutations']['players'][player_id]
    participant_dict = entrant['mutations']['participants'][participant_id]

    return {
        'entrant_id': entrant['id'],
        'tag': player_dict['gamerTag'],
        'fname': get_subfield(participant_dict, 'contactInfo', 'nameFirst'),
        'lname': get_subfield(participant_dict, 'contactInfo', 'nameLast'),
        'state': player_dict['state'],
        'country': player_dict['country'],
        'final_placement': entrant['finalPlacement'],
        'seed': entrant['initialSeedNum']
    }
