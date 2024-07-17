import math as Math
import sys 
from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))
print("absolute path === ",dir)

sys.path.append(dir)
from app import *  



@app.route('/getAreaRectangle')
def getAreaRectangle( width : float, length : float):
    area : float;
    area = width * length;
    return area;

@app.route('/getAreaCircle')
def getAreaCircle( radius : float):
    area : float;
    area = 0.5 * round(Math.pi,2) * radius**2;
    return area;

@app.route('/getAreaTriangle')
def getAreaTriangle( base : float, height : float):
    area : float;
    area = 0.5 * base * height;
    return area;

@app.route('/getPerimeterRectangle')
def getPerimeterRectangle( width : float, length : float):
    perimeter : float;
    perimeter = 2 * ( width + length );
    return perimeter;

@app.route('/getPerimeterCircle')
def getPerimeterCircle( radius : float):
    perimeter : float;
    perimeter = 2 * round(Math.pi,2) * radius;
    return perimeter;

@app.route('/getPerimeterTriangle')
def getPerimeterTriangle( side1 : float, side2 : float, side3 : float):
    perimeter : float;
    perimeter = side1 + side2 + side3;
    return perimeter;

@app.route('/test')
def getTest( ):
    
    return "hello test king jay";
