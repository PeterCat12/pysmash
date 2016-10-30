from constants import SMASH_GG_PREFIX, TOURNAMENT_PREFIX, EVENT_URL, BRACKET_URL


# merges two dictionaries together
def merge_two_dicts(x, y):
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z


def get_event_url(name, event_name,  params=[]):
    return TOURNAMENT_PREFIX + name + EVENT_URL + event_name


def get_tournament_url(name,  params=[]):
    return TOURNAMENT_PREFIX + name


def get_bracket_url(bracket_id, params=[]):
    return SMASH_GG_PREFIX + BRACKET_URL + bracket_id


def get_subfield(_dict, field, subField):
    if _dict[field] is not None:
        return _dict[field].get(subField, '')
    return ''

    # if contactInfo is not None:
    #     result['fname'] = contactInfo['nameFirst'],
    #     result['lname'] = contactInfo['nameLast']
    # else:
    #     result['fname'] = '',
    #     result['lname'] = ''
    # return result
