from app import *
from models.Geometry import *

@app.route('/')
def server():
   return 'Hello Server'

if __name__ == '__main__':
   app.run()