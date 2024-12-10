from django.db import models

class ProgrammingQuestion(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    input_example = models.TextField()
    output_example = models.TextField()
    difficulty = models.CharField(
        max_length=50,
        choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')],
    )

    def __str__(self):
        return self.title
