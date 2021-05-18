# gsoc2021.py
This programmme scrap the GSoC 2021 website (https://summerofcode.withgoogle.com/projects/) and stores the data in a csv file in the following format: Name,Organization,Project
It uses 'requests', 'bs4',and 'selenium' libraries in python.

## Running the programme
1. The programme is written for system having 'Chrome' installed and also, 'chromedriver' must be present on the directory in which the programme is run.
2. On line 13 of the python code, 'SCROLL_PAUSE_TIME' is the time difference (in seconds) between consecutive scrolls. Although, the default value has been put after testing few cases, it should be modified by user depending upon internet speed. A slower internet connection user may increase the 'SCROLL_PAUSE_TIME'.
3. Then, one can procced to run the code in the terminal. It may take about 15 minutes to execute.

## What you get
1. The data will be written in a csv file named 'gsoc2021.csv' in the same directory where the programme is located and run.
2. The data will be written into the csv file in the following format
   Name,Organisation,Project
