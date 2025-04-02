from django.shortcuts import render, redirect
from time import gmtime, strftime
from datetime import datetime, timedelta
import pytz


def root(request):
    return render(request, 'root.html')

def fetch(request):
    local_tz = request.POST["c_tz"]
    data = pytz.timezone(local_tz)
    time = datetime.now(data)
    rd_time = str(time.strftime("%b, %d %Y %I:%M %p"))
    request.session["time"] = rd_time
    return redirect("/")