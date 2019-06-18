from django.db import models

# creates the blog class
class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    # returns title for the admin page
    def __str__(self):
        return self.title

    # first 100 char for the blog homepage
    def summary(self):
        return self.body[:100]

    # formats date
    def pub_date_pretty(self):
        return self.pub_date.strftime('%B %e %Y')

