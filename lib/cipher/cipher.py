import re

from lib.cipher.case.same import same_checker
from lib.cipher.matrix import Matrix


def split_in_couples(input_value, output):
    if len(input_value) == 0:
        return output

    if len(input_value) == 1:
        output.append(input_value + 'X')
        return output

    output.append(input_value[:2])
    return split_in_couples(input_value[2:], output)


class Cipher:
    def __init__(self, letters, encoders):
        self.encoders = encoders
        self.matrix = Matrix(letters)

    def encode(self, input_value):
        input_value = str.upper(input_value)
        input_value = re.sub(r'[^A-Z]+', "", input_value)

        couples = split_in_couples(input_value, [])

        result = ""
        for couple in couples:
            result += (self.encode_couple(couple))
        return result

    def encode_couple(self, couple):
        process = couple
        for case in self.encoders:
            if case[0](process, self.matrix):
                process = case[1](process, self.matrix)
        return process
