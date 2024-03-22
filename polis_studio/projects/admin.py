from django.contrib import admin
import projects.models as models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'year',
    )

    search_fields = (
        'name',
        'year',
    )

    empty_value_display = '-'


@admin.register(models.ProjectCard)
class ProjectCardAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'project',
    )

    search_fields = (
        'project',
    )

    empty_value_display = '-'


@admin.register(models.Bluprint)
class BlueprintAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )

    search_fields = (
        'name',
    )

    empty_value_display = '-'


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )

    search_fields = (
        'name',
    )

    empty_value_display = '-'
