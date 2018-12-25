from pysmash.v2.models.base.smashgg_objects import SmashGGObject
from pysmash.v2.models.participants import Participant
from pysmash.v2.models.players import Player


class Entrant(SmashGGObject):

    def __init__(self, **kwargs):
        SmashGGObject.__init__(self, **kwargs)
        self.id = kwargs.get('id')
        self.eventId = kwargs.get('eventId')
        self.name = kwargs.get('name')
        self.finalPlacement = kwargs.get('finalPlacement')

        mutations = self.data.get('mutations', {})
        for entity_key, entity_data in mutations.items():
            if entity_key == 'participants':
                self.participants = [
                    Participant(**participant_data) for participant_id, participant_data in entity_data.items()
                ]
            elif entity_key == 'players':
                self.players = [
                    Player(**player_data) for player_id, player_data in entity_data.items()
                ]
