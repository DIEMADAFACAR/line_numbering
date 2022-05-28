import fileinput
import os

def number_lines(filename, start=1):
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        for n, line in enumerate(file, start=start):
            print(n, line, end='')
    os.unlink(filename + '.bak')
number_lines("C:\\Users\\Artyom hdd\\Desktop\\untitled1\\Test_program.txt")