from django.db import models
from django.utils.text import slugify  # ✅ Import slugify

class Computer(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)  # ✅ Allow blank slugs
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    price = models.FloatField(null=True)
    date_post = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # ✅ Generate slug only if it's empty
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class C_Acer(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)  # ✅ Allow blank slugs
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    price = models.FloatField(null=True)
    date_post = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # ✅ Generate slug only if it's empty
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class C_Asus(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)  # ✅ Allow blank slugs
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    price = models.FloatField(null=True)
    date_post = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # ✅ Generate slug only if it's empty
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class C_Msi(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)  # ✅ Allow blank slugs
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    price = models.FloatField(null=True)
    date_post = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # ✅ Generate slug only if it's empty
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class C_Lenovo(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)  # ✅ Allow blank slugs
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    price = models.FloatField(null=True)
    date_post = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # ✅ Generate slug only if it's empty
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class C_Mac(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)  # ✅ Allow blank slugs
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    price = models.FloatField(null=True)
    date_post = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # ✅ Generate slug only if it's empty
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class C_Mac_A(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)  # ✅ Allow blank slugs
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    price = models.FloatField(null=True)
    date_post = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # ✅ Generate slug only if it's empty
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class C_Mac_B(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)  # ✅ Allow blank slugs
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    price = models.FloatField(null=True)
    date_post = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # ✅ Generate slug only if it's empty
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class C_Mac_C(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)  # ✅ Allow blank slugs
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    price = models.FloatField(null=True)
    date_post = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # ✅ Generate slug only if it's empty
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)