from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import EventDoesNotExist
from .models import Events, EventCategory
from .renderers import EventJSONRenderer
from .serializers import EventSerializers, EventCategorySerializer
from rest_framework.decorators import api_view, permission_classes, parser_classes

# Create your views here.

class CreateEventsAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    renderer_classes = (EventJSONRenderer,)
    serializer_class = EventSerializers

    def post(self, request):
        event = request.data.get('event', {})
        serializer = self.serializer_class(data=event)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_events_view(request, event_name):
    if request.method == "GET":
        try:
            events = Events.objects.get(event_name=event_name)
            serializer = EventSerializers(events)
            return Response(serializer.data)
        except Events.DoesNotExist:
            return Response({"error":"Event Name doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_events_organization(request, organization_id):
    if request.method == "GET":
        try:
            events = Events.objects.filter(organization=organization_id)
            serializer = EventSerializers(events, many=True)
            return Response(serializer.data)
        except Events.DoesNotExist:
            return Response({"error":"Event Name doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_events_category(request, category_id):
    if request.method == "GET":
        try:
            events = Events.objects.filter(category=category_id)
            serializer = EventSerializers(events, many=True)
            return Response(serializer.data)
        except Events.DoesNotExist:
            return Response({"error":"Event Name doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def all_events(request):
    get_events= Events.objects.all()
    serializers = EventSerializers(get_events, many=True)
    return Response(serializers.data)


@api_view(['PATCH'])
@permission_classes([AllowAny])
def update_event(request, pk):
    if request.method == "PATCH":
        data = request.data
        get_event = Events.objects.filter(pk=pk).first()
        serializer = EventSerializers(get_event, data=data, partial=True)
        if serializer.is_valid():
            #s = serializer.save(commit=True)
            #s.user = request.user
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error":"something wrong with fields"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_event(request, pk):
    if request.method == "DELETE":
        get_event = Events.objects.filter(pk=pk).first()
        get_event.delete()
        return Response({"message":"event deleted successfully"}, status=status.HTTP_204_NO_CONTENT)




@api_view(['POST'])
@permission_classes([AllowAny])
def create_category(request):
    # return Response({"data": get_category})
    if request.method == "POST":
        # print(f"DATAFG: {request.data}")
        data = request.data['category']
        get_category = EventCategory.objects.filter(category_name = data['category_name']).first()
        if get_category:
            return Response({"error":"category already exists"}, status=status.HTTP_400_BAD_REQUEST)
        print(f"DATAVG_PASS: {data}")
        serializer = EventCategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error":"fields not valid"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def all_category(request):
    if request.method == "GET":
        get_category = EventCategory.objects.all()
        if not get_category:
            return Response({"error":"no category"}, status=status.HTTP_200_OK)
        else:
            serializer = EventCategorySerializer(get_category, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_category(request, uid):
    if request.method == "PUT":
        data = request.data
        get_category = EventCategory.objects.filter(category_id=uid).first()
        serializer = EventCategorySerializer(get_category, data=data)
        if serializer.is_valid():
           
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error":"something wrong with fields"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([AllowAny])
def get_category(request, uid):
    if request.method == "GET":
        get_category = EventCategory.objects.filter(category_id=uid).first()
        if not get_category:
            return Response({"message":"category doesn't exist"}, status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = EventCategorySerializer(get_category)
            return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_category(request, uid):
    if request.method == "DELETE":
        get_event = EventCategory.objects.filter(category_id=uid).first()
        get_event.delete()
        return Response({"message":"category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)