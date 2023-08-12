from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.exceptions import ValidationError

from cryptography.fernet import Fernet

import os
import logging

class Command(BaseCommand):
    help = '''
        Python Security with Cryptography module and Fernet Symmetric encryption.
    '''

    def add_arguments(self, parser):
        parser.add_argument(
            '--subject', type=str, help='The string to encrypt and decrypt.')

    def handle(self, *args, **options):
        if options['subject'] is None:
            raise ValidationError('Missing required subject argument')
        print(f'Subject : {options["subject"]}')
        key = Fernet.generate_key()
        f = Fernet(key)
        token = f.encrypt(bytes(options['subject'], 'utf-8'))
        print(f'Encrypted subject : {token}')
        decrypted_token = f.decrypt(token)
        print(f'Decrypted subject : {decrypted_token}')
        