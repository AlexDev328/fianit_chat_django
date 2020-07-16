from rest_framework import serializers

from .models import Message

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

    class Meta:
        model = Message
        fields = ('id', 'author', 'created_at', 'content')

