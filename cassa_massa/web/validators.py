from django.core.exceptions import ValidationError


# TODO unit test

def validate_only_letters_and_spaces(value):
    for ch in value:
        if not ch.isalpha() and not ch.isspace():
            raise ValidationError('Name must contain only letters')

'''
- check for numbers -> error
- check for only letters - no error
- check for only spaces -> error
- check for letters and numbers - error            
          
'''

'''
unit tests = concrete isolated piece of code
integration test -> integration of coupled piesces of code
'''