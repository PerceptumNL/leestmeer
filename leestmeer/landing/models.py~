from django.db import models
from model_utils.managers import InheritanceManager

# Blocks
class BlockHolder(models.Model):
    blocks = models.ManyToManyField('Block')

class Block(models.Model):
    title = models.CharField(max_length=255)
    objects = InheritanceManager()

class TextBlock(Block):
    content = models.TextField()

class ImageBlock(Block):
    source = models.URLField()
    caption = models.TextField()


