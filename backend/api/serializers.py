from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model


# class AuthoUsernameField(serializers.RelatedField):
#     def to_representation(self, value):
#         # return value.first_name + " " + value.last_name
#         return value.username
class ArticleSerialiser(serializers.ModelSerializer):
    def get_author(self,obj):
        return {
            "username" : obj.author.username,
            "first_name" : obj.author.first_name,
            "last_name":obj.author.last_name,
        }

    author= serializers.SerializerMethodField("get_author")
    class Meta:
        model =Article
        fields="__all__"

        def validate_title(self, value):
            filter_list = ["javascript","php"]

            for i in filter_list:
                if i in value:
                    raise serializers.ValidationError("Do't use bad word : {}".format(i))
                

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields="__all__"
