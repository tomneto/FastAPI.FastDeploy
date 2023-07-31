from typing import Annotated, Union

from fastapi import HTTPException, Cookie, Request, Header
from api.database import connect
from api.config import app_config
import secrets

# here we can define a mongo uri
db = connect(app_config.mongo_uri)


# it's also a good practice to keep a particular name to each collection to avoid conflicts when using multiple collections at the same time
def access_collection():
    return db.collection('access')


async def get_fingerprint(
    fingerprintHeader: Annotated[str | None, Header(min_length=24, max_length=24)] = None,
    fingerprintCookie: Union[str, None] = Cookie(title='fingerprint', min_length=24, max_length=24, default=None)
):
    # First, check if the fingerprint is present in the cookie
    if fingerprintCookie is not None:
        print('fingerprint found in the cookie: %s' % fingerprintCookie)
        fingerprint = fingerprintCookie

    # If not in the cookie, check if it's in the header
    elif fingerprintHeader is not None:
        print('fingerprint found in the header: %s' % fingerprintHeader)
        fingerprint = fingerprintHeader

    else:
        raise HTTPException(detail='Device fingerprint not recognised. Please contact support.', status_code=401)

    host_fingerprint = fingerprint[0:5]
    result = fingerprint[5:]

    return result



def authorize(request: Request, refresh_token: str = Header(title='refresh-token')):

    valid_token = None

    def compare_tokens():
        if valid_token is not None:
            if valid_token['token_type'] == 'refresh':
                return True
            else:
                return False
        else:
            return False

    valid_refresh_token_condition = {
        'token': refresh_token,
        'token_type': 'refresh'
    }

    valid_token = access_collection().find_one(valid_refresh_token_condition)

    print(f'Receiving request from: {request.client.host}, search condition: {valid_refresh_token_condition}, result: {valid_token}')

    if compare_tokens():
        update_refresh_token_condition = {'_id': valid_token['_id']}
        new_token = str(secrets.token_urlsafe(24))
        access_collection().update_one(update_refresh_token_condition, {'$set': {'token': new_token}}, upsert=True)

        return new_token
    else:
        raise HTTPException(status_code=401, detail='Invalid refresh-token header.')
