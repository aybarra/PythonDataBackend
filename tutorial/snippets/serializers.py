from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, PFRtoGuidModel, GameModel, SeasonModel, CareerModel
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404


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

    class Meta:
        model = PFRtoGuidModel
        fields = ('pfr_name', 'player_name', 'pguid', 'pos_type')
        lookup_field = 'pguid'

class CareerSerializer(serializers.HyperlinkedModelSerializer): #serializers.ModelSerializer):
    # player_name = serializers.CharField(source='careermodel.player_name')
    player_name = serializers.HyperlinkedRelatedField(
        view_name='pfrguidmodel-detail',
        read_only=True,
        lookup_field='pguid'
    )

    class Meta:
        model = CareerModel
        fields = ('pguid', 'ff_pts', 'start_year', 'end_year', 'win_pct', 'active', 'player_name')
        lookup_field = 'pfrtoguidmodel__player_name'

    @receiver(post_save, sender=CareerModel)
    def create_pfrtoguidmodel(sender, instance, created, **kwargs):
        instance.pfrtoguidmodel = get_object_or_404(PFRtoGuidModel, pk=instance.pguid)

class SeasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = SeasonModel
        fields = ('season_guid', 'pguid', 'year', 'games_played', 
            'pass_tds', 'pass_yards', 'ints_thrown', 'rec_tds',
            'rec_yards', 'rush_tds', 'rush_yards', 'kr_tds', 'pr_tds',
            'fumbles_lost', 'season_ff_pts')

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