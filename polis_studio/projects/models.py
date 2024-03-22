from django.db import models

import polis_studio.constant_values as constant_values


class Project(models.Model):
    name = models.CharField(
        max_length=constant_values.PROJECT_NAME_MAX_LENGTH,
        unique=True,
        verbose_name='Name',
    )

    slug = models.SlugField(
        max_length=constant_values.PROJECT_SLUG_MAX_LENGTH,
        unique=True,
        verbose_name='Slug',
    )

    info = models.TextField(
        blank=True,
        null=True,
        verbose_name='Info',
    )

    year = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Year',
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Description',
    )


class Image(models.Model):
    file = models.ImageField(
        upload_to='projects/images/',
        verbose_name='Image file',
    )

    name = models.CharField(
        max_length=constant_values.IMAGE_NAME_MAX_LENGTH,
        unique=True,
        verbose_name='Name',
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Description',
    )

    upload_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Upload date',
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Project',
    )


class Bluprint(models.Model):
    file = models.ImageField(
        upload_to='projects/blueprints/',
        verbose_name='Image file',
    )

    name = models.CharField(
        max_length=constant_values.IMAGE_NAME_MAX_LENGTH,
        unique=True,
        verbose_name='Name',
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Description',
    )

    upload_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Upload date',
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='blueprints',
        verbose_name='Project',
    )


class ProjectCard(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='cards',
        verbose_name='Project',
    )

    image = models.ImageField(
        upload_to='projects/card_titles/',
        verbose_name='Title image',
    )
