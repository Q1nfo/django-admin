from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from movies.models import FilmWork, PersonRole


class MoviesApiMixin:
    model = FilmWork
    http_method_names = ['get']

    def get_person_array(self, role):
        return ArrayAgg(
            'personfilmwork__person__full_name',
            filter=Q(personfilmwork__role=role),
            distinct=True
        )

    def get_queryset(self):
        values = ('id', 'title', 'description', 'creation_date', 'rating', 'type')
        query = FilmWork.objects.values(*values).annotate(
            actors=self.get_person_array(role=PersonRole.ACTOR),
            directors=self.get_person_array(role=PersonRole.DIRECTOR),
            writers=self.get_person_array(role=PersonRole.WRITER),
            genre=ArrayAgg(
                'genres__name',
                distinct=True
            )
        ).order_by('title')

        return query

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesListApi(MoviesApiMixin, BaseListView):
    """"""

    model = FilmWork
    http_method_names = ('get',)

    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()
        page_size = self.get_paginate_by(queryset)

        paginator, page, queryset, _ = self.paginate_queryset(queryset, page_size)
        context = {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': page.previous_page_number() if page.has_previous() else None,
            'next': page.next_page_number() if page.has_next() else None,
            'results': list(queryset)
        }
        return context


class MoviesDetailView(MoviesApiMixin, BaseDetailView):

    model = FilmWork
    http_method_names = ('get',)
    pk_url_kwarg = 'id'

    def get_context_data(self, *, object_list=None, **kwargs):
        return self.object if self.object else {}
