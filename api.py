
from genericpath import exists
from numpy import delete
from config import *



@app.route('/user', methods=['GET'])
def get_User():
    results = []
    if r.exists('user'):
        results = json.loads(r.get('user'))
    else :
        data = User.get_list_user()
        rval = json.dumps(data)
        r.set('user' ,rval)
        results = data
    return jsonify({
        "data": results
    })
@app.route('/update/<int:id>', methods=['PUT'])
def update_user(id):
    query = User.select().where(User.id == id)
    if query.exists():
        try:
            request_data = request.get_json()
            User.update_one_user(id ,request_data['name'], request_data['age'])
            r.delete("user")
            results = User.json(User.get_by_id(id))

            return jsonify({
                "code":0,
                "data": results
            }), 200

        except Exception as e:
             return jsonify({'error': e})


    else :
        return "khong tim thay id "
            




    
if __name__ == "__main__":
    app.run(port=8000, debug=True)

