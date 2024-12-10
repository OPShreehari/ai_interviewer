from rest_framework import serializers
from .models import ProgrammingQuestion

class ProgrammingQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingQuestion
        fields = '__all__'
