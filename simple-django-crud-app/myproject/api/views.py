from rest_framework.decorators import api_view #, #permission_classes  # Ensure permission_classes is imported
# from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import  NoteSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated



@api_view(['POST'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def createNote(request):
    user= request.user
    data = request.data
    serializer = NoteSerializer(data=data)

    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_notes(request):
    """Get all notes."""
    user = request.user 
    notes = Note.objects.filter(user=user)  # Filter notes by the logged-in user
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def note_details(request, pk):
    """Retrieve, update, or delete a specific note."""
    try:
        note = Note.objects.get(id=pk)
    except Note.DoesNotExist:
        return Response({"error": "Note not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        note.delete()
        return Response({"message": "Note deleted successfully."}, status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
def signup(request):
    
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username=request.data['username'])
        token, create = Token.objects.get_or_create(user=user)

        serializer = UserSerializer(user)

        data = {
            "user": serializer.data,
            "token": token.key
        }
        return Response(data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    data = request.data

    authenticate_user = authenticate(username=data['username'],password=data['password'])

    if authenticate_user is not None:
        user = User.objects.get(username=data['username'])
        serializer = UserSerializer(user)

        response_data ={
            'user': serializer.data
        }

        token, created_token = Token.objects.get_or_create(user=user)

        if token:
            response_data['token'] = token.key

        if created_token:
            response_data['token'] = created_token.key

        return Response(response_data, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid Credentials'},status=status.HTTP_400_BAD_REQUEST)
