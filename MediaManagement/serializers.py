from rest_framework.serializers import ModelSerializer
from .models import Category, Plan, Coordinadas, Media, Field, MediaContainer, Media_Field

class FieldSerializer(ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    fields = FieldSerializer(many=True, read_only=True)
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





class MediaSerializer(ModelSerializer):
    coordinadas = CoordinadasSerializer()

    class Meta:
        model = Media
        fields = '__all__'

    def create(self, validated_data):
        # Acceder a los datos no validados o enviados de más
        extra_data = self.context['request'].data
        print(extra_data)
        media_father = None
        #******Si se envia un Id de Medio padre, buscar el medio padre*************
        if 'mediaFatherId' in extra_data:
            media_father_id = extra_data['mediaFatherId']
            media_father = Media.objects.filter(id=media_father_id).first()
        #*******Insertar las coordenadas*********
        coordinada_data = validated_data.pop('coordinadas')
        coordinadas = Coordinadas.objects.filter(lat=coordinada_data['lat'], lng=coordinada_data['lng']).first()
        if coordinadas == None:
            coordinadas = Coordinadas.objects.create(**coordinada_data)
        #*******Insertar el Medio*******
        media = Media.objects.create(coordinadas=coordinadas, **validated_data)
        #*******Insertar Campos del Medio*******
        for key, value in extra_data['fields'].items():
            field = Field.objects.filter(id = key).first()
            Media_Field.objects.create(media =media, field = field, field_value=value['value'], link_media=value['link'])
        #Insertar Medio padre e hijo si se requiere
        if (media_father != None):
            MediaContainer.objects.create(father=media_father, son=media)
        if 'mediaSonId' in extra_data:
            media_son_id = extra_data['mediaSonId']
            media_son = Media.objects.filter(id=media_son_id).first()
            media_son_coordinadas = Coordinadas.objects.filter(id = media_son.coordinadas.id).first()
            media_son_coordinadas.lat = coordinada_data['lat']
            media_son_coordinadas.lng = coordinada_data['lng']
            media_son_coordinadas.save()
            media_son.plan = validated_data['plan']
            media_son.save()
            MediaContainer.objects.create(father=media, son=media_son)
        return media

    def update(self, instance, validated_data):
        extra_data = self.context['request'].data
        #print(extra_data)
       # print(validated_data)
        coordinadas_data = validated_data.pop('coordinadas')
        if coordinadas_data:
            coordinadas_serializer = CoordinadasSerializer(instance.coordinadas, data=coordinadas_data)
            if coordinadas_serializer.is_valid():
                coordinadas_serializer.save()
        # *******Actualizar valores de los Campos del Medio*******
        for key, value in extra_data['fields'].items():
            media_field = Media_Field.objects.filter(id=value['idMediaField']).first()
            media_field.field_value = value['value']
            media_field.link_media = value['link']
            media_field.save()
        if 'mediaSonId' in extra_data:
            media_son_id = extra_data['mediaSonId']
            media_son = Media.objects.filter(id=media_son_id).first()
            media_son_coordinadas = Coordinadas.objects.filter(id = media_son.coordinadas.id).first()
            media_son_coordinadas.lat = coordinadas_data['lat']
            media_son_coordinadas.lng = coordinadas_data['lng']
            media_son_coordinadas.save()
            media_son.plan = validated_data['plan']
            media_son.save()
            MediaContainer.objects.create(father=instance, son=media_son)
        else:
            media_container = MediaContainer.objects.filter(father = instance.id).first()
            print(media_container)
            media_son = Media.objects.filter(id=media_container.son.id).first()
            media_son_coordinadas = Coordinadas.objects.filter(id=media_son.coordinadas.id).first()
            media_son_coordinadas.lat = coordinadas_data['lat']
            media_son_coordinadas.lng = coordinadas_data['lng']
            media_son_coordinadas.save()
            #valorar realizar un ciclo para actualizar el plano de los medios hijos
            media_son.plan = validated_data['plan']
            media_son.save()
        return super().update(instance, validated_data)


class MediaSerializerGet(ModelSerializer):
    coordinadas = CoordinadasSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    plan = PlanSerializer(read_only=True)

    class Meta:
        model = Media
        fields = '__all__'


class Media_FieldSerializer(ModelSerializer):


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
        fields = ['field', 'link_media', 'field_value']


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
    father_containers = MediaContainerSerializerGet(many=True, read_only=True)
    media_fields = FieldsAllSerializer(many=True , read_only=True)
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
