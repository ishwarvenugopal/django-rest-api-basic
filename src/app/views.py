from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class SampleProtectedView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self,request):
        return Response({"message":"This is a sample endpoint behind token authentication"})