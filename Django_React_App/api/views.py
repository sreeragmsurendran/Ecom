
import json
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions

from .models import Note
# Create your views here.
from .serializers import NoteSerializer

@api_view(['GET'])
def getRoutes(request):

        routes = [
            {
                'Endpoint': '/notes/',
                'method': 'GET',
                'body': None,
                'description': 'Returns an array of notes'
            },
            {
                'Endpoint': '/notes/id',
                'method': 'GET',
                'body': None,
                'description': 'Returns a single note object'
            },
            {
                'Endpoint': '/notes/create/',
                'method': 'POST',
                'body': {'body': ""},
                'description': 'Creates new note with data sent in post request'
            },
            {
                'Endpoint': '/notes/id/update/',
                'method': 'PUT',
                'body': {'body': ""},
                'description': 'Creates an existing note with data sent in post request'
            },
            {
                'Endpoint': '/notes/id/delete/',
                'method': 'DELETE',
                'body': None,
                'description': 'Deletes and exiting note'
            },
            ]

        return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes=Note.objects.all()

    serializer=NoteSerializer(notes,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request,pk):
   
    notes=Note.objects.get(id=pk)
    serializer=NoteSerializer(notes,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def update(request,pk):
    data= request.data
    note= Note.objects.get(id=pk)
    serializer= NoteSerializer(instance= note,data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request,pk):
    data= request.data
    note= Note.objects.get(id=pk)
    note.delete()
    return Response('Note is Deleted')

@api_view(['POST'])
def create(request):
    data= request.data
    note=Note.objects.create(
      body=""
    )
    serializer= NoteSerializer(note,many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getLastObject(request):
    note=Note.objects.last()

    serializer=NoteSerializer(note,many=False)
    return Response(serializer.data)