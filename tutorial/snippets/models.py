from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
import hashlib
import random

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

from rest_framework import serializers

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES,
                                default='python',
                                max_length=100)
    style = models.CharField(choices=STYLE_CHOICES,
                             default='friendly',
                             max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets')
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

        # limit the number of instances retained
        snippets = Snippet.objects.all()
        if len(snippets) > 100:
            snippets[0].delete()

''' Model for mapping the name to the guid ''' 
class PFRtoGuidModel(models.Model):
	# owner = models.ForeignKey('auth.User')
	pro_football_ref_name = models.CharField(primary_key=True, max_length=30, blank=False)
	player_full_name = models.CharField(primary_key=False, max_length=50, blank=False)
	pguid = models.CharField(primary_key=False, max_length=40, blank=True, editable=False)

	def save(self, *args, **kwargs):
		if not self.pguid:
			self.pguid = hashlib.sha1(str(random.random())).hexdigest()
		super(PFRtoGuidModel, self).save(*args, **kwargs)

# ''' Model for career data ''' 
# class CareerModel(models.Model):
#     pguid = models.UUIDField(primary_key=True, format='hex_verbose', blank=False, editable=False)
#     ff_pts = models.IntegerField()
#     start_date = models.DateField()
#     end_date = models.DateField()
#     win_pct = models.DecimalField(max_digits=5, decimal_places=2)

#     def save(self, *args, **kwargs):
#         super(CareerModel, self).save(*args, **kwargs)

# ''' Season data '''
# class SeasonModel(models.Model):

#     def save(self, *args, **kwargs):
#         super(SeasonModel, self).save(*args, **kwargs)

''' Single game data ''' 
class GameModel(models.Model):
    pguid = models.CharField(max_length=40)#serializers.UUIDField(format='hex')
    year = models.IntegerField()
    game_count_played = models.IntegerField()
    game_number = models.IntegerField()
    date = models.DateField()
    home_team = models.CharField(max_length=3)
    home_or_away = models.CharField(choices=(('home','home'),('away','away')), max_length=4)
    opp_team = models.CharField(max_length=3)
    result = models.CharField(max_length=10)
    
    # QB PASSING STATS 
    gs = models.CharField(blank=True, null=True, max_length=10)
    pass_comp = models.IntegerField(blank=True, null=True)
    pass_att = models.IntegerField(blank=True, null=True)
    comp_pct = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    pass_yards = models.IntegerField(blank=True, null=True)
    pass_tds = models.IntegerField(blank=True, null=True)
    ints_thrown = models.IntegerField(blank=True, null=True)
    qb_rating = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=1)
    yards_per_pass_att = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)
    adj_yards_per_pass_att = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)

    # RUSHING STATS
    rush_att = models.IntegerField(blank=True, null=True)
    rush_yards = models.IntegerField(blank=True, null=True)  # Yards gained by rushing 
    yards_per_rush_att = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)
    rush_tds = models.IntegerField(blank=True,null=True)

    # RCVING STATS
    pass_tgts = models.IntegerField(blank=True, null=True)
    receptions = models.IntegerField(blank=True, null=True)
    rec_yards = models.IntegerField(blank=True, null=True)
    yards_per_rec = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)
    rec_tds = models.IntegerField(blank=True, null=True)

    # TWO PT Conversions
    two_pt_conv_made = models.IntegerField(blank=True, null=True)
    # td_every_type = models.IntegerField(blank=True)
    # pts_every_type = models.IntegerField(blank=True)

    # PUNT RETURN STATS
    # Rt    Yds    Y/Rt    TD
    punt_returns = models.IntegerField(blank=True, null=True)
    pr_yards = models.IntegerField(blank=True, null=True)
    yards_per_punt_return = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)
    pr_tds = models.IntegerField(blank=True, null=True)

    # KICKOFF RETURN STATS
    # Ret    Yds    Y/R    TD
    kickoff_returns = models.IntegerField(blank=True, null=True)
    kr_yards = models.IntegerField(blank=True, null=True)
    yards_per_kick_return = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)
    kr_tds = models.IntegerField(blank=True, null=True)

    # PUNTING stats
    # punts = models.IntegerField(blank=True)
    # punt_yards = models.IntegerField(blank=True)
    # yards_per_punt = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    # times_punt_blocked = models.IntegerField(blank=True)

    # Total fantasy points
    game_ff_pts = models.IntegerField()

    def save(self, *args, **kwargs):
        super(GameModel, self).save(*args, **kwargs)

