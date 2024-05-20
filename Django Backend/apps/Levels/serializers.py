from rest_framework import serializers
from .models import * 

class Leve_1_serializer(serializers.ModelSerializer):
    class Meta:
        model = Level_1_const
        fields = '__all__'
        
class Leve_2_serializer(serializers.ModelSerializer):
    class Meta:
        model = Level_2_v_d
        fields = '__all__'
        
class Leve_3_serializer(serializers.ModelSerializer):
    class Meta:
        model = Level_3_sent
        fields = '__all__'
        
class ReadingTest_serializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingTest
        fields  = '__all__'