import unittest
from pysmash import SmashGG
from pysmash.brackets import _filter_set_response


class BaseTestClass(unittest.TestCase):

    smash = SmashGG()

    def empty(self, dictionary, _key):
        if _key in dictionary:
            if dictionary[_key]:
                return False
            return True


class TournamentMethods(BaseTestClass):

    tournament_show_keys_smash_4 = [
        'details', 'venue_addresss', 'tournament_full_source_url',
        'tournament_id', 'name', 'state_short', 'venue_name'
    ]

    tournament_show_with_bracket_keys_smash_4 = [
        'details', 'venue_addresss', 'tournament_full_source_url',
        'tournament_id', 'name', 'state_short', 'venue_name', 'bracket_ids',
        'event_name'
    ]

    tournament_show_event_brackets_keys_smash_4 = [
        'event_name', 'bracket_ids', 'bracket_full_source_url'
    ]

    tournament_show_player_sets_keys_smash_4 = [
        'player', 'sets'
    ]

    def test_tournament_show_smash_4(self):
        result = self.smash.tournament_show('hidden-bosses-4-0')
        for _key in self.tournament_show_keys_smash_4:
            self.assertFalse(self.empty(result, _key))

    def test_tournament_show_with_brackets_smash_4(self):
        result = self.smash.tournament_show_with_brackets('hidden-bosses-4-0')
        for _key in self.tournament_show_with_bracket_keys_smash_4:
            self.assertFalse(self.empty(result, _key))

    def test_tournament_show_sets_smash_4(self):
        result = self.smash.tournament_show_sets('hidden-bosses-4-0')
        self.assertTrue(len(result) == 423)

    def test_tournament_show_players_smash_4(self):
        result = self.smash.tournament_show_players('hidden-bosses-4-0')
        self.assertTrue(len(result) == 123)

    def test_tournament_show_event_brackets_smash_4(self):
        result = self.smash.tournament_show_event_brackets('hidden-bosses-4-0')
        for _key in self.tournament_show_event_brackets_keys_smash_4:
            self.assertFalse(self.empty(result, _key))
        self.assertTrue(len(result['bracket_ids']), 10)

    def test_tournament_show_player_sets_smash_4(self):
        result = self.smash.tournament_show_player_sets('hidden-bosses-4-0', 'DOM')
        for _key in self.tournament_show_player_sets_keys_smash_4:
            self.assertFalse(self.empty(result, _key))

    def test_bracket_show_players_smash_4(self):
        result = self.smash.bracket_show_players(225024)
        self.assertTrue(len(result) == 32)

    def test_bracket_show_sets_smash_4(self):
        result = self.smash.bracket_show_sets(225024)
        self.assertTrue(len(result) == 47)


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
