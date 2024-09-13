from models_app.models.photo.models import Photo
from utils.constants import VISIBILITY_CHOICES
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501


class ListAuthorPhotoService(ServiceWithResult):
    author = forms.IntegerField()
    status = forms.ChoiceField(choices=VISIBILITY_CHOICES)

    def process(self):
        self.result = Photo.items.filter_by_author(
                author=self.cleaned_data['author']
            ).filter_by_status(
                status=self.cleaned_data['status']
            )
        self.response_status = 200
        return self
