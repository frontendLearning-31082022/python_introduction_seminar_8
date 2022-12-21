# Создайте собственный класс-исключение, обрабатывающий ситуацию деления
# на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.
import re


class ExcepZeroCatcher(Exception):
    @staticmethod
    def check_it(digit):
        if digit == 0:
            raise ExcepZeroCatcher("User inputed second digit - 0")

    def __init__(self, *args):
        self.messsage = args[0] if len(args) > 0 else None

    def __str__(self):
        return f"ExcepZeroCatcher " \
               f"{self.messsage if self.messsage != None else ''}"


def input_digit(positive_only, msg):
    while True:
        print(msg)
        inputed = input()
        check_digit = is_it_digit(inputed)
        if (positive_only and check_digit):
            corrected_input = float(inputed) > -1
        if check_digit:
            break
        print("Input integer again")

    inputed = float(inputed)
    return inputed


def is_it_digit(inputed):
    result = re.findall(r'\D', inputed)
    result = list(filter(lambda x: not (str(x).__eq__("-")), result))
    result = list(filter(lambda x: not (str(x).__eq__(",")), result))
    result = list(filter(lambda x: not (str(x).__eq__(".")), result))

    corrected_input = len(result) == 0
    return corrected_input


if __name__ == '__main__':
    while True:
        dig = input_digit(False, "input first dig")
        dig2 = input_digit(False, "input second dig")

        try:
            ExcepZeroCatcher.check_it(dig2)
            res = dig / dig2
            print(f"Result {res}")
        except ExcepZeroCatcher as errr:
            print(f"Error {errr}. Try again")
