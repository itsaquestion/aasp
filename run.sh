#!/usr/bin/bash
python --daemongunicorn -w  wsgi:app
