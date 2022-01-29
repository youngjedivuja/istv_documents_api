from base64 import b64decode

from rest_framework_simplejwt.authentication import JWTAuthentication
import jwt

jwt_authenticator = JWTAuthentication()
SECRET_KEY = "BqM9xDCMhed8A9ibORR3i5Nk2V0Qo4ryljDxDwupw3hnA92ZWRKDyXSPapRcl3pfy"

jwt_options = {
        'verify_signature': False,
        'verify_exp': True,
        'verify_nbf': False,
        'verify_iat': True,
        'verify_aud': False
    }


def auth(request):
    token = request.headers['Authorization']
    return jwt.decode(token, SECRET_KEY, "HS256", jwt_options)['sub']
