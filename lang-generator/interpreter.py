from collections import defaultdict
import sys


class Interpreter(object):
    def __init__(self, opts):
        self.cells, self.cellptr = [0] * opts['MAX_MEM'], 0
        self.stack, self.level = defaultdict(list), 0
        for key in opts.keys():
            setattr(self, key, opts[key])

    def _push(self, instruction):
        self.stack[self.level].append(instruction)

    def _loop(self):
        while self.cells[self.cellptr] > 0:
            for instruction in self.stack[self.level]:
                if instruction == self.OP_INC:
                    self.cells[self.cellptr] += 1
                elif instruction == self.OP_DEC:
                    self.cells[self.cellptr] -= 1
                elif instruction == self.OP_INCPTR:
                    self.cellptr += 1
                elif instruction == self.OP_DECPTR:
                    self.cellptr -= 1
                elif instruction == self.OP_OUT:
                    sys.stdout.write(chr(self.cells[self.cellptr]))

    def evaluate(self, code):
        code = filter(self.VALID_CHARS.__contains__, code)
        buffer = ''
        print('Code: ', code)
        try:
            for char in code:
                instruction = buffer + char
                print('Instruction: ', instruction)
                print('JMP: ', self.OP_JMP, '; RET: ', self.OP_RET)
                if instruction == self.OP_INC:
                    print('OP_INC')
                    buffer = ''
                    if self.level > 0:
                        self._push(instruction)
                    else:
                        self.cells[self.cellptr] += 1
                elif instruction == self.OP_DEC:
                    print('OP_DEC')
                    buffer = ''
                    if self.level > 0:
                        self._push(instruction)
                    else:
                        self.cells[self.cellptr] -= 1
                elif instruction == self.OP_INCPTR:
                    print('OP_INCPTR')
                    buffer = ''
                    if self.level > 0:
                        self._push(instruction)
                    else:
                        self.cellptr += 1
                elif instruction == self.OP_DECPTR:
                    print('OP_DECPTR')
                    buffer = ''
                    if self.level > 0:
                        self._push(instruction)
                    else:
                        self.cellptr -= 1
                elif buffer == self.OP_JMP:
                    print('OP_JMP')
                    buffer = char
                    self.level += 1
                    self.stack[self.level] = []
                elif buffer == self.OP_RET:
                    print('OP_RET')
                    buffer = char
                    self._loop()
                    self.level -= 1
                elif instruction == self.OP_OUT:
                    print('OP_OUT: ', self.level)
                    buffer = ''
                    if self.level > 0:
                        self._push(instruction)
                    else:
                        sys.stdout.write(chr(self.cells[self.cellptr]))
                else:
                    buffer += char
        except IndexError:
            print "[Error] Segmentation fault at address 0x%08x (maxmem = %s)" % (self.cellptr, len(self.cells))
