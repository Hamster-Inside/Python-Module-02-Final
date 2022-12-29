""" Small Script to show if password has leaked """
from password_validators.password_validator import PasswordValidator
import logging

logging.basicConfig(filename=r'Logs\module_02_logs.log', encoding='utf-8', level=logging.INFO)

validator = PasswordValidator('ZAQ!2wsx')

print(validator.is_valid())


