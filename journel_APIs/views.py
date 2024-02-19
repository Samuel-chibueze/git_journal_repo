from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import PublishingHouse,journel_model,Publisher_model,Authors
from .serializers import JournalSerializer,AuthorsSerializer,PublishingHouseSerializer,PublishingModelSerializer
# Create your views here.

    

# journel view 
    
class Journel(APIView):
    # this gets all the journals from the database 
    def get(self,request):
        journal = journel_model.objects.all()
        journalserializer = JournalSerializer(instance=journal, many=True)
        if journalserializer is not None:
            return Response(journalserializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"mesage":"journal empty"}, status=status.HTTP_400_BAD_REQUEST)
    
    # this is a post method to input or add journals to the database 




    # def get(self,request,pk):
    #     try:
    #         instance= journel_model.objects.get(pk=pk)
    #     except journel_model.DoesNotExist:
    #         return Response({"message":"user not found"},status=status.HTTP_400_BAD_REQUEST)
        
    #     serializer = JournalSerializer(instance, partial=True)
    #     if serializer:
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# this apiview is to create new journals into the database 
    def post(self, request):
        data= request.data
        serilaizer= JournalSerializer(data=data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serilaizer.errors, status=status.HTTP_401_UNAUTHORIZED)
        



    # updating the journel instance
    def put(seld,request, pk):
        try:
            instance = journel_model.objects.get(pk=pk)
        except journel_model.DoesNotExist:
            return Response({"message": " the user is not found "}, status=status.HTTP_401_UNAUTHORIZED) 
        serializer =  JournalSerializer(instance, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



        #delete user from the database  
    def delete(self,request, pk):
        try:
            instance = journel_model.objects.get(pk=pk)
        except journel_model.DoesNotExist:
            return Response({"message": " the journal is not found "}, status=status.HTTP_400_BAD_REQUEST)

        instance.delete()
        return Response({"message":"journal has been deleted"}, status=status.HTTP_200_OK)
        
        


# publisher views
class PublishersList(APIView):
       # this gets all the publishers from the database 
    
    def get(self,request):
        publishers =Publisher_model.objects.all()
        serializer = PublishingModelSerializer(instance=publishers, many=True)
        if serializer is not None:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"mesage":"journal empty"}, status=status.HTTP_400_BAD_REQUEST)
    
    # this is a post method to input or add journals to the database 



    # def get(self,request,pk):
    #     try:
    #         instance= journel_model.objects.get(pk=pk)
    #     except journel_model.DoesNotExist:
    #         return Response({"message":"user not found"},status=status.HTTP_400_BAD_REQUEST)
        
    #     serializer = JournalSerializer(instance, partial=True)
    #     if serializer:
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# this apiview is to create new journals into the database 
    def post(self, request):
        data= request.data
        serilaizer= PublishingModelSerializer(data=data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serilaizer.errors, status=status.HTTP_401_UNAUTHORIZED)
        



    # updating the publisher model instance
    def put(seld,request, pk):
        try:
            instance = Publisher_model.objects.get(pk=pk)
        except Publisher_model.DoesNotExist:
            return Response({"message": " the user is not found "}, status=status.HTTP_401_UNAUTHORIZED) 
        serializer =  PublishingModelSerializer(instance, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



        #delete user from the database  
    def delete(self,request, pk):
        try:
            instance = Publisher_model.objects.get(pk=pk)
        except Publisher_model.DoesNotExist:
            return Response({"message": " the user is not found "}, status=status.HTTP_400_BAD_REQUEST)

        instance.delete()
        return Response({"message":"user has been deleted"}, status=status.HTTP_200_OK)
        