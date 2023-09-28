from rest_framework.serializers import ModelSerializer
from .models import Category, Plan, Coordinadas, Media, Field, MediaContainer, Media_Field


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
        # Acceder a los datos no validados o enviados de más
        extra_data = self.context['request'].data
        media_father = None
        if 'mediaFatherId' in extra_data:
            media_father_id = extra_data['mediaFatherId']
            media_father = Media.objects.filter(id=media_father_id).first()
        coordinada_data = validated_data.pop('coordinadas')
        coordinadas = Coordinadas.objects.filter(lat=coordinada_data['lat'], lng=coordinada_data['lng']).first()
        if coordinadas == None:
            coordinadas = Coordinadas.objects.create(**coordinada_data)
        media = Media.objects.create(coordinadas=coordinadas, **validated_data)
        if (media_father != None):
            MediaContainer.objects.create(father=media_father, son=media)
        if 'mediaSonId' in extra_data: #para adicionarle un medio ver como puedo hacer para cambiar los datos de la coordenada
            media_son_id = extra_data['mediaSonId']
            MediaContainer.objects.create(father=media, son=media_son_id)
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
        media_field = Media_Field.objects.create(field=field, **validated_data)
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


class MediaContainerSerializer(ModelSerializer):
    class Meta:
        model = MediaContainer
        fields = '__all__'


class MediaContainerFatherSerializer(ModelSerializer):
    coordinadas = CoordinadasSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    plan = PlanSerializer(read_only=True)
    media_fields = FieldsAllSerializer(many=True, read_only=True)

    class Meta:
        model = Media
        fields = '__all__'


class MediaContainerSerializerGet(ModelSerializer):
    father = MediaContainerFatherSerializer(read_only=True)

    class Meta:
        model = MediaContainer
        fields = ['father']


class Media_Fields_AllSerializer(ModelSerializer):
    coordinadas = CoordinadasSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    plan = PlanSerializer(read_only=True)
    media_fields = FieldsAllSerializer(many=True, read_only=True)
    father_containers = MediaContainerSerializerGet(many=True, read_only=True)

    class Meta:
        model = Media
        fields = '__all__'


class MediaContainerSerializerGetSon(ModelSerializer):
    son = MediaContainerFatherSerializer(read_only=True)

    class Meta:
        model = MediaContainer
        fields = ['son']


class Media_Fields_Sons_AllSerializer(ModelSerializer):
    coordinadas = CoordinadasSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    plan = PlanSerializer(read_only=True)
    media_fields = FieldsAllSerializer(many=True, read_only=True)
    son_containers = MediaContainerSerializerGetSon(many=True, read_only=True)

    class Meta:
        model = Media
        fields = '__all__'
