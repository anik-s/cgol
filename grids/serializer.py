from rest_framework import serializers

from grids.models import Grid


class GridSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grid
        fields = ('id', 'x', 'y', 'data')

    def create(self, validated_data):
        print(validated_data['data'])
        grid = Grid.objects.create(**validated_data)
        return grid

    def update(self, instance, validated_data):
        instance.x = validated_data.get('x', instance.x)
        instance.y = validated_data.get('y', instance.y)
        instance.data = validated_data.get('data', instance.data)
        instance.save()
        return instance
