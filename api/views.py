from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from core.models import Product, Category, Feedback
from .serializers import (UserCreateSerializer,
                          UserUpdateSerializer,
                          UserListSerializer,
                          UserDetailSerializer,
                          ProductListSerializer,
                          ProductDetailSerializer,
                          CategoryListSerializer,
                          CategoryDetailSerializer,
                          FeedbackCreateSerializer,
                          FeedbackListSerializer,
                          FeedbackDetailSerializer)


class UserCreateView(APIView):
    """Создание нового пользователя"""

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserUpdateView(UpdateAPIView):
    """Изменение данных пользователя"""
    serializer_class = UserUpdateSerializer
    queryset = User.objects.filter()


class UserListView(APIView):
    """Вывод списка пользователей"""

    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)


class UserDetailView(APIView):
    """Вывод конкретного пользователя"""

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


class ProductListView(APIView):
    """Вывод списка товаров"""

    def get(self, request):
        products = Product.objects.filter(status=1)
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    """Вывод конкретного товара"""

    def get(self, request, pk):
        product = Product.objects.get(status=1, id=pk)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)


class CategoryListView(APIView):
    """Вывод списка категорий"""

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoryListSerializer(categories, many=True)
        return Response(serializer.data)


class CategoryDetailView(APIView):
    """Вывод конкретной категории"""

    def get(self, request, pk):
        category = Category.objects.get(id=pk)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)


class FeedbackCreateView(APIView):
    """Добавление отзыва к товару"""

    def post(self, request):
        serializer = FeedbackCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=201)


class FeedbackListView(APIView):
    """Вывод списка отзывов"""

    def get(self, request):
        feedbacks = Feedback.objects.all()
        serializer = FeedbackListSerializer(feedbacks, many=True)
        return Response(serializer.data)


class FeedbackDetailView(APIView):
    """Вывод конкретного отзыва"""

    def get(self, request, pk):
        feedback = Feedback.objects.get(id=pk)
        serializer = FeedbackDetailSerializer(feedback)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        feedback = Feedback.objects.get(id=pk)
        feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
