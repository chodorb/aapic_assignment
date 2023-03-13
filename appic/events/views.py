from email import message
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from performances.models import Performance
from performances.serializers import PerformanceSerializer

from events.models import Event
from events.serializers import EventSerializer

from events.tasks import export_events


class EventListAPIView(APIView):
    
    def get(self,request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self,request):
        serializer = EventSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
class EventDetailAPIView(APIView):
    
    def get_object(self, pk):
        try:
            return Event.objects.get(pk = pk)
        except Event.DoesNotExist:
            return None
        
    def get(self,request,pk):
        event = self.get_object(pk)
        if event is None:
            return Response({'error':'event not found'}, status = status.HTTP_404_NOT_FOUND)
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        event = self.get_object(pk)
        if event is None:
            return Response({'error':'event not found'}, status = status.HTTP_404_NOT_FOUND)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_200_OK)
        return Response (serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
class EventPerformancesDetailAPIView(APIView):
    def get_object(self,pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return None
    
    def get(self, request, pk):
        event = self.get_object(pk)
        sort_order = request.query_params.get('sort','desc')
        performances = Performance.objects.filter(event_id=pk)
        
        if sort_order == 'asc':
            performances = performances.order_by('start')
        if sort_order == 'desc':
            performances = performances.order_by('-end')
            
        serializer = EventSerializer(event,context={'request':request})
        data = serializer.data
        data['performances'] = PerformanceSerializer(performances, many=True).data
        
        return Response(data,status=status.HTTP_200_OK)
        
class EventExportAPIView(APIView):
    def post(self,request):
        webhook = request.data.get('webhook')
        
        task  = export_events.delay(webhook)
        
        return Response({"task_id":task.id},status=status.HTTP_200_OK)
        