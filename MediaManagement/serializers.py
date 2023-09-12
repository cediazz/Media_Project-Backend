from rest_framework.serializers import ModelSerializer
from .models import Category,Plan,Coordinadas,Media,Field,MediaContainer,Media_Field

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class CoordinadasSerializer(ModelSerializer):
    class Meta:
        model = Coordinadas
        fields = '__all__'


class FieldSerializer(ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'

class MediaSerializer(ModelSerializer):

    coordinadas = CoordinadasSerializer()
    class Meta:
        model = Media
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        coordinada_data = validated_data.pop('coordinadas')
        coordinadas = Coordinadas.objects.create(**coordinada_data)
        media = Media.objects.create(coordinadas=coordinadas,**validated_data)
        return media

    def update(self, instance, validated_data):
        print(validated_data)
        print(instance.description)
        coordinada_data = validated_data.pop('coordinadas')

        return instance

class MediaSerializerGet(ModelSerializer):
    coordinadas = CoordinadasSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    plan = PlanSerializer(read_only=True)
    class Meta:
        model = Media
        fields = '__all__'

class Media_FieldSerializer(ModelSerializer):

    field = FieldSerializer()
    class Meta:
        model = Media_Field
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        field_data = validated_data.pop('field')
        field = Field.objects.create(**field_data)
        media_field = Media_Field.objects.create(field=field,**validated_data)
        return media_field

class Media_FieldSerializerGet(ModelSerializer):
    media = MediaSerializerGet(read_only=True)
    field = FieldSerializer(read_only=True)
    class Meta:
        model = Media_Field
        fields = '__all__'

class MediaContainerSerializer(ModelSerializer):
    father = MediaSerializer()
    son = MediaSerializer()
    class Meta:
        model = MediaContainer
        fields = '__all__'

"""Estructura para la insercion del Medio y los campos
{
  
  "coordinadas": {
        "lat": "6755",
        "lng": "3453"
    },
  "description": "switch mio",
  "category": 1,
  "plan": 1,
  
}"""





