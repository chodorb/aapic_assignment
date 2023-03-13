from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

from performances.models import Performance
from performances.serializers import PerformanceSerializer

from events.models import Event


class PerformanceListApiView(APIView):
    def get(self, request, event_id):
        performances = Performance.objects.filter(event_id=event_id)
        serializer = PerformanceSerializer(performances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request,event_id):
        event = Event.objects.get(pk=event_id)
        serializer = PerformanceSerializer(data = request.data)
        if serializer.is_valid():
            start_time = serializer.validated_data['start']
            end_time = serializer.validated_data['end']
            
            if start_time < event.start or end_time > event.end:
                raise ValidationError("Performances time do not fit in event planned time")
            
            for performance in Performance.objects.filter(event_id=event_id):
                if start_time < performance.end and end_time > performance.start:
                    raise ValidationError("Performances overlap one another.")
            
            serializer.save(event_id=event_id)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
            