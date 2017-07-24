from django.db import models
from django.utils import timezone

# Create your models here.
class PropagandistSlogans(models.Model):
    slogan = models.CharField(max_length=140, blank=True, null=True)

    def __str__(self):
        return self.slogan


class Post(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    summary = models.CharField(max_length=500)
    created_date = models.DateTimeField()
    last_edited = models.DateTimeField()

    def __str__(self):
        return self.title



"""
1. [Jazz plays:] Doopity bap tap, doobidy doo do,
2. Blame it on the boogie,
3. That old chestnut,
4. All my code uses the UK imperial system,
--5. Deep one perfect morning,--
6. Just like honey,
7. Like Mummidalen in summer,
8. from django.huh? import oooohh!,
9. The chemistry between us,
10. Put the kettle on for tea,
11. It can be of use,
12. Like a blue sky and sunshine,

"""