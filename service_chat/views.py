from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MessageSerializer
from .models import Message

# Create your views here.
'''
class MessageView(APIView):

    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request):

        message = request.data
        print(message)

        serializer = MessageSerializer(data=message)

        if serializer.is_valid(raise_exception=True):
            message_saved = serializer.save()
            return HttpResponse(status=201)


'''


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-created_at')
    serializer_class = MessageSerializer
