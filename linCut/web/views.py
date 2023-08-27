from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from web.models import Link
from web.serilizers import LinkSerializer


"________________________HARD_WAY______________________________"


@csrf_exempt
def Link_list(request):
    """
    List all code Links, or create a new Link.
    """
    if request.method == "GET":
        links = Link.objects.all()
        serializer = LinkSerializer(links, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = LinkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def link_detail(request, pk):
    """
    Retrieve, update or delete a code Link.
    """
    try:
        link = Link.objects.get(pk=pk)
    except Link.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = LinkSerializer(link)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = LinkSerializer(link, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        Link.delete()
        return HttpResponse(status=204)


"________________________EASIER_WAY______________________________"
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LinkList(APIView):
    """
    List all Links, or create a new Link.
    """

    def get(self, request, format=None):
        Links = Link.objects.all()
        serializer = LinkSerializer(Links, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LinkDetail(APIView):
    """
    Retrieve, update or delete a Link instance.
    """

    def get_object(self, pk):
        try:
            return Link.objects.get(pk=pk)
        except Link.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        link = self.get_object(pk)
        serializer = LinkSerializer(link)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        link = self.get_object(pk)
        serializer = LinkSerializer(link, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        link = self.get_object(pk)
        link.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"________________________MIXIN_WAY______________________________"
from web.models import Link
from web.serilizers import LinkSerializer
from rest_framework import mixins
from rest_framework import generics


class Link2List(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class Link2Detail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


"________________________GENERICS_WAY______________________________"
from web.models import Link
from web.serilizers import LinkSerializer
from rest_framework import generics


class Link3List(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class Link3Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


"________________________USER______________________________"
from django.contrib.auth.models import User
from web.serilizers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
