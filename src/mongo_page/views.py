from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from bson.objectid import ObjectId
import json

from nosql_wiki.utils.mongodb_client import getDatabase

class MongoPage(APIView):
    def get(self, request):
        try:
            db = getDatabase()
            collection = db["page"]
            pages = collection.find({})
            data = []
            for page in pages:
                data.append({
                    "id": str(page.get('_id')),
                    "title": page.get('title'),
                    "content": page.get('content'),
                    "tags": page.get('tags'),
                })
        except Exception as e:
            return Response(data={"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            db = getDatabase()
            collection = db['page']
            data = json.loads(request.body.decode('utf-8'))
            id = collection.insert_one(data).inserted_id
            page = collection.find_one({"_id":ObjectId(id)})
            data = {
                "id": str(page.get('_id')),
                "title": page.get('title'),
                "content": page.get('content'),
                "tags": page.get('tags'),
            }
        except Exception as e:
            return Response(data={"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_201_CREATED)

class MongoPageDetail(APIView):
    def get(self, request, id):
        try:
            db = getDatabase()
            collection = db["page"]
            params = {}
            if id:
                params["_id"] = ObjectId(id)
            page = collection.find_one(params)
            data = {}
            if page is not None:
                data = {
                    "id": str(page.get('_id')),
                    "title": page.get('title'),
                    "content": page.get('content'),
                    "tags": page.get('tags'),
                }
        except Exception as e:
            return Response(data={"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        try:
            db = getDatabase()
            collection = db["page"]
            data = json.loads(request.body.decode('utf-8'))
            params = {}
            if id:
                params["_id"] = ObjectId(id)
            collection.update_one(params, { "$set": data })
            page = collection.find_one(params)
            data = {}
            if page is not None:
                data = {
                    "id": str(page.get('_id')),
                    "title": page.get('title'),
                    "content": page.get('content'),
                    "tags": page.get('tags'),
                }
        except Exception as e:
            return Response(data={"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        try:
            db = getDatabase()
            collection = db["page"]
            data = json.loads(request.body.decode('utf-8'))
            params = {}
            if id:
                params["_id"] = ObjectId(id)
            collection.delete_one(params)
            data = {"deleted": True}
        except Exception as e:
            return Response(data={"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)