from pysmash.v2.models.base.smashgg_objects import SmashGGObject
from pysmash.v2.models.participants import Participant
from pysmash.v2.models.players import Player
from pysmash.v2.models.entrants import Entrant


class Seed(SmashGGObject):

    def __init__(self, **kwargs):
        SmashGGObject.__init__(**kwargs)
        self.id = kwargs.get('id')
        self.phaseId = kwargs.get('phaseId')
        self.entrantId = kwargs.get('entrantId')
        self.seedNum = kwargs.get('seedNum')
        self.placement = kwargs.get('placement')
        self.losses = kwargs.get('losses')
        self.isFinal = kwargs.get('isFinal')
        self.isSeeded = kwargs.get('isSeeded')
        self.checkInState = kwargs.get('checkInState')
        self.isBye = kwargs.get('isBye')
        self.progressingName = kwargs.get('progressingName')
        self.progressionSeedId = kwargs.get('progressionSeedId')
        self.progressionPhaseId = kwargs.get('progressionPhaseId')
        self.progressionPhaseGroupId = kwargs.get('progressionPhaseGroupId')

        mutations = kwargs.get('mutations', {})
        for entity_key, entity_data in mutations.items():
            if entity_key == 'participants':
                self.participants = [
                    Participant(**participant_data) for participant_id, participant_data in entity_data.items()
                ]
            elif entity_key == 'players':
                self.players = [
                    Player(**player_data) for player_id, player_data in entity_data.items()
                ]
            elif entity_key == 'entrants':
                self.entrants = [
                    Entrant(**entrant_data) for entrant_id, entrant_data in entity_data.items()
                ]
