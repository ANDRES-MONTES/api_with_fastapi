import jwt
def create_token(data:dict):
    token:str = jwt.encode(payload=data, key ='my_secret_key', algorithm='HS256')
    return token
    
    
#val = create_token({'mensaje': 'sere el mejor'})


def decode_string(info:str):
    token: dict = jwt.decode(info, key ='my_secret_key',  algorithms=['HS256'])
    print(token)
    return token
    
#decode_string(val)