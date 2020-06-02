import jwt

def create_token(data, secret):
    token = jwt.encode(data, secret, algorithm = 'HS256')

    return token

def verify_signature(token):
    secret = 'acelera'
    data = {'language': 'Python'}

    real_token = create_token(data, secret)

    if real_token == token:
        decoded = jwt.decode(token, secret, algorithms='HS256')
        return decoded
    else:
        return {'error':2}

