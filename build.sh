#!/bin/bash

# Build script for Vercel Django deployment

# Collect static files
python manage.py collectstatic --noinput --clear

echo "✅ Build completed successfully"
