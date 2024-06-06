from flask import Flask, jsonify, request
from models.place import Place
from persistence.file_storage import FileStorage

app = Flask(__name__)
storage = FileStorage()
storage.reload()

@app.route('/places', methods=['GET'])
def get_places():
    return jsonify([place.to_dict() for place in storage.all().values() if isinstance(place, Place)])

@app.route('/places', methods=['POST'])
def create_place():
    data = request.get_json()
    place = Place(**data)
    storage.new(place)
    storage.save()
    return jsonify(place.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
