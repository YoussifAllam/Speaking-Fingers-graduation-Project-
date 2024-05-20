from .serializers import SingUpSerializer,UserSerializer #, VideoSerializer, FavoriteVideoSerializer


from rest_framework import viewsets, status , generics , permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.decorators import action
from django.contrib.auth import get_user_model

from django.core.mail import send_mail
import random
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import  login as django_login
from django.contrib.auth import logout
from rest_framework.decorators import api_view, permission_classes,parser_classes
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404

from django.utils.crypto import get_random_string
from datetime import datetime, timedelta
from .permissions import IsAdminOrPostOnly 
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework.parsers import MultiPartParser, FormParser

import re   
from django.utils.timezone import now
User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SingUpSerializer
    permission_classes = [IsAdminOrPostOnly]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Generate a 4-digit OTP and store it in the user's profile
            otp = random.randint(1000, 9999)
            user.otp = otp
            user.otp_created_at = timezone.now()

            user.save()

            # Send the OTP to the user via email
            current_site = 'Speaking-Fingers.com'
            subject = 'Your verification OTP on {0}'.format(current_site)
            message = f'Your verification OTP is: {otp}'
            user.email_user(subject, message)

            refresh = RefreshToken.for_user(user)
            token_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            return Response({'user': serializer.data, 'tokens': token_data}, status=status.HTTP_201_CREATED)
        else:
            email_errors = serializer.errors.get('email', [])
            password_errors = serializer.errors.get('password', [])

            if email_errors:
                return Response({'message': email_errors[0]}, status=status.HTTP_400_BAD_REQUEST)
            elif password_errors:
                return Response({'message': password_errors[0]}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def confirm_email(self, request):
        user_id = request.data.get('user_id')
        otp = request.data.get('otp')
        
        try:
            user = User.objects.get(pk=str(user_id))
            if user.email_verified:
                return Response({'message': 'تم تاكيد البريد الالكتروني من قبل'}, status=status.HTTP_400_BAD_REQUEST)

            if user.otp == int(otp) and self.is_otp_valid(user.otp_created_at):
                user.email_verified = True
                user.save()
                return Response({'message': 'تم تاكيد البريد الالكتروني بنجاح'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'الكود الذي ادخلته غير صالح'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'message': 'المستخدم غير موجود'}, status=status.HTTP_404_NOT_FOUND)
        
    def is_otp_valid(self, otp_created_at):
        # Check if the OTP is still valid based on the expiration time
        if otp_created_at:
            return otp_created_at <=  otp_created_at + timedelta(hours=2)
        return False

    
    @action(detail=False, methods=['post'])
    def send_reset_otp(self, request):
        email = request.data.get('email', '')
        if not email:  # Check if email is not provided in the request body
            return Response({'message': 'الايميل مطلوب.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)

            # Generate a new 4-digit OTP and update it in the user's profile
            otp = random.randint(1000, 9999)
            user.otp = otp
            user.save()

            # Send the new OTP to the user via email
            current_site = 'Spacetly.com'
            subject = 'Your reset OTP on {0}'.format(current_site)
            message = f'Your reset OTP is: {otp}'
            user.email_user(subject, message)

            return Response({'message': 'تم ارسال الكود الجديد بنجاح'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message': 'المستخدم غير موجود'}, status=status.HTTP_404_NOT_FOUND)

    # @action(detail=False, methods=['post'], url_path='login')
    # def login(self, request):
    #     email = request.data.get('email')
    #     password = request.data.get('password')
    #     user = User.objects.get(email=email)

    #     if user is not None:
    #         refresh = RefreshToken.for_user(user)
    #         token_data = {
    #             'refresh': str(refresh),
    #             'access': str(refresh.access_token),
    #         }

    #         # Add the refresh token to the outstanding tokens
    #         user.outstanding_tokens.append(str(refresh))
    #         user.save()

    #         django_login(request, user)

    #         return Response({'user': SingUpSerializer(user).data, 'tokens': token_data}, status=status.HTTP_200_OK)
    #     else:
    #         return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = UserSerializer(request.user, many=False)
    return Response(user.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def update_user(request):
    user = request.user
    data = request.data

    user.name = data.get('name', user.name)
    if 'profile_picture' in request.data:
        user.profile_picture = request.data['profile_picture']
        if user.profile_picture:
            user.profile_picture = request.data['profile_picture']
        else:
            # Set default profile picture if 'profile_picture' is not provided or empty
            user.profile_picture = 'default.jpg'


    if 'old_password' in data or 'password' in data:
        PASSWORD_PATTERN = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

        if 'old_password' in data and 'new_password' in data and 'confirm_password' in data:
            old_password = data['old_password']
            new_password = data['new_password']
            confirm_password = data['confirm_password']

            # Check if the new password and confirm password are not empty
            if new_password and confirm_password:
                # Verify that the old password matches the user's current password
                if user.check_password(old_password):
                    # Check if the new password is the same as the old password
                    if new_password != old_password:
                        # Check if the new password and confirm password match
                        if new_password == confirm_password:
                            # Check if the new password meets the strength requirements
                            if re.match(PASSWORD_PATTERN, new_password):
                                # Set the new password
                                user.set_password(new_password)
                                # Save the user object
                                user.save()
                            else:
                                # Return an error response indicating that the password does not meet the strength requirements
                                return Response({"message": "يجب ان كلمة المرور تحتوي على حروف كبيرة وصغيرة ورقم ورمز واحد على الاقل"}, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            # Return an error response indicating that the new password and confirm password do not match
                            return Response({"message": "كلمة المرور غير متطابقة"}, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        # Return an error response indicating that the new password is the same as the old password
                        return Response({"message": "كلمة المرور الجديدة يجب ان تكون مختلفة"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    # Return an error response indicating that the old password is incorrect
                    return Response({"message": "كلمة المرور القديمة غير صحيح"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # Return an error response indicating that the new password or confirm password is empty
                return Response({"message": "يرجى تعبئة كلمة المرور الجديدة وتأكيد كلمة المرور"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Return an error response indicating that the required fields are missing
            return Response({"message": "Old password, new password, and confirm password are required"}, status=status.HTTP_400_BAD_REQUEST)

    if 'phone_number' in data:
        user.phone_number = data['phone_number']

    user.save()
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

def get_current_host(request):
    protocol = request.is_secure() and 'https' or 'http'
    host = request.get_host()
    return "{protocol}://{host}/".format(protocol=protocol, host=host)


# @api_view(['POST'])
# def forgot_password(request):
#     data = request.data
#     email = request.GET.get('email')
#     if not email:
#         return Response({'detail': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)

#     user = get_object_or_404(User, email=email)
#     token = get_random_string(40)
#     expire_date = datetime.now() + timedelta(minutes=10)
#     user.profile.reset_password_token = token
#     user.profile.reset_password_expire = expire_date
#     user.profile.save()
    
#     host = get_current_host(request)
#     link = "{host}api/reset_password/{token}".format(token=token, host=host)
#     body = "Your password reset link is : {link}".format(link=link)
#     send_mail(
#         "Paswword reset from Speaking Fingers",
#         body,
#         "Speaking-Fingers@gmail.com",
#         [data['email']]
#     )
#     return Response({'details': 'Password reset sent to {email}'.format(email=data['email']),'link': link,'token': token,})


@api_view(['POST'])
def forgot_password(request):
    data = request.data
    email = data.get('email')
    
    # Check if the email is provided and is not empty
    if not email:
        return Response({'detail': 'Email address is required.'}, status=400)
    
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        # Consider security practices here; in some cases, you might not want to reveal that an email does or doesn't exist in the system
        return Response({'detail': 'User not found.'}, status=404)
    
    token = get_random_string(40)
    expire_date = now() + timedelta(hours=10)
    user.profile.reset_password_token = token
    user.profile.reset_password_expire = expire_date
    user.profile.save()
    
    # Assuming you're using https in production
    host = get_current_host(request)
    link = "{host}api/reset_password/{token}".format(token=token, host=host)
    body = "Your password reset link is : {link}".format(link=link)
    send_mail(
        "Paswword reset from Speaking Fingers",
        body,
        "Speaking-Fingers@gmail.com",
        [data['email']]
    )
    
    # Be cautious about the amount of detail you reveal in success messages
    return Response({'details': 'If the email exists in our system, a password reset link has been sent.', 'link': link, 'token': token})

 
@api_view(['POST'])
def reset_password(request,token):
    data = request.data
    try:
        # print('====================' , token)
        user = User.objects.get(profile__reset_password_token=token)
    except User.DoesNotExist:
        return Response(
            {'message': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST
        )
    if user.profile.reset_password_expire.replace(tzinfo=None) < datetime.now():
        return Response({'message': 'الرابط منتهي'},status=status.HTTP_400_BAD_REQUEST)
    try:
        if not data['password'] or not data['confirmPassword']:
            return Response({'message': 'يجب ان تقوم بأدخال كلمه المرور'},status=status.HTTP_400_BAD_REQUEST)
        
    except : return Response({'message': 'يجب ان تقوم بأدخال كلمات المرور'},status=status.HTTP_400_BAD_REQUEST)
    
    if data['password'] != data['confirmPassword']:
        return Response({'message': 'كلمة المرور غير متطابقة'},status=status.HTTP_400_BAD_REQUEST)
    
    user.password = make_password(data['password'])
    user.profile.reset_password_token = ""
    user.profile.reset_password_expire = None 
    user.profile.save() 
    user.save()
    return Response({'message': 'تم تغيير كلمة المرور بنجاح'})



class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None and user.check_password(password):
            if not user.is_active:
                return Response({'message': 'تم تعطيل حسابك'}, status=status.HTTP_403_FORBIDDEN)

            if not user.email_verified:
                return Response({'user_id': user.id,'message': 'يرجي تفعيل البريد الالكتروني'}, status=status.HTTP_403_FORBIDDEN)
            
            refresh = RefreshToken.for_user(user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            django_login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            return Response({'user': UserSerializer(user).data, 'tokens': data}, status=status.HTTP_200_OK)
        #check if email not exist
        elif user is None:
            return Response({'message': 'لم يتم العثور على البريد الالكتروني'}, status=status.HTTP_401_UNAUTHORIZED)
            
        else:
            return Response({'message': 'خطاء في البريد الالكتروني او كلمة المرور'}, status=status.HTTP_401_UNAUTHORIZED)


class APILogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if self.request.data.get('all'):
            token: OutstandingToken
            for token in OutstandingToken.objects.filter(user=request.user):
                _, _ = BlacklistedToken.objects.get_or_create(token=token)
            return Response({"status": "OK, goodbye, all refresh tokens blacklisted"})
        refresh_token = self.request.data.get('refresh_token')
        token = RefreshToken(token=refresh_token)
        token.blacklist()
        logout(request)
        return Response({"status": "OK, goodbye"})
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_user_permissions(request, username):
    # Check if the requesting user is a superuser or staff
    if not (request.user.is_superuser or request.user.is_staff):
        return Response({"message": "ليس لديك صلاحيات لتغيير صلاحيات المستخدم"}, status=status.HTTP_403_FORBIDDEN)

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({"message": "المستخدم غير موجود"}, status=status.HTTP_404_NOT_FOUND)

    data = request.data
    is_staff = data.get('is_staff', False)
    is_superuser = data.get('is_superuser', False)

    # Only superusers can set superuser flag
    if request.user.is_superuser:
        user.is_superuser = is_superuser

    # Both superusers and staff can set staff flag
    user.is_staff = is_staff

    user.save()

    return Response({"message": "User permissions updated successfully"}, status=status.HTTP_200_OK)
       
       
#! vedios ___________________________________________________________________

# class VideoListView(viewsets.ModelViewSet):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
#     def list(self, request, *args, **kwargs):
#         response = super(VideoListView, self).list(request, *args, **kwargs)
        
#         formatted_response = {
#             "status": "success",
#             "data": {
#                 "videos": response.data
#             }
#         }
        
#         return Response(formatted_response) 

# from django.core.exceptions import ObjectDoesNotExist
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_video_details(request):
#     # Use request.query_params instead of request.data for GET requests
#     video_title = request.GET.get('video_title', None)
    
#     if video_title:
#         try:
#             targetvideo = Video.objects.get(title=video_title)
#             serializer = VideoSerializer(targetvideo, context={'request': request})
#             json = {
#                 "status": "success",
#                 "data": {
#                     "video": serializer.data
#                 }
#             }
#             return Response(json)
#         except ObjectDoesNotExist:
#             return Response({"message": "Video with the specified title does not exist."}, status=status.HTTP_404_NOT_FOUND)
#     else:
#         return Response({"message": "You should enter video_title."}, status=status.HTTP_400_BAD_REQUEST)


# class FavoriteVideoListCreateView(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = FavoriteVideoSerializer

#     lookup_field = 'video_id'
    
#     def get_queryset(self):
#         return FavoriteVideos.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
        
#     def delete(self, request, *args, **kwargs):
#         video_id = kwargs.get('video_id')
#         print('2__________________' , video_id)
#         try:
#             favorite_video = FavoriteVideos.objects.get(user=request.user, video__id=video_id)
#             favorite_video.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except FavoriteVideos.DoesNotExist:
#             return Response({"message": "Video not found in favorites or already removed."}, status=status.HTTP_404_NOT_FOUND)
        
    
# class FavoriteVideoDestroyView(generics.DestroyAPIView):
#     serializer_class = FavoriteVideoSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     lookup_field = 'video_id'  # Assuming 'video_id' is the URL kwarg to look up a FavoriteVideos instance

#     def get_queryset(self):
#         # Filter the queryset to only include the user's favorite videos
#         return FavoriteVideos.objects.filter(user=self.request.user)

#     def delete(self, request, *args, **kwargs):
#         video_id = kwargs.get('video_id')
#         print(video_id , '===========================')
#         try:
#             favorite_video = FavoriteVideos.objects.get(user=request.user, video__id=video_id)
#             favorite_video.delete()
#             return Response( {"message": "removed successfully."}, status=status.HTTP_204_NO_CONTENT)
        
#         except FavoriteVideos.DoesNotExist:
#             return Response({"message": "Video not found in favorites or already removed."}, status=status.HTTP_404_NOT_FOUND)
        
        
        
        
        
        
