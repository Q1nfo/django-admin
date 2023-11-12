from django.contrib import admin

from .models import FilmWork, Genre, PersonFilmWork, GenreFilmWork, Person


class PersonRoleInline(admin.TabularInline):
    model = PersonFilmWork
    readonly_fields = ['created_at']
    autocomplete_fields = ['person']
    extra = 1


class GenreFilmInline(admin.TabularInline):
    model = GenreFilmWork
    readonly_fields = ['created_at']
    autocomplete_fields = ['genre']
    extra = 1


@admin.register(FilmWork)
class FilmWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'creation_date', 'rating')
    search_fields = ('title', 'description', 'id')
    list_filter = ('type',)
    fields = (
        'title', 'type', 'description', 'creation_date',
        'certificate', 'file_path', 'rating'
    )
    sortable_by = ('title', 'created_at')

    inlines = [
        PersonRoleInline,
        GenreFilmInline
    ]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at',)
    fields = (
        'name', 'description'
    )
    search_fields = ('name',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ('id', 'full_name')
    readonly_fields = ('created_at', 'updated_at',)

    inlines = [
        PersonRoleInline
    ]
