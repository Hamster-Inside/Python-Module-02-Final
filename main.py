""" Small Script to show if password has leaked """
from password_validators.password_validator import PasswordValidator, ValidationError
from files_manager import FilesManager

current_file = FilesManager()

for password in current_file.get_list_of_passwords():
    validator = PasswordValidator(password)
    try:
        validator.is_valid()
        current_file.add_to_safe_passwords_file(password)
    except ValidationError as error:
        current_file.add_to_unsafe_passwords_file(password)
        print(f'{password} -> {error}')
