
# Primero importamos los modelos que queremos serializar:
from e_commerce.models import Comic,WishList
from django.contrib.auth.models import User

# Luego importamos todos los serializadores de django rest framework.
from rest_framework import serializers

class ComicSerializer(serializers.ModelSerializer):
    # algo =  serializers.SerializerMethodField()
    class Meta:
        model = Comic
        fields = ('marvel_id','title', 'description', 'price', 'stock_qty', 'picture')
        # fields = ('marvel_id', 'title', 'algo')

    # def get_algo(self, obj):
    #     return {'hola':10}


class WishListSerializer(serializers.ModelSerializer):
    # Incluyo aquellos fields del WishList Model que poseen Foreign Keys de tablas relacionadas:
    user_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all())
    comic_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Comic.objects.all())
    class Meta:
        model = WishList
        fields= ("__all__")



# TODO: Realizar el serializador para el modelo de WishList



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ("__all__")
