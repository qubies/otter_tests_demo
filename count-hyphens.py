OK_FORMAT = True

test = {   'name': 'count-hyphens',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> count_hyphens('Hello-World') == 1\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> count_hyphens('Hello--World') == 2\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> count_hyphens('Hello') == 0\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
