from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer
from .models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
from rest_framework_simplejwt.tokens import RefreshToken

class CommonView(APIView):
    model = User
    serializer_class = LoginSerializer
    permission_classes = [
        AllowAny,
    ]

class LoginView(CommonView):
    def post(self, request, format=None):
        user_id = request.data['user_id']
        user_password = request.data['user_password']

        queryset = User.objects.raw(f"select * from tbl_job_users where user_id=('{user_id}') \
            and BINARY user_password=password('{user_password}');")

        # id, pw 존재하면 토큰 생성하여 response
        if queryset:
            serializer = LoginSerializer(queryset[0])
            token = RefreshToken.for_user(queryset[0])
            refresh = str(token)
            access = str(token.access_token)

            data = Response({
                'user': serializer.data,
                'message': 'success',
                'refresh': refresh,
                'access': access,
            })

            # 쿠키 세팅
            data.set_cookie('refresh', refresh, httponly=True)
            data.set_cookie('access', access, httponly=True)
            return data
        else:
            return Response({"message": "failed"})


class LogoutView(CommonView):
    def post(self, request, format=None):
        data = Response({
            "message" : "success"
        })

        # 쿠키 제거
        data.delete_cookie('refresh')
        data.delete_cookie('access')
        return data

        
