# zwiftrunalyze
Download FIT files from Zwift and upload to runanalyze. Simple as that.

Zwift (www.zwift.com) is a popular virtual reality world for cyclists and runners.
Runalyze (www.runalyze.com) is a privacy-friendly training log with extensive functionality (and its free!)

# Prequisites
- Install zwift-client from https://github.com/sandeepvasani/zwift-client:
``` pip install zwift-client ```
or
``` pip install -r requirements.txt  ```
to include the few other (standard) packages needed.

Alternatively use the Docker config below.
=======

or include the few other (standard) packages needed:
``` pip install -r requirements.txt  ```

- add data directory to your folder ``` mkdir data ```

- Rename ```zrconfig.py.example``` to ``` zrconfig.py ``` and proceed to config (no worries only three infos needed)


# Configure
Add your zwift username, zwift password and obtain a token for runanalyze (https://runalyze.com/settings/personal-api) and entere it too in the header of main.py and you are good to go. 

FIT files are downloaded into /data and pushed to runanalyze, once downloaded there are not requested a second time. Furthermore Zwift info is saved in a JSON file.

# Docker
Use Docker Image with local mounts of data/ and zrconfig.py/

``` docker-compose up -d --build ```

Then start with

``` docker exec zwiftrunalyze_app_1 python3 main.py ```

which can be added to the host system's crontab

``` crontab -e ```

e.g. run every evening at 22:30h:

``` 30 22 * * * docker exec zwiftrunalyze_app_1 python3 main.py ```

# Run locally
Simple: ``` python3 main.py ``` or ```chmod +x main.py ``` and ```./main.py ```.

Optional argument: Download only after date:
``` python3 main.py YYYY-MM-DD ``` will skip any zwift acitivies ended before YYYY-MM-DD
