from django.core.exceptions import ValidationError


# TODO unit test

def validate_only_letters_and_spaces(value):
    # Validating the first and last name use only letters and spaces
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
* test where environment/lang matters ( if django => test in python)

1. unit tests = concrete isolated piece of code
2. integration test -> integration of coupled pieces of code

* tests where environment/lang does not matter

3. api tests - check if the api works correctly
    - cehck if the result of http call returns the correct json
4. Functional e2e/ie tests

* other tests
5.load test
6. performance test
7. security tests
'''