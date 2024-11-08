import asyncio
import random
from django.db import models  # type: ignore
from nanodjango import Django  # type: ignore

app = Django(
    # Avoid clashes with other examples
    SQLITE_DATABASE="hello_async.sqlite3",
    MIGRATIONS_DIR="hello_async_migrations",
)


@app.admin
class CountLog(models.Model):
    # Standard Django model, registered with the admin site
    timestamp = models.DateTimeField(auto_now_add=True)


@app.route("/async/")
async def view_async(request):
    sleep = random.randint(1, 5)
    await asyncio.sleep(sleep)
    return f"<p>Hello world, async view. You waited {sleep} seconds.</p>"


@app.api.get("/async")
async def api_async(request):
    sleep = random.randint(1, 5)
    await asyncio.sleep(sleep)
    return {
        "saying": f"Hello world, async endpoint. You waited {sleep} seconds.",
        "type": "async",
    }


@app.route("/")
def view_sync(request):
    return "<p>Hello sync world, sync view.</p>"


@app.api.get("/sync")
def api_sync(request):
    return {
        "saying": "Hello world, sync endpoint.",
        "type": "sync",
    }
