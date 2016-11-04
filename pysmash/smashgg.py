from pysmash import tournaments, brackets


class SmashGG(object):

    def __init__(self, key="", secret=""):
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

    def tournament_show(self, tournament_name, params=[], filter_response=True):
        """Show tournament information by name"""
        return tournaments.show(tournament_name, params, filter_response)

    def tournament_show_with_brackets(self, tournament_name,
                                      tournament_params=[], event_name='wii-u-singles'):
        """Show tournament information with a list of Bracket Ids by event"""
        return tournaments.show_with_brackets(tournament_name, tournament_params,
                                              event_name)

    def tournament_show_sets(self, tournament_name, tournament_params=[]):
        """Shows a complete list of sets given a tournament name"""
        return tournaments.show_sets(tournament_name, tournament_params)

    def tournament_show_players(self, tournament_name, tournament_params=[]):
        """Shows a complete list of players/entrants given a tournament name """
        return tournaments.show_players(tournament_name, tournament_params)

    def tournament_show_event_brackets(self, tournament_name,
                                       event='wii-u-singles', filter_response=True):
        """Shows brackets given a tournament name"""
        return tournaments.event_brackets(tournament_name, event, filter_response)

    def bracket_show_players(self, bracket_id, filter_response=True):
        """Shows a list of players given a bracket id"""
        return brackets.players(bracket_id, filter_response)

    def bracket_show_sets(self, bracket_id, filter_response=True):
        """Shows a list of sets given a bracket id"""
        return brackets.sets(bracket_id, filter_response)
