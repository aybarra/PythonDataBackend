from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, PFRtoGuidModel, GameModel
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')

class PFRGuidSerializer(serializers.ModelSerializer):
    # owner = serlizers.ReadOnlyField(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(view_name='pfrguids-detail', format='html')

    class Meta:
        model = PFRtoGuidModel
        fields = ('pro_football_ref_name', 'player_full_name', 'pguid')

# class CareerSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = CareerModel
#         fields = ('pguid', 'ff_pts', 'start_date', 'end_date', 'win_pct')

# class SeasonSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = SeasonModel
#         fields = 

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameModel
        fields = ('pguid', 'year', 'game_count_played', 'game_number', 
                  'date', 'home_team', 'home_or_away', 'opp_team',
                  'result', 'gs', 
                  # Passing 
                  'pass_comp', 'pass_att', 'comp_pct', 
                  'pass_yards', 'pass_tds', 'ints_thrown', 
                  'qb_rating', 'yards_per_pass_att', 'adj_yards_per_pass_att', 
                  # Rushing 
                  'rush_att', 'rush_yards', 'yards_per_rush_att', 'rush_tds',
                  # Receiving
                  'pass_tgts', 'receptions', 'rec_yards', 'yards_per_rec', 'rec_tds', 
                  
                  # Two Pt Conversions
                  'two_pt_conv_made',

                  # Punt returns
                  'punt_returns', 'pr_yards', 'yards_per_punt_return', 'pr_tds',
                  
                  # Kickoff returns
                  'kickoff_returns', 'kr_yards', 'yards_per_kick_return', 'kr_tds', 
                  
                  # Punting
                  # 'punts', 'punt_yards', 'yards_per_punt', 'times_punt_blocked',
                  'game_ff_pts')

# class SnippetSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance