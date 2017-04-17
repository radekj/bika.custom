def validate(self, value, *args, **kwargs):
    if value.isdigit() and len(value) > 3:
        return True
    else:
        return 'Wrong iban'
