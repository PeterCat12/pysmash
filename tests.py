import unittest
from pysmash import SmashGG
from pysmash.brackets import _filter_set_response
from pysmash.exceptions import ValidationError


class BaseTestClass(unittest.TestCase):

    smash = SmashGG()

    def empty(self, dictionary, _key):
        if _key in dictionary:
            if dictionary[_key]:
                return False
            return True

    def key_in_dict(self, dictionary, _key):
        if _key in dictionary:
            return True
        return False


class TournamentMethods(BaseTestClass):
    """Only thing we can reliably test is that the contract remains consistent"""

    tournament_show_keys_smash_4 = [
        'details', 'venue_addresss', 'tournament_full_source_url',
        'tournament_id', 'name', 'state_short', 'venue_name', 'links'
    ]

    tournament_show_with_bracket_keys_smash_4 = [
        'details', 'venue_addresss', 'tournament_full_source_url',
        'tournament_id', 'name', 'state_short', 'venue_name', 'bracket_ids',
        'event_name', 'links', 'bracket_full_source_url'
    ]

    tournament_show_event_brackets_keys_smash_4 = [
        'event_name', 'bracket_ids', 'bracket_full_source_url'
    ]

    tournament_show_player_sets_keys_smash_4 = [
        'player', 'sets'
    ]

    def test_tournament_show(self):
        result = self.smash.tournament_show('hidden-bosses-4-0')
        self.assertTrue(len(result) == len(self.tournament_show_keys_smash_4))
        for _key in self.tournament_show_keys_smash_4:
            self.assertTrue(self.key_in_dict(result, _key))

    def test_tournament_show_with_brackets_no_event_specified(self):
        with self.assertRaises(ValidationError) as context:
            self.smash.tournament_show_with_brackets('hidden-bosses-4-0')
        self.assertTrue(
            "You must specify an event name to show sets for a tournament" in str(context.exception)
        )

    def test_tournament_show_with_brackets(self):
        result = self.smash.tournament_show_with_brackets('hidden-bosses-4-0', 'wii-u-singles')
        self.assertTrue(len(result) == len(self.tournament_show_with_bracket_keys_smash_4))
        for _key in self.tournament_show_with_bracket_keys_smash_4:
            self.assertTrue(self.key_in_dict(result, _key))

        # test another event, different tournament...
        result = self.smash.tournament_show_with_brackets('kombat-cup-week-4', 'mkxl')
        self.assertTrue(len(result) == len(self.tournament_show_with_bracket_keys_smash_4))
        for _key in self.tournament_show_with_bracket_keys_smash_4:
            self.assertTrue(self.key_in_dict(result, _key))

        # test with default event name set
        self.smash.set_default_event('wii-u-singles')
        result = self.smash.tournament_show_with_brackets('hidden-bosses-4-0')
        self.assertTrue(len(result) == len(self.tournament_show_with_bracket_keys_smash_4))
        for _key in self.tournament_show_with_bracket_keys_smash_4:
            self.assertTrue(self.key_in_dict(result, _key))

    def test_tournament_show_sets(self):
        result = self.smash.tournament_show_sets('hidden-bosses-4-0', 'wii-u-singles')
        self.assertTrue(len(result) == 423)

        self.smash.set_default_event('wii-u-singles')
        result = self.smash.tournament_show_sets('hidden-bosses-4-0')
        self.assertTrue(len(result) == 423)


    def test_tournamaent_show_sets_other_events(self):
        result = self.smash.tournament_show_sets(tournament_name='kombat-cup-week-4',
                                                 event='mkxl')
        self.assertTrue(len(result) == 255)
        result = self.smash.tournament_show_sets(tournament_name='hidden-bosses-4-0',
                                                 event='wii-u-doubles')
        self.assertTrue(len(result) == 95)

    def test_tournament_show_players(self):
        result = self.smash.tournament_show_players('hidden-bosses-4-0')
        self.assertTrue(len(result) == 123)

    def test_tournament_show_event_brackets(self):
        result = self.smash.tournament_show_event_brackets('hidden-bosses-4-0')
        for _key in self.tournament_show_event_brackets_keys_smash_4:
            self.assertFalse(self.empty(result, _key))
        self.assertTrue(len(result['bracket_ids']), 10)

    def test_tournament_show_player_sets(self):
        result = self.smash.tournament_show_player_sets('hidden-bosses-4-0', 'DOM')
        for _key in self.tournament_show_player_sets_keys_smash_4:
            self.assertFalse(self.empty(result, _key))

    def test_bracket_show_players(self):
        result = self.smash.bracket_show_players(225024)
        self.assertTrue(len(result) == 32)

    def test_bracket_show_sets(self):
        result = self.smash.bracket_show_sets(225024)
        self.assertTrue(len(result) == 47)

    def test_tournament_show_events(self):
        result = self.smash.tournament_show_events('hidden-bosses-4-0')
        self.assertTrue('wii-u-singles' in result['events'])
        self.assertTrue('wii-u-doubles' in result['events'])

    def test_tournament_show_with_event_param(self):
        result = self.smash.tournament_show('hidden-bosses-4-0', ['event'])
        self.assertTrue('wii-u-singles' in result['events'])
        self.assertTrue('wii-u-doubles' in result['events'])

    def test_tournament_show_with_phase_param(self):
        result = self.smash.tournament_show('hidden-bosses-4-0', ['phase'])
        self.assertTrue(len(result['phases']) == 4)

    def test_tournament_show_with_groups_param(self):
        result = self.smash.tournament_show('hidden-bosses-4-0', ['groups'])
        self.assertTrue(len(result['groups']) == 11)

    def test_tournament_show_with_3_params(self):
        result = self.smash.tournament_show('hidden-bosses-4-0', ['phase', 'event', 'groups'])
        self.assertTrue(len(result['phases']) == 4)
        self.assertTrue('wii-u-singles' in result['events'])
        self.assertTrue('wii-u-doubles' in result['events'])
        self.assertTrue(len(result['groups']) == 11)


class SetMethods(BaseTestClass):

    def test_not_sets_in_response(self):

        empty_response = {
            "entities": {
                "groups": {
                    "id": 273024,
                    "phaseId": 87578,
                    }
            }
        }

        # test empty winnersTargetPhaseId
        result = _filter_set_response(empty_response)
        self.assertTrue(len(result) == 0)

        # test empty 'sets' in entities
        empty_response['entities']['groups']['winnersTargetPhaseId'] = 1
        result = _filter_set_response(empty_response)
        self.assertTrue(len(result) == 0)


if __name__ == '__main__':
    unittest.main()
