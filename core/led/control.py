

class LedControl:
    def __init__(self, color_vals=None):
        # Set to a dictionary passed in, or default to 0
        self._color_vals = color_vals or {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        # variables prefixed with an '_' are considered private, and should be accessed via a function
        self._modes = ['solid', 'inactive']

    # Create some hackerish ways to get/set color vals in dictionary
    @property
    def green(self):
        return self._color_vals['green']

    @green.setter
    def green(self, x):
        print('setting green to {}'.format(x))
        self._color_vals['green'] = x

    @property
    def red(self):
        return self._color_vals['red']

    @red.setter
    def red(self, x):
        print('setting red to {}'.format(x))
        self._color_vals['red'] = x

    @property
    def blue(self):
        return self._color_vals['blue']

    @blue.setter
    def blue(self, x):
        print('setting blue to {}'.format(x))
        self._color_vals['blue'] = x

    def validate_value(self, val):
        #: Validate that a value is within the allowed
        if val > 255 or val < 0:
            raise ValueError('Value not in allowed range 0-255: {}'.format(val))

    def set_color(self, color, val, extra=None):
        if color not in self._color_vals:
            raise ValueError("Color does not exist: {}".format(color))
        # Validate_value should raise ValueError if incorrect
        self.validate_value(val)
        print('setting color {} to {}'.format(color, val))
        self._color_vals[color] = val

    def set_mode(self, mode):
        if mode not in self._modes:
            raise ValueError("Mode not supported: {}".format(mode))
