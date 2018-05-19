import json

from django.http import JsonResponse, Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from grids.models import Grid
from grids.serializer import GridSerializer

from grids.grid_helper import get_new_grid_after_age

class GridView(APIView):

    def get(self, request, format=None):
        grids = Grid.objects.all()
        serializer = GridSerializer(grids, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GridSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GridDetailView(APIView):

    def get_object(self, pk):
        try:
            return Grid.objects.get(pk=pk)
        except Grid.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        if 'after' in request.GET:
            response = {}
            data = []
            after = request.GET['after']
            ages = after.split(',')
            grid = self.get_object(pk)
            grid_r = grid.data
            grid_l = json.loads(grid_r)
            print(ages)
            for age in ages:
                new_grid = get_new_grid_after_age(grid_l, int(age))
                data.append({
                    'age': age,
                    'grid': new_grid
                })
            response['id'] = grid.id
            response['x'] = grid.x
            response['y'] = grid.y
            response['data'] = data
            return JsonResponse(response, safe=False)
        else:
            grid = self.get_object(pk)
            serializer = GridSerializer(grid)
            return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = GridSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class GridLifeSpanView(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Grid.objects.get(pk=pk)
#         except Grid.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, after, format=None):
#         book = self.get_object(pk)
#         serializer = GridSerializer(book)
#         return Response(serializer.data)






