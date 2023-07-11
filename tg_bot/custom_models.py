from django import forms
from datetime import time
from django.db import models


class CustomTimeField(models.Field):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = [(time(hour=h), '{:02d}:00'.format(h)) for h in range(11, 20)]
        kwargs['default'] = time(hour=11)
        kwargs['max_length'] = 5
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return value

    def to_python(self, value):
        if isinstance(value, time):
            return value
        if value is None:
            return value
        if isinstance(value, str):
            return time.fromisoformat(value)
        return time(hour=value)

    def get_prep_value(self, value):
        if value is None:
            return value
        return value.strftime('%H:%M:%S')

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.TimeField}
        defaults.update(kwargs)
        return super().formfield(**defaults)
