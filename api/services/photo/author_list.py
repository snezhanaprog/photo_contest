from models_app.models.photo.models import Photo
from utils.constants import VISIBILITY_CHOICES
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from utils.custom_pagination import CustomPagination
from utils.django_service_objects.service_objects.errors import NotFound


class ListAuthorPhotoService(ServiceWithResult):
    author_id = forms.IntegerField()
    status = forms.ChoiceField(choices=VISIBILITY_CHOICES)
    current_page = forms.IntegerField(required=False)
    per_page = forms.IntegerField(required=False)

    custom_validations = ['validate_presence_author']

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self.pagination_photos()
        return self

    @property
    def _photos(self):
        return (
            Photo.items
            .filter_by_author(author=self._author)
            .filter_by_status(status=self.cleaned_data['status'])
        )

    @property
    def _author(self):
        return User.objects.get(id=self.cleaned_data['author_id'])

    def pagination_photos(self):
        per_page = self.cleaned_data.get('per_page') or 3
        current_page = self.cleaned_data['current_page'] or 1

        paginator = Paginator(self._photos, per_page)
        photos_page = paginator.get_page(current_page)
        pagination = CustomPagination(photos_page, current_page, per_page)

        return {
            "pagination": pagination,
            "photos": photos_page
        }

    def validate_presence_author(self):
        if not self._author:
            self.add_error(
                "id",
                NotFound(
                    message=f"Not found user with id = {
                        self.cleaned_data['author_id']}"
                ),
            )
