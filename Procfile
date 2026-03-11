web: gunicorn --bind 0.0.0.0:$PORT --workers 1 bot:web & python -c "import asyncio; from bot import run_bot_async; asyncio.run(run_bot_async())"
