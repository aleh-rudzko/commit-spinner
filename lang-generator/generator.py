import json
import sys
from interpreter import Interpreter


class Generator(object):
    def __init__(self, lang_name):
        self.lang_opts = json.load(open('languages/{0}.json'.format(lang_name)))

    def get_interpreter(self):
        return Interpreter(self.lang_opts)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            with open(sys.argv[2], "r") as f:
                generator = Generator(sys.argv[1])
                interpreter = generator.get_interpreter()
                interpreter.evaluate(f.read())
        except IOError as e:
            print e
    else:
        print "\n    USAGE ERROR"
