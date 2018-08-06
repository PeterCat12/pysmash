from pysmash.v2.support.contants import URI_TOURNAMENT, URI_GROUP, URI_EVENT
from pysmash.api import api

# model imports
from pysmash.v2.models.groups import Group
from pysmash.v2.models.tournaments import Tournament
from pysmash.v2.models.events import Event


class Client(object):

    def __init__(self, default_event='', key='', secret=''):
        self.event = default_event
        self.credentials = {
            "api_key": key,
            "api_secret": secret
        }

    def get_tournament(self, name, expands):
        response = api.get(URI_TOURNAMENT + name, expands)

        tournament_data = response['entities'].get('tournament')
        tournament_data['expands'] = {expand: response['entities'].get(expand, []) for expand in Tournament.EXPAND_KEYS}

        return Tournament(**tournament_data)

    def get_event(self, event_id, expands):
        response = api.get(URI_EVENT + event_id, expands)

        event_data = response['entities'].get('event')
        event_data['expands'] = {expand: response['entities'].get(expand, []) for expand in Event.EXPAND_KEYS}

        return Event(**event_data)

    def get_event_by_slug(self, slug, expands):
        response = api.get(slug, expands)

        event_data = response['entities'].get('event')
        event_data['expands'] = {expand: response['entities'].get(expand, []) for expand in Event.EXPAND_KEYS}

        return Event(**event_data)

    def get_group(self, group_id, expands):
        response = api.get(URI_GROUP + group_id, expands)

        group_data = response['entities'].get('groups')

        group_data['expands'] = {expand: response['entities'].get(expand, []) for expand in Group.EXPAND_KEYS}

        return Group(**group_data)