from api import app

if __name__ == '__main__':
    app.run(debug=True)



# # run.py
# from flask import Flask
# from models import *
# from persistence import FileStorage

# app = Flask(__name__)

# # Reload objects from file
# storage = FileStorage()
# storage.reload()

# @app.teardown_appcontext
# def teardown(self):
#     storage.save()

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port='5000')
