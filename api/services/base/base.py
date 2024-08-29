import abc
from contextlib import contextmanager
from django import forms
from django.db import transaction
from django.core.exceptions import ValidationError
from django.forms.forms import DeclarativeFieldsMetaclass
import six


class ServiceMetaclass(abc.ABCMeta, DeclarativeFieldsMetaclass):
    pass


@six.add_metaclass(ServiceMetaclass)
class Service(forms.Form):

    db_transaction = True
    run_post_process = True

    @classmethod
    def execute(cls, inputs, files=None, **kwargs):
        instance = cls(inputs, files, **kwargs)
        instance.service_clean()
        with instance._process_context():
            print(instance.__dict__)
            return instance.process()

    def service_clean(self):
        if not self.is_valid():
            raise ValidationError(self.errors)

    @abc.abstractmethod
    def process(self):
        pass

    @contextmanager
    def _process_context(self):
        if self.db_transaction:
            with transaction.atomic():
                if self.run_post_process:
                    transaction.on_commit(self.post_process)
                yield
        else:
            yield
            if self.run_post_process:
                self.post_process()

    def post_process(self):
        pass
