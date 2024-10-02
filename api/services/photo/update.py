from models_app.models.photo.models import Photo
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501
from utils.django_service_objects.service_objects.errors import ValidationError  # noqa: E501
from utils.django_service_objects.service_objects.errors import ForbiddenError  # noqa: E501
from django.contrib.auth.models import User
from utils.django_service_objects.service_objects.errors import NotFound


class UpdatePhotoService(ServiceWithResult):
    id = forms.IntegerField(required=True)
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=500)
    author_id = forms.IntegerField()
    image = forms.FileInput()

    custom_validations = [
        'validate_presence_author',
        'validate_permission',
        'validate_presence_photo',
        'validate_format'
    ]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._update()
        return self

    @property
    def _photo(self):
        return Photo.objects.get(id=self.cleaned_data['id'])

    @property
    def _author(self):
        return User.objects.get(id=self.cleaned_data['author_id'])

    def _update(self):
        obj = self._photo
        obj.title = self.cleaned_data['title']
        obj.description = self.cleaned_data['description']
        obj.old_image = obj.image
        if 'image' in self.data:
            obj.image = self.data['image']
            obj.status = "private"
        obj.save()
        return obj

    def validate_format(self):
        type = ['image/jpeg', 'image/png']
        if 'image' in self.data:
            if self.data['image'].content_type not in type:
                raise ValidationError(
                    "Ошибка типа. Разрешены только JPEG, PNG.")

    def validate_permission(self):
        if self._author != self._photo.author:
            ForbiddenError("Пользователь не имеет прав на изменение")

    def validate_presence_author(self):
        if not self._author:
            self.add_error(
                "id",
                NotFound(
                    message="Not found user with id = " +
                    self.cleaned_data['author_id']
                ),
            )

    def validate_presence_photo(self):
        if not self._photo:
            self.add_error(
                "id",
                NotFound(
                    message="Not found photo with id = " +
                    self.cleaned_data['id']
                ),
            )
