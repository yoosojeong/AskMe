from django.db import models

class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class UserBox(TimeStampedModel):
    message = models.TextField()
    creator = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.message, self.creator)
        
class ReComment(TimeStampedModel):
    reuserbox = models.ForeignKey(UserBox, on_delete=models.CASCADE, null=True)
    remessage = models.TextField()
