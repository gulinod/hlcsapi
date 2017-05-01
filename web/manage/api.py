from flask_restful import reqparse, Resource
from core.led.control import LedControl
from flask import request
import json


# Create a parse object2
parser = reqparse.RequestParser()

# Add parser
#: First arg - The name in the JSON object
#: Type - not required, only use it if necessary.
#: Help - the message that is raised with the '400 - bad request' message when something fucks up
parser.add_argument('red', required=False, type=int, help='Not a valid color value')
parser.add_argument('green', required=False, type=int, help='Not a valid color value')
parser.add_argument('blue', required=False, type=int, help='Not a valid color value')
parser.add_argument('mode', required=False, help='Not a valid mode')

# Example JSON:
# {
#     red: 255,
#     green: 255,
#     blue: 0,
#     mode: 'solid'
# }

# This should probably come from a better place than here, but it's here for now
led = LedControl()
class BasicColor(Resource):
    def post(self):
        try:
            self._post()
        except Exception as e:
            print("FUCKKKKK, this happened: {}".format(e))
            # return {'error': e}
        return {}

    def _post(self):
        # Parse the args
        print('request data', request.get_data())
        try:
            args = parser.parse_args()
        except Exception as e:
            print("parse error", e.description)
            return

        # print the args for the hell of it


        #print(data)
        print('args', args, '\n')

        # List of errors to return
        errors = []
        for arg in args:

            # the 'and args[arg]' part checks if the value was specified
            # if not, it will be equivalent to None
            if arg in ['red', 'green', 'blue'] and args[arg]:

                print('attempting to set {} to {}'.format(arg, args[arg]))


                try:
                    # color and val are specified for clarity, not necessary
                    led.set_color(color=arg, val=args[arg])
                except ValueError as e:
                    # if value was invalid, ValueError is raised
                    errors.append(str(e))

            if arg in ['mode'] and args[arg]:
                # Try to set mode, append to errors if it fails
                try:
                    # again, mode need not be specified, but done for clarity
                    led.set_mode(mode=args[arg])
                except ValueError as e:
                    print("Could not set mode: {}".format(e))
                    errors.append(str(e))



        # If there was errors, return them, otherwise empty dict
        return {'errors': errors} if errors else {}

    def get(self):

        #create the json with the current color
        data = {"red": led.red, "green": led.green, "blue": led.blue, "mode": "solid" }
        #return the data
        return data
