# python modules
import ast

# django modules
from django.http import Http404

# rest framework modules
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import generics

# app level modules
from .models import (Providers, ServiceArea)
from .serializer import (
    ProviderSerializer,
    ServiceAreaSerializer,
    QueryParamSerializer)


class ProviderViewSet(viewsets.GenericViewSet):

    queryset = Providers.objects.filter(is_active=True)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProviderSerializer(queryset, many=True)
        res_data = {"results": serializer.data}
        return Response(res_data)

    def create(self, request):
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res_data = {"data": serializer.data}
            return Response(
                res_data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        provider = self.get_object()
        serializer = ProviderSerializer(provider, data=request.data)
        if serializer.is_valid():
            serializer.save()
            res_data = {"data": serializer.data}
            return Response(res_data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        provider = self.get_object()
        serializer = ProviderSerializer(instance=provider)
        res_data = {"data": serializer.data}
        return Response(res_data)

    def delete(self, request, pk=None):
        provider = self.get_object()
        provider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @detail_route(methods=['post', 'get'], url_path="servicearea")
    def servicearea(self, request, pk=None):
        provider = self.get_object()
        if request.method == "GET":
            queryset = ServiceArea.objects.filter(provider_id=str(provider.id))
            serializer = ServiceAreaSerializer(queryset, many=True)
            res_data = {"results": serializer.data}
            return Response(res_data)
        else:
            data = request.data.copy()
            data["provider_id"] = provider.id
            serializer = ServiceAreaSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                res_data = {"data": serializer.data}
                return Response(
                    res_data, status=status.HTTP_201_CREATED)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchApi(generics.ListAPIView):

    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

    def list(self, request):
        query_data = request.query_params.copy()
        points = query_data.getlist("point")
        coordinates = [ast.literal_eval(point) for point in points]
        data = {"polygon": [coordinates]}
        serializer = QueryParamSerializer(data=data)
        if serializer.is_valid():
            queryset = self.get_queryset()
            coordinates = serializer.validated_data["polygon"]
            queryset = queryset.filter(
                polygon__geo_within={"type": "Polygon",
                                     "coordinates": coordinates})
            res_data = {"results": serializer.data}
            return Response(res_data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceAreaApi(generics.RetrieveUpdateDestroyAPIView):

    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

    def get_object(self):
        pk = self.kwargs.get('pk', None)
        try:
            return ServiceArea.objects.get(id=pk)
        except:
            raise Http404
