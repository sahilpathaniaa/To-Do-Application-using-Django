from . forms import TaskCreate
from . models import Task, Tag
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskSerializer

class TaskApi(APIView):
    def get(self, request, pk=None, format=None):
# <----------------------GET DATA ------------------------------->
        if pk is not None:
            try:
                task = Task.objects.get(id=pk)
                serializer = TaskSerializer(task)
                return Response(serializer.data)
            except:
                return Response({'message': "The data you are requesting is not available or deleted "})
        else:       
            task = Task.objects.all()
            serializer=TaskSerializer(task, many=True)
            return Response(serializer.data )

# <----------------------Add Data (POST) ------------------------->
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid(): 
            tags=request.data.get('tags')
            tag_id=[]
            for x in tags:
                tag_id.append(int(Tag.objects.get(name=x).id))
            serializer.save(tags=tag_id)
            return Response({'message':'Your data has been added successfully '})
        return Response(serializer.errors)

# <----------------------COMPLETE DATA UPDATE --------------------->
    def put(self, request,pk, format=None):
        try:
            task = Task.objects.get(id=pk)
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                tags=request.data.get('tags')
                tag_id=[]
                for x in tags:
                    tag_id.append(int(Tag.objects.get(name=x).id))
                serializer.save(tags=tag_id)
                return Response({'message':'Your data has been Updated successfully '})
        except:
            return Response({"Error message": "Check the id of the post you are trying to update "})
        return Response(serializer.errors)


# <----------------------PARTIAL DATA UPDATE ------------------------->
    def patch(self, request,pk, format=None):
        try:
            task = Task.objects.get(id=pk)
            serializer = TaskSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                tags=request.data.get('tags')
                tag_id=[]
                for x in tags:
                    tag_id.append(int(Tag.objects.get(name=x).id))
                serializer.save(tags=tag_id)
                return Response({'message':'Your data has been Updated successfully '})
        except:
            return Response({"Error message": "Check the id of the post you are trying to update "})
        return Response(serializer.errors)


# <------------------------DELETE DATA-------------------------------->
    def delete(self, request,pk, format=None):
        try:    
            task = Task.objects.get(id=pk)
            task.delete()
            return Response({'message':'Your data has been Deleted  '})
        except:
            return Response({'message': "The data you are requesting is not available or deleted "})