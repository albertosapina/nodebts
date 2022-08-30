from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from bson.objectid import ObjectId
from rest_framework_simplejwt.tokens import RefreshToken
import json, jwt, hashlib

from nodebts.utils.mongodb_client import getDatabase
from nodebts.settings import SECRET_KEY



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class CreateToken(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            body = data = json.loads(request.body.decode('utf-8'))
            email = body["email"]
            password = body["password"]
            if email != "" and password != "":
                db = getDatabase()
                collection = db["user"]  
                data = collection.find_one({
                    "email": email,
                    "password": hashlib.sha256(password.encode('utf-8')).hexdigest()
                })
                if data is not None:
                    user = {
                        "email": data.get("email"),
                        "username": data.get("username")
                    }
                    res = get_tokens_for_user(user)
                    return Response(res, status=status.HTTP_200_OK)
            else:
                res = {"error": "can not authenticate with the given credentials or the account has been deactivated"}
                return Response(res, status=status.HTTP_403_FORBIDDEN)
        except KeyError:
            res = {"error": "please provide a email and a password"}
            return Response(res)
