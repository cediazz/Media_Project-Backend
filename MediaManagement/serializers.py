from rest_framework.serializers import ModelSerializer
from .models import Category,Plan,Coordinadas,Media,Field,MediaContainer

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
        exclude = ['media']

class MediaSerializer(ModelSerializer):
    fieldss = FieldSerializer(many=True)
    coordinadas = CoordinadasSerializer()
    class Meta:
        model = Media
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        field_data = validated_data.pop('fieldss')
        coordinada_data = validated_data.pop('coordinadas')
        coordinadas = Coordinadas.objects.create(**coordinada_data)
        media = Media.objects.create(coordinadas=coordinadas,**validated_data)
        for field in field_data:
         Field.objects.create(media=media, **field)
        return media

class MediaSerializerGet(ModelSerializer):
    fieldss = FieldSerializer(many=True)
    category = CategorySerializer(read_only=True)
    plan = PlanSerializer(read_only=True)
    coordinadas = CoordinadasSerializer(read_only=True)
    class Meta:
        model = Media
        fields = '__all__'

class MediaContainerSerializer(ModelSerializer):
    father = MediaSerializer()
    son = MediaSerializer()
    class Meta:
        model = MediaContainer
        fields = '__all__'

"""Estructura para la insercion del Medio y los campos
{
  "fieldss": [
    {
      "name": "marca",
      "value": "sony"
    },
    {
      "name": "color",
      "value": "verde"
    },
    {
      "name": "tamano",
      "value": "45"
    }

  ],
  "coordinadas": {
        "lat": "6755",
        "lng": "3453"
    },
  "description": "switch mio",
  "category": 1,
  "plan": 1,
  
}"""





