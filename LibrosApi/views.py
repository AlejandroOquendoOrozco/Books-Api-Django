from django.shortcuts import render
from LibrosApi.models import Libro
from LibrosApi.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def books_list(request):
    libros=Libro.objects.all()
    serialize=BookSerializer(libros,many=True)
    return Response(serialize.data)

@api_view(['POST'])
def book_create(request):
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def book(request,pk):
    book=Libro.objects.get(pk)
    if request.method=='GET':
        book=Libro.objects.get(pk)
        serializer=BookSerializer(book)
        return Response(serializer.data)
    
    if request.method=='PUT':
        serializer=BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method=='DELETE':
        book.delete()
        return Response({
            'delete':True
        })