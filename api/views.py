from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Category, Entry
from api.serializers import CategorySerializer, EntrySerializer


@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        items = Category.objects.order_by('pk')
        serializer = CategorySerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        item = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CategorySerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def entry_list(request):
    if request.method == 'GET':
        items = Entry.objects.order_by('pk')
        serializer = EntrySerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def entry_detail(request, pk):
    try:
        item = Entry.objects.get(pk=pk)
    except Entry.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = EntrySerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EntrySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)
