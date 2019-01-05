class SmashGGObject(object):

    def __init__(self, **raw):
        self.data = raw

    def raw(self):
        return self.data

    @staticmethod
    def _format_expands(params):
        if isinstance(params, str):
            params = params.split(',')
        if isinstance(params, list):
            return {'expand[]': params}
        return params

    def _set_expands(self, expands, data):
        expand_key = 'entities'
        if 'expands' in data.keys():
            expand_key = 'expands'

        # Grab the expand data from smashgg and set it to the object
        from pysmash.v2.support.factories import SmashGGObjectFactory
        for expand in expands:
            result = [
                SmashGGObjectFactory.factory(expand, **expand_data) for expand_data
                in data.get(expand_key, {}).get(expand, [])
            ]
            setattr(self, expand, result)
