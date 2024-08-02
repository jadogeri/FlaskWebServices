import math as Math
import sys 
from os.path import dirname, abspath

from flask import request
dir = dirname(dirname(abspath(__file__)))
print("absolute path === ",dir)

sys.path.append(dir)
from app import *  

#Returns number of minutes from seconds, 1 minute = 60 seconds
@app.route('/time/secondsToMinutes')
def secondsToMinutes(seconds: int):
    try:
        minutes : float;
        minutes = round(seconds / 60,2);
        return str(minutes);

    except Exception as e:
        print(e)
        return "Invalid data in query string", 400

#Returns number of hours from seconds, 1 hour = 60 minutes
@app.route('/time/secondsToHours')
def secondsToHours(seconds: int): 
    try:
        minutes : float;
        hours : float;
        #convert seconds to minutes i.e 1 minute = 60 seconds
        minutes = seconds / 60;    
        #convert minutes to hours    
        hours = round(minutes / 60,2);
        return str(hours);

    except Exception as e:
        print(e)
        return "Invalid data in query string", 400


#Returns number of days from seconds, 1 day = 24 hours
@app.route('/time/secondsToDays')
def secondsToDays(seconds : int): 
    try:
        minutes : float;
        hours : float;
        days : float;
        #convert seconds to minutes 
        minutes = seconds / 60;    
        #convert minutes to hours    
        hours = minutes / 60;
        #convert hours to days  
        days = round(hours / 24,2);
        return str(days);

    except Exception as e:
        print(e)
        return "Invalid data in query string", 400


#Returns number of years from seconds, 1 year = 365 days
@app.route('/time/secondsToYears')
def secondsToYears(seconds : int): 
    try:
        minutes : float;
        hours : float;
        days : float;
        years : float;
        #convert seconds to minutes 
        minutes = seconds / 60;    
        #convert minutes to hours    
        hours = minutes / 60;
        #convert hours to days  
        days = hours / 24;
        #convert days to years
        years = round(days / 365,2);
        return str(years);

    except Exception as e:
        print(e)
        return "Invalid data in query string", 400


#Returns number of seconds from minutes, 1 minute = 60 seconds
@app.route('/time/minutesToSeconds')
def minutesToSeconds(minutes : float): 
    try:
        seconds : float;
        seconds = minutes * 60;
        return str(seconds);

    except Exception as e:
        print(e)
        return "Invalid data in query string", 400

#Returns number of seconds from hours, 1 hour = 60 minutes
@app.route('/time/hoursToSeconds')
def hoursToSeconds(hours : float):
    try:
        minutes : float;
        seconds : float;
        #convert hours to minutes i.e 60 minutes = i hour
        minutes = hours * 60;    
        #convert minutes to seconds  
        seconds = minutes * 60
        return str(seconds);

    except Exception as e:
        print(e)
        return "Invalid data in query string", 400


#Returns number of seconds from days, 1 day = 24 hours
@app.route('/time/daysToSeconds')
def daysToSeconds(days : float):
    try:
        minutes : float;
        hours : float;
        seconds : float;
        #convert days to hours
        hours = days * 24;    
        #convert hours to minutes   
        minutes = hours * 60;
        #convert minutes to seconds
        seconds = minutes * 60;
        return str(seconds);

    except Exception as e:
        print(e)
        return "Invalid data in query string", 400


#Returns number of seconds from hours, 1 year = 365 days
@app.route('/time/yearsToSeconds')
def yearsToSeconds(years : float): 
    try:
        minutes : float;
        hours : float;
        days : float;
        seconds : float;
        #convert years to days 
        days = years * 365;    
        #convert days to hours    
        hours = days * 24;
        #convert hours to minutes
        minutes = hours * 60;
        #convert minutes to seconds
        seconds = minutes * 60;
        return str(seconds);

    except Exception as e:
        print(e)
        return "Invalid data in query string", 400


