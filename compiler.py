from base64 import b64encode
from gzip import compress
from marshal import dumps
 
def convert(filename):
    with open(filename, 'r') as f:
        codestring=b64encode(compress(dumps(compile(f.read(), '', 'exec')))).decode('utf-8')
    with open("cp_"+filename,"w") as f:
        f.write('from base64 import b64decode\n')
        f.write('from gzip import decompress\n')
        f.write('from marshal import loads\n')
        f.write(f'exec(loads(decompress(b64decode("{codestring}".encode()))))')
