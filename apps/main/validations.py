from django.core.exceptions import ValidationError
import re


class Validations:
    @staticmethod
    def validate_char_fields(value):
        reg = r"^[a-zA-Z\s]+$"

        if not re.match(reg, value):
            raise ValidationError("Only letters are allowed")
