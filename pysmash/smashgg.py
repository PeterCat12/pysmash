from pysmash import tournaments, brackets, exceptions


class SmashGG(object):

    def __init__(self, default_event='', key="", secret=""):
        self.event = default_event
        self.credentials = {
            "api_key": key,
            "api_secret": secret
        }

    def set_credentials(self, key, secret):
        """Sets creds for SmashGG (Not yet needed, API still public)"""
        self.credentials['key'] = key
        self.credentials['secret'] = secret

    def get_credentials(self):
        """Returns SmashGG credentials (Not yet needed, API still public)"""
        return self.credentials['key'], self.credentials['secret']

    def set_default_event(self, event):
        self.event = event

    def get_default_event(self):
        return self.event

    # tournament meta data endpoints
    def tournament_show(self, tournament_name, params=[], filter_response=True):
        """Show tournament information by name"""
        return tournaments.show(tournament_name, params, filter_response)

    def tournament_show_with_brackets(self, tournament_name, event='', params=[]):
        """Show tournament information with a list of Bracket Ids by event"""
        event = self._validate_event_name(event)
        return tournaments.show_with_brackets(tournament_name, event, params)

    # general tournament endpoints
    def tournament_show_events(self, tournament_name):
        """Show a list of events belonging to a tournment"""
        return tournaments.show_events(tournament_name)

    def tournament_show_sets(self, tournament_name, event='', params=[]):
        """Shows a complete list of sets given a tournament and event names"""
        event = self._validate_event_name(event)
        return tournaments.show_sets(tournament_name, event, params)

    def tournament_show_players(self, tournament_name, event='', tournament_params=[]):
        """Shows a complete list of players/entrants given a tournament and event name"""
        event = self._validate_event_name(event)
        return tournaments.show_players(tournament_name, tournament_params, event)

    def tournament_show_event_brackets(self, tournament_name, event='', filter_response=True):
        """Shows brackets given a tournament name"""
        event = self._validate_event_name(event)
        return tournaments.event_brackets(tournament_name, event, filter_response)

    def tournament_show_player_sets(self, tournament_name, player_tag, event=''):
        event = self._validate_event_name(event)
        return tournaments.show_player_sets(tournament_name, event, player_tag)

    def tournament_show_head_to_head(self, tournament_name, player1_tag, player2_tag, event=''):
        event = self._validate_event_name(event)
        return tournaments.show_head_to_head(tournament_name, event, player1_tag, player2_tag)

    # bracket endpoints
    def bracket_show_players(self, bracket_id, filter_response=True):
        """Shows a list of players given a bracket id"""
        return brackets.players(bracket_id, filter_response)

    def bracket_show_sets(self, bracket_id, filter_response=True):
        """Shows a list of sets given a bracket id"""
        return brackets.sets(bracket_id, filter_response)

    def _validate_event_name(self, event):
        if event == '' and self.event == '':
            msg = "You must specify an event name to show sets for a tournament"
            raise exceptions.ValidationError(msg)
        if event == '':
            event = self.event
        return event
