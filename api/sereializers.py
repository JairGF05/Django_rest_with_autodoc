#se pueden convertir los datos del modelo en una lista de elementos en foormato JSON 
from rest_framework import serializers
from .models import Programmer

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        #que campos queremos que se serialcen, solo los que yo requiera
        #en este campo se toman todos los campos 
        #fields = ('fullname', 'nickname')
        fields = '__all__'
