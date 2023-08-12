from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.signing import Signer
from django.core import signing

from cryptography.fernet import Fernet

import os
import logging

class Command(BaseCommand):
    help = '''
        Python Security 2 with Cryptography module and Fernet Symmetric encryption and Django Signing.
    '''

    def add_arguments(self, parser):
        parser.add_argument(
            '--subject_key', type=str, help='The string key to encrypt and decrypt.')
        parser.add_argument(
            '--subject_val', type=str, help='The string value to encrypt and decrypt.')

    def handle(self, *args, **options):
        if options['subject_key'] is None:
            raise ValidationError('Missing required subject_key argument')
        if options['subject_val'] is None:
            raise ValidationError('Missing required subject_val argument')
        print(f'Subject key : {options["subject_key"]}')
        print(f'Subject val : {options["subject_val"]}')
        
        signer = Signer()
        token = signer.sign_object({
            options['subject_key']: options['subject_val'] })
        
        try:
            print(f'Encrypted : {token}')
            original = signer.unsign_object(token)
            print(f'Decrypted : {original}')
        except signing.BadSignature:
            return CommandError('Signing failed.')