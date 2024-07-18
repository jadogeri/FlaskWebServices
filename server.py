from app import *
from models.Geometry import *

@app.route('/')
def server():
   return 'Hello Server'

if __name__ == '__main__':
   # Development 
   # app.run(debug=True)

   # Production
   from waitress import serve
   serve(app, host="0.0.0.0", port=8080)
