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

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "description": instance.description,
            "image": f"http://127.0.0.1:8000/Media/{instance.image}",

        }


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
        coordinadas_data = validated_data.pop('coordinadas', None)
        if coordinadas_data:
            coordinadas_serializer = CoordinadasSerializer(instance.coordinadas, data=coordinadas_data)
            if coordinadas_serializer.is_valid():
                coordinadas_serializer.save()
        return super().update(instance, validated_data)

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

class Media_FieldSerializerPost(ModelSerializer):

   class Meta:
        model = Media_Field
        fields = '__all__'

class Media_FieldSerializerGet(ModelSerializer):
    media = MediaSerializerGet(read_only=True)
    field = FieldSerializer(read_only=True)
    class Meta:
        model = Media_Field
        fields = '__all__'

class FieldsAllSerializer(ModelSerializer):

    field = FieldSerializer(read_only=True)
    class Meta:
        model = Media_Field
        fields = ['field']

class Media_Fields_AllSerializer(ModelSerializer):
    coordinadas = CoordinadasSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    plan = PlanSerializer(read_only=True)
    media_fields = FieldsAllSerializer(many=True, read_only=True)
    class Meta:
        model = Media
        fields = '__all__'

class MediaContainerSerializer(ModelSerializer):
    father = MediaSerializer()
    son = MediaSerializer()
    class Meta:
        model = MediaContainer
        fields = '__all__'







