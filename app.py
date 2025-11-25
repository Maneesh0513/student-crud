from flask import Flask, request, jsonify

app = Flask(__name__)
students = []

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    students.append(data)
    return jsonify({'message': 'Student added'}), 201

@app.route('/students/<int:index>', methods=['PATCH'])
def update_student(index):
    data = request.json
    students[index].update(data)
    return jsonify({'message': 'Student updated'})

@app.route('/students/<int:index>', methods=['DELETE'])
def delete_student(index):
    students.pop(index)
    return jsonify({'message': 'Student deleted'})

if __name__ == '__main__':
    app.run(debug=True)
