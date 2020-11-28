import sys
import json
import os.path
import requests
import pandas as pd

from datetime import datetime
from zwift import Client  # pip install zwift-client
from zrconfig import zwiftuser, zwiftpwd, runtoken

# Initialize Client
client = Client(zwiftuser, zwiftpwd)
profile = client.get_profile()
activities = client.get_activity(profile.profile["id"])
act = activities.list()

# Import only after importdate
if len(sys.argv) > 1:
    importdate = pd.to_datetime(sys.arg[1])
else:
    importdate = pd.to_datetime(datetime.now())

for a in act:
    if pd.to_datetime(a["endDate"]).tz_convert(None) > importdate:
        print("Activity ended after set importdate. Skipping.")
        continue
    link = "https://" + a["fitFileBucket"] + ".s3.amazonaws.com/" \
           + a["fitFileKey"]

    fname = "data/" + pd.to_datetime(a["endDate"]).strftime("%Y%m%d_%H%M%S")

    if os.path.isfile(fname+".fit"):
        print("Already downloaded. Skipping")
        continue

    print("Processing: " + a["name"] + " - Date: "
          + pd.to_datetime(a["endDate"]).strftime("%Y-%m-%d")
          + " - " + str(a["distanceInMeters"]/1000) + "km")

    # Save Fit File
    res = requests.get(link)
    with open(fname+".fit", "wb") as f:
        f.write(res.content)
    if runtoken:
        r = requests.post("https://runalyze.com/api/v1/activities/uploads",
                          files={'file': open(fname+".fit", "rb")},
                          headers={"token": runtoken})
        print(r.text)
    # Save Desc Data as Json
    with open(fname+"_desc.json", "w") as f:
        json.dump(a, f)
