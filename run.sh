#!/usr/bin/bash
python --daemon gunicorn -w  wsgi:app
