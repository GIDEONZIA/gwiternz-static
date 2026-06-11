#!/usr/bin/env python3
import os
import sys
import subprocess

# Install dependencies
subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "django", "django-distill"])

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Build static site
from django.core.management import execute_from_command_line
execute_from_command_line(['manage.py', 'distill-local', 'dist/', '--force', '--exclude-staticfiles'])

print("Build complete! dist/ folder ready.")
