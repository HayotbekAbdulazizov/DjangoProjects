from rest_framework import fields, serializers
from main.models import  GitProfile, Repository


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = ['profile','name', 'description']



class GitProfileSerializer(serializers.ModelSerializer):
    repos = RepositorySerializer(many=True, read_only=True)
    class Meta:
        model = GitProfile
        fields = ['username', 'pat', 'full_name', 'email','password','description', 'status','repos']