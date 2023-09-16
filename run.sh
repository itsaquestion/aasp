#!/usr/bin/bash
gunicorn --daemon -w 2 wsgi:app