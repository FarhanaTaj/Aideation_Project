from rest_framework import generics, permissions
from .models import Article, Tag
from .serializers import ArticleSerializer, TagSerializer
from django.conf import settings
from django.http.response import JsonResponse
from rest_framework.response import Response
from requests.api import request
from django.db.models import Q
from django.contrib import auth
from django.contrib.auth import authenticate
from django.db.utils import IntegrityError
from ams_app.backends import *
#  ams_app.decorator import *
from .serializers import *
import random
from .models import *
import time
import datetime
import inspect
from django.core.mail import message, send_mail, EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.views import APIView 
from rest_framework.generics import GenericAPIView
import jwt
from rest_framework import status
from django.utils.decorators import method_decorator
import re
from mimetypes import guess_extension
# from .pagination import *
import base64
from django.core.exceptions import ObjectDoesNotExist

import json

# List/Create Articles
class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Author is the logged-in user

# Retrieve/Update/Delete Articles
class ArticleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:  # Admin can access all articles
            return Article.objects.all()
        return Article.objects.filter(author=self.request.user)  # Users can only access their own articles

# List/Create Tags
class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

# Retrieve/Update/Delete Tags
class TagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]
