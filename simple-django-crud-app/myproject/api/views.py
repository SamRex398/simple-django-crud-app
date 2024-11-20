from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serilizer import NoteSerializer

@api_view(['POST'])
def createNote(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.error_messages)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def noteDetails(request, pk):
    try:
        note = Note.objects.get(id = pk)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method=='DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.error_messages)


