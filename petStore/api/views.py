from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Basetable,Category,Tags
from .serializers import BasetableSerializer,CategorySerializer,TagsSerializer
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Find pet by ID': '/pet/{petId}',
        'Updates a pet in the store with form data': '/pet/{petId}',
        'Deletes a pet': '/pet/{petId}',
        'Uploads an Image': '/pet/{petId}/uploadImage',
        'Add a new pet to the store': '/pet',
        'Update an existing pet': '/pet',
        'Finds pets by status': '/pet/findByStatus'
    }
    return Response(api_urls)


@api_view(['POST'])
def add_items(request):
    item = ItemSerializer(data = request.data)

    if Pet.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status = status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def pets(request):
    if request.query_params:
        items = Pet.objects.filter(**request.query_params.dict())
    else:
        items = Pet.objects.all()

        # if there is something in items else raise error
    if items:
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
#
# @api_view(['GET'])
# def view_pet(request,pet_id):
#
#     if pet_id:
#         item = get_object_or_404(Pet,pk=pet_id)
#     else:
#         items = Pet.objects.all()
#
#     if item:
#         serializer = ItemSerializer(item,many=False)
#         return Response(serializer.data)
#
# @api_view(['POST'])
# def update_items(request,pk):
#     item = Pet.objects.get(pk=pk)
#     data = ItemSerializer(instance=item,data=request.data)
#
#     if data.is_valid():
#         data.save()
#         return Response(data.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
# @api_view(['DELETE'])
# def delete_items(request,pk):
#     item = get_object_or_404(Pet,pk=pk)
#     item.delete()
#     return Response(status=status.HTTP_202_ACCEPTED)