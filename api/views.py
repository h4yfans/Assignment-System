from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)
from .serializers import AssignmentSerializer
from .models import Assignment


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

    def create(self, request, **kwargs):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            assignment = serializer.create(request)
            if assignment:
                return Response(status=HTTP_201_CREATED)
            return Response(status=HTTP_400_BAD_REQUEST)

