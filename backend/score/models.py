from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from score.utils import DIFICULTY_CHOICES


class Player(User):
    uuid = models.UUIDField(
        primary_key=True, unique=True, default=str(uuid4()))
    max_score = models.PositiveIntegerField(
        _("Max Score"), default=0, editable=False)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.max_score = self.scores.aggregate(
            models.Max('score')).get('score__max') or 0
        super(Player, self).save(*args, **kwargs)


class Score(models.Model):
    score = models.PositiveIntegerField(_("score"), default=0)
    player = models.ForeignKey("Player", verbose_name=_(
        "player"), related_name='scores', on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    dificulty = models.CharField(
        _("dificulty"), max_length=6, choices=DIFICULTY_CHOICES,
        null=False, blank=False)

    def __str__(self):
        return f"{self.score} - {self.player.username}"

    def save(self, *args, **kwargs):
        super(Score, self).save(*args, **kwargs)
        # update player max_score
        if self.score > self.player.max_score:
            self.player.save()
