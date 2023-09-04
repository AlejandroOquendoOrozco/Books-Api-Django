from rest_framework import serializers
from LibrosApi.models import Libro

class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField()
    numero_de_paginas=serializers.IntegerField()
    dia_de_publicacion=serializers.DateField()
    cantidad=serializers.IntegerField()
    

    def create(self,data):

        return Libro.objects.create(**data)
    

    def update(self, instance, validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.numero_de_paginas=validated_data.get('numero_de_paginas',instance.numero_de_paginas)
        instance.dia_de_publicacion=validated_data.get('dia_de_publicacion',instance.dia_de_publicacion)
        instance.cantidad=validated_data.get('cantidad',instance.cantidad)
        
        instance.save()
        return instance