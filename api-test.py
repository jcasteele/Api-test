from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

class Customer(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('userId', required=True)
        parser.add_argument('fname', required=False)
        parser.add_argument('lname', required=True)
        parser.add_argument('city', required=True)
        parser.add_argument('state', required=True)
        parser.add_argument('customer', required=True)
        args = parser.parse_args()

        data = pd.read_csv('customer.csv')

        if args['userId'] in list(data['userId']):
            return {'message': f"'{args['userId']}'' already exists."}, 401
        else:
            new_data = pd.DataFrame({
                'userId': args['userId'],
                'fname': args['fname'],
                'lname': args['lname'],
                'city': args['city'],
                'state': args['state'],
                'customer': args['customer']
                })

            data = pd.read_csv('customer.csv')
            data = data.append(new_data, ignore_index=True)
            data.to_csv('customer.csv', index=False)
            return {'data': data.to_dict()}, 200
    
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userId', required=True)
        args = parser.parse_args()

        data = pd.read_csv('customer.csv')

        if args['userId'] in list(data['userId']):
            data['notes'] = data['notes'].apply(lambda x: ast.literal_eval(x))
            user_data = data[data['userId'] == args['userId']]
            user_data['notes'] = user_data['notes'].values[0].append(args['notes'])
            data.to_csv('customers.csv', index=False)
            return {'data': data.to_dict()}, 200

        else:
            return {'message': f"'{args['userId']} user not found."}, 404

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_arguement('userId', required=True)
        args = parser.parse_args()

        data = pd.read_csv('customer.csv')

        if args['userId'] in list(data['userId']):
            data = data[data['userId'] != args['userId']]

            data.to_csv('customer.csv', index=False)
            return {'data': data.to_dict()}, 200
    
        else:
            return {'message': f"'{args['userId']}' user not found."}, 404

api.add_resource(Customer, '/customer')

if __name__ == '__main__':
    app.run()