from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import Message, Author

'''
class MessageSerializer(serializers.Serializer):
    # author = serializers.IntegerField()
    content = serializers.CharField()
    #date = serializers.DateTimeField()
    #author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.filter(), source='author.id')

    def create(self, validated_data):
        return Message.objects.create(**validated_data)



'''






class MessageSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    author_city = serializers.CharField(source='author.city', read_only=True)


    class Meta:
        model = Message
        fields = ('id', 'author_name','author_city', 'created_at', 'content')
