from django.db import models  # type: ignore
from nanodjango import Django  # type: ignore

from datetime import datetime

app = Django()


@app.admin
class CountLog(models.Model):
    # Standard Django model, registered with the admin site
    timestamp = models.DateTimeField(auto_now_add=True)


class CountLogSchema(app.ninja.Schema):
    # Django Ninja Pydantic schema
    timestamp: datetime

@app.route("/")
def count(request):
    # Standard Django function view
    CountLog.objects.create()
    return f"<p>Number of page loads: {CountLog.objects.count()}</p>"


@app.api.get("/add")
def add(request):
    # Django Ninja API support built in
    CountLog.objects.create()
    return {"count": CountLog.objects.count()}

@app.api.get("/logs", response=list[CountLogSchema])
def logs(request):
    # Django Ninja API support built in
    return CountLog.objects.order_by("-timestamp")

@app.route("/slow/")
async def slow(request):
    import asyncio

    await asyncio.sleep(10)
    return "Async views supported"
