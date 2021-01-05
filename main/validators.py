from django.core.exceptions import ValidationError


def validate_max_file_size(value):
    if value.file.size > 2097152:  # 2 МБ
        raise ValidationError(
            'Размер файла не должен превышать 2 Мб',
            code='bad_file_size',
        )


def validate_format(value):
    if value.name.split('.')[1].lower() not in ['jpeg', 'jpg']:
        raise ValidationError(
            'Допускается только формат jpg/jpeg',
            code='bad_format',
        )
