from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Items
from .serializer import ItemsSerializer


class ItemsList(APIView):
    def get(self, request):
        items = Items.objects.all()
        serializer = ItemsSerializer(items, many=True)
        return Response(serializer.data)


class GetItem(APIView):
    def get(self, request, id):
        item = Items.objects.get(id=id)
        serializer = ItemsSerializer(item)
        return Response(serializer.data)


class CreateItem(APIView):
    def post(self, request):
        data = request.data
        serializer = ItemsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)