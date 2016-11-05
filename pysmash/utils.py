from pysmash import exceptions


def merge_two_dicts(x, y):
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z


def _validate_query_params(params, valid_params, route_type):
    """Validates query params for Smash.gg requests"""
    for param in params:
        if param not in valid_params:
            error_msg = """
                '{0}' is not a valid query param for route of type: {1}.
                Valid types are [{2}].
             """.format(param, route_type, ', '.join(valid_params))
            raise exceptions.ValidationError(error_msg)


def get_subfield(_dict, field, subField):
    """checks to see if a field in a dictionary exists, if it does, `.get` a specified subfield"""
    if _dict[field] is not None:
        return _dict[field].get(subField, '')
    return ''
