from models_app.models.photo.models import Photo
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501
from django.core.paginator import Paginator
from utils.custom_pagination import CustomPagination


class ListPhotoService(ServiceWithResult):
    search = forms.CharField(max_length=200, required=False)
    sort = forms.CharField(max_length=50)
    per_page = forms.IntegerField(required=False)
    current_page = forms.IntegerField(required=False)

    def process(self):
        self.result = self.pagination_photos()
        return self

    @property
    def _photos(self):
        return (
            Photo.items.filter_by_status(status='public')
            .search(self.cleaned_data['search'])
            .sort_by_field(self.cleaned_data['sort'])
        )

    def pagination_photos(self):
        per_page = self.cleaned_data.get('per_page') or 3
        current_page = self.cleaned_data.get('current_page') or 1

        paginator = Paginator(self._photos, per_page)
        photos_page = paginator.get_page(current_page)
        pagination = CustomPagination(photos_page, current_page, per_page)

        return {
            "pagination": pagination,
            "photos": photos_page
        }
