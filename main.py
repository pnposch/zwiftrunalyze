<<<<<<< HEAD
import sys
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 10:21:16 2020

@author: pnp
"""
>>>>>>> origin/main
import json
import os.path
import requests
import pandas as pd
<<<<<<< HEAD
from datetime import datetime
from zwift import Client # pip install zwift-client
from zrconfig import * #zwiftuser, zwiftpwd and runtoken are specified in the config file

# Initialize Client
client = Client(zwiftuser, zwiftpwd)
profile = client.get_profile()
activities = client.get_activity(profile.profile["id"])
act = activities.list()

# Import only after importdate
if len(sys.argv)>1:
    importdate = pd.to_datetime(sys.arg[1])
else:
    importdate = pd.to_datetime(datetime.now())

for a in act:
    if pd.to_datetime(a["endDate"]).tz_convert(None) > importdate:
        print("Activity ended after set importdate. Skipping.")
        continue
    
=======

from zwift import Client
from appconf import *

#zwiftuser, zwiftpwd and runtoken are specified in the config file


client = Client(zwiftuser, zwiftpwd)
profile = client.get_profile()


activities = client.get_activity(profile.profile["id"])
act = activities.list()

for a in act:
>>>>>>> origin/main
    link = "https://" + a["fitFileBucket"] + ".s3.amazonaws.com/"  + a["fitFileKey"]
    fname = "data/" + pd.to_datetime(a["endDate"]).strftime("%Y%m%d_%H%M%S")

    if os.path.isfile(fname+".fit"):
<<<<<<< HEAD
        print("Already downloaded. Skipping")
        continue

    print("Processing: " + a["name"] + " - Date: " \
          + pd.to_datetime(a["endDate"]).strftime("%Y-%m-%d") \
              + " - " + str(a["distanceInMeters"]/1000) + "km")
=======
        print("Already downloades...skipping")
        continue

    print("Processing " + a["name"])
>>>>>>> origin/main
    # Save Fit File
    res = requests.get(link)
    with open(fname+".fit", "wb") as f:
        f.write(res.content)
    if runtoken:
        r = requests.post("https://runalyze.com/api/v1/activities/uploads", files={'file': open(fname+".fit","rb")}, headers={"token": runtoken})
        print(r.text)
    # Save Desc Data as Json
    with open(fname+"_desc.json", "w") as f:
        json.dump(a, f)