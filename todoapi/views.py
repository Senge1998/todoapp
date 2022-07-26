from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from django.db import connection

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list',
        'Create': '/task-create',
        'Update': '/task-update'
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Todo.objects.raw("select * from todoapi_todo order by completed_at desc")
    serializer = TodoSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TodoSerializer(data=request.data)
    print(connection.queries)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    tasks = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)