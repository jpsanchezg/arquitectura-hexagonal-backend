
from http import HTTPStatus

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from app.aplicacion.domain.model.voting_user import VotingUser
import json

class ArticleView(APIView):

    def post(self, request, id=""):
        jd = json.loads(request.body)
        
        
