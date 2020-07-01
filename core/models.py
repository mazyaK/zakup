from autoslug import AutoSlugField
from django.db import models
from googletrans import Translator
from mptt.models import MPTTModel, TreeForeignKey
from pytils.translit import slugify
import time


class Category(MPTTModel):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=200, unique=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def save(self, *args, **kwargs):
        parents = list()
        translator = Translator()
        parent = self.parent
        # вытаскиваем всех родителей, тут мы идем снизу-вверх по графу
        while parent is not None:
            parents.append(translator.translate(text=parent.name).text.lower().replace(" ", "-"))
            parent = parent.parent
        # разворачиваем массив чтобы родители были сверху-вниз, а не снизу-вверх
        parents.reverse()
        parent_str = ""
        # если у нас больше 0 родителей, то мы берем весь список и соединяем его '_'.join(список),
        # тип "_" это разделитель
        if len(parents) != 0:
            parent_str = '_'.join(parents) + '_'
        self.slug = parent_str + translator.translate(text=self.name).text.lower().replace(" ", "-") + "-" + str(
            int(time.time()))
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class CategoryImages(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=False, blank=False)
    image = models.ImageField(upload_to='core/categories_img/', blank=True, verbose_name='Подпись')


STATUS = (
    (0, "Not available"),
    (1, "Are available"),
)


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(to=Category)
    status = models.IntegerField(choices=STATUS, default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(max_length=200, unique=True, blank=True, populate_from='name')
    image = models.ImageField(upload_to='core/product_img/', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name


class Feedback(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='feedback')
    name = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'
