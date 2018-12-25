from pysmash.v2.support.contants import URI_TOURNAMENT, URI_GROUP, URI_EVENT
from pysmash.api import api
from typing import Dict

# model imports
from pysmash.v2.models.groups import Group
from pysmash.v2.models.tournaments import Tournament
from pysmash.v2.models.events import Event


class Client(object):

    @staticmethod
    def get_tournament(name, params):
        response = api.get(URI_TOURNAMENT + name, params)

        tournament_data = response['entities'].get('tournament')
        tournament_data['expands'] = {expand: response['entities'].get(expand, []) for expand in Tournament.EXPAND_KEYS}

        return Tournament(**tournament_data)

    @staticmethod
    def get_event(event_id, params):
        response = api.get(URI_EVENT + event_id, params)

        event_data = response['entities'].get('event')
        event_data['expands'] = {expand: response['entities'].get(expand, []) for expand in Event.EXPAND_KEYS}

        return Event(**event_data)

    @staticmethod
    def get_event_by_slug(self, slug, params):
        response = api.get(slug, params)

        event_data = response['entities'].get('event')
        event_data['expands'] = {expand: response['entities'].get(expand, []) for expand in Event.EXPAND_KEYS}

        return Event(**event_data)

    @staticmethod
    def get_group(group_id, params):
        response = api.get(URI_GROUP + group_id, params)

        group_data = response['entities'].get('groups')

        group_data['expands'] = {expand: response['entities'].get(expand, []) for expand in Group.EXPAND_KEYS}

        return Group(**group_data)
