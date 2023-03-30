import os
import subprocess
from steno import database as db

def size(file: str):
    cmd = subprocess.Popen(['snow', '-S', file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = cmd.communicate()
    return str(stdout, 'utf-8').split()[-2]
def encode(passwd: str, infile: str, outfile: str, file: str = None, message: str = None):
    if message is not None:
        command = 'snow -C -Q -p "{}" -m "{}" {} {}'.format(passwd, message, infile, outfile)
        os.system(command)
    elif file is not None:
        command = 'snow -C -Q -p "{}" -f {} {} {}'.format(passwd, file, infile, outfile)
        os.system(command)


def decode(passwd: str, file: str):
    cmd = subprocess.Popen(['snow', '-C', '-p', passwd, file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = cmd.communicate()
    return str(stdout, 'utf-8')
