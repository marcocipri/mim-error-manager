# -*- coding: utf-8 -*-

"""Main module."""
from flask import Flask, url_for, request, Response, jsonify
import json

app = Flask(__name__)

@app.route('/two_phase_service', methods = ['PUT', 'DELETE'])
def api_echo():
    # action : prepare, confirm, forget 
    action = request.headers.get('action')
    # operation-type : subscribe, delete
    # operation-id
    transaction_id = request.headers.get('transaction-id')
    '''
    python rest_services.py
    curl --header "Content-Type: application/json" \
    --request PUT \
    --data '{ "name": "nameField", "surname": "surname", "email": "new.email@fake.org", "nickname": "nickname", "user-id": "user-id"}'   http://127.0.0.1:5000/two_phase_service
    '''

        #
        # request.is_json 
        # request.get_json()['name']
    headers = {'transaction-id': transaction_id, 
            'action': action
        }
    payload = json.dumps({'status':'0', 'message':'success'})
    return Response(headers=headers, status=200, response=payload , mimetype="application/json")

if __name__ == '__main__':
    app.run()
