# # 방법 1
# from rest_framework import viewsets

# 방법 2
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

##########
from .serializers import UserSerializer
from .models import User

# # 방법 1
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# 방법 2
@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        if len(serializer.data) == 0:
            return Response("User에 데이터 없음",status=404)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=200)

        return Response("User 생성 실패", status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def user_select(request, _id):
    try:
        user = User.objects.get(_id=_id)
    except User.DoesNotExist:
        return Response("대상이 존재하지 않음", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)

        return Response(serializer.data, status=200)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=200)
        
        return Response("User 수정 실패", status=500)
    elif request.method == 'DELETE':
        user.delete()

        return Response(_id + " 삭제 완료",status=200)