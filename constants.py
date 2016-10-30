

# url constants
SMASH_GG_PREFIX = 'https://api.smash.gg'
TOURNAMENT_PREFIX = SMASH_GG_PREFIX + '/tournament/'
BRACKET_URL = '/phase_group/'
EVENT_URL = '/event/'

# param constants
VALID_TOURNAMENT_PARAMS = [
    'event',
    'phase',
    'groups',
    'stations'
]

VALID_BRACKET_PARAMS = ['sets', 'entrants']

VALID_EVENTS = ['wii-u-singles', 'wii-u-doubles']
