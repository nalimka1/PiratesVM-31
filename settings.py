SETTINGS = {
    'DB': {
        'NAME': 'vm31-db',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'USER': 'vm31-user',
        'PASS': '12345678',
    },
    'CHAT': {
        'ECHO_DISTANCE': '10'
    },
    'MEDIATOR': {
        'EVENTS': {
            'INSERT_USER': 'INSERT_USER',
            'ADD_USER_ONLINE': 'ADD_USER_ONLINE',
            'DELETE_USER_ONLINE': 'DELETE_USER_ONLINE',
            'UPDATE_TOKEN_BY_LOGIN': 'UPDATE_TOKEN_BY_LOGIN',
            'LOGOUT': 'LOGOUT'
        },
        'TRIGGERS': {
            'GET_ALL_USERS': 'GET_ALL_USERS',
            'GET_USER_BY_ID': 'GET_USER_BY_ID',
            'GET_USER_BY_TOKEN': 'GET_USER_BY_TOKEN',
            'GET_USER_BY_LOGIN': 'GET_USER_BY_LOGIN',
            'GET_HASH_BY_LOGIN': 'GET_HASH_BY_LOGIN',
            'COUNT_DISTANCE': 'COUNT_DISTANCE'
        }
    }
}
