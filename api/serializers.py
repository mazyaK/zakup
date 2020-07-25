from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from accounts.models import User
from core.models import Product, Category, Feedback
from cart.cart import Cart
from django.conf import settings
from django.utils import formats


class UserCreateSerializer(serializers.ModelSerializer):
    """Создание нового пользователя"""
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")


class UserListSerializer(serializers.ModelSerializer):
    """Cписок пользователей"""

    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    # last_login = serializers.SerializerMethodField()

    def get_created_on(self, obj):
        return formats.date_format(obj.created_on, 'DATETIME_FORMAT')

    def get_updated_on(self, obj):
        return formats.date_format(obj.updated_on, 'DATETIME_FORMAT')

    # def get_last_login(self, obj):
    #     return formats.date_format(obj.last_login, 'DATETIME_FORMAT')

    class Meta:
        model = User
        exclude = ("password", "date_joined", "groups", "user_permissions", "last_login")


class UserDetailSerializer(serializers.ModelSerializer):
    """Конкретный пользователь"""

    class Meta:
        model = User
        exclude = ("password", "date_joined", "groups", "user_permissions")


class UserUpdateSerializer(serializers.ModelSerializer):
    """Обновление данных о пользователе"""

    class Meta:
        model = User
        fields = ("about_me",)

    def update(self, instance, validated_data):
        instance.about_me = validated_data.get('about_me')
        instance.save()
        return instance


class CategoryListSerializer(serializers.ModelSerializer):
    """Список категорий"""

    class Meta:
        model = Category
        fields = ("id", "name", "slug")


class CategoryDetailSerializer(serializers.ModelSerializer):
    """Конкретная категория"""

    class Meta:
        model = Category
        fields = ("id", "name", "slug")


class FeedbackListSerializer(serializers.ModelSerializer):
    """Список отзывов"""
    created_on = serializers.SerializerMethodField()

    def get_created_on(self, obj):
        return formats.date_format(obj.created_on, 'DATETIME_FORMAT')

    class Meta:
        model = Feedback
        fields = ("id", "name", "body", "created_on")


class FeedbackCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Feedback
        fields = "__all__"


class FeedbackDetailSerializer(serializers.ModelSerializer):
    """Удаление отзыва"""
    created_on = serializers.SerializerMethodField()

    def get_created_on(self, obj):
        return formats.date_format(obj.created_on, 'DATETIME_FORMAT')

    class Meta:
        model = Feedback
        fields = ("id", "name", "body", "created_on")


class ProductListSerializer(serializers.ModelSerializer):
    """Список товаров"""
    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()
    category = CategoryListSerializer(many=True, read_only=True)
    feedback = FeedbackListSerializer(many=True)

    def get_created_on(self, obj):
        return formats.date_format(obj.created_on, 'DATETIME_FORMAT')

    def get_updated_on(self, obj):
        return formats.date_format(obj.updated_on, 'DATETIME_FORMAT')

    class Meta:
        model = Product
        fields = "__all__"


class ProductDetailSerializer(serializers.ModelSerializer):
    """Конкретный товар"""
    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()
    category = CategoryListSerializer(many=True, read_only=True)
    feedback = FeedbackListSerializer(many=True)

    def get_created_on(self, obj):
        return formats.date_format(obj.created_on, 'DATETIME_FORMAT')

    def get_updated_on(self, obj):
        return formats.date_format(obj.updated_on, 'DATETIME_FORMAT')

    class Meta:
        model = Product
        fields = "__all__"









