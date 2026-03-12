web: sh -c "python bot.py & gunicorn --bind 0.0.0.0:${PORT:-8080} --workers 1 --timeout 120 --log-level debug bot:web"
