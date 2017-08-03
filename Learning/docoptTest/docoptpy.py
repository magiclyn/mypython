# -*- coding: utf-8 -*-

"""Usage:
    docoptpy (--diff | --b | --c) <req1> <req2> [--exclude <package>...]
    docoptpy (-h | --help)
Options:
    -h --help --db   asdfsdf....
    --diff        diff.........
    --b        b.........
    --c        c.........
"""


from docopt import docopt
import os
import codecs
import re


BOMS = [
    (codecs.BOM_UTF8, 'utf8'),
    (codecs.BOM_UTF16, 'utf16'),
    (codecs.BOM_UTF16_BE, 'utf16-be'),
    (codecs.BOM_UTF16_LE, 'utf16-le'),
    (codecs.BOM_UTF32, 'utf32'),
    (codecs.BOM_UTF32_BE, 'utf32-be'),
    (codecs.BOM_UTF32_LE, 'utf32-le'),
]

ENCODING_RE = re.compile(b'coding[:=]\s*([-\w.]+)')

class reqirement(object):
    """docstring for reqirement"""
    def __init__(self, r = None):
        super(reqirement, self).__init__()
        self.r = r
        self.lines = []
        if r:
            self.load(r)

    def load(self,filename):
        if os.path.exists(filename):
            with open(filename,'rb') as f:
                datastr = None
                data = f.read()
                for bom,encoding in BOMS:
                    if data.startswith(bom):
                        datastr = data[len(bom):].decode(encoding)
                if datastr is None:
                    for line in data.split(b'\n')[:2]:
                        if line[0:1] == b'#' and ENCODING_RE.search(line):
                            encoding = ENCODING_RE.search(line).groups()[0].decode('ascii')
                            datastr = data.decode(encoding)
                if datastr is None:
                    try:
                        datastr = data.decode('utf-8')
                    except Exception:
                        print("decode error")
                if datastr: 
                    b = datastr.splitlines()
                    self.lines = enumerate(b,start = 1)
                    print("lines len:",len(b))


    def diff(self,req):
        r1 = [x[1] for x in self.lines]
        r2 = [x[1] for x in req.lines]

        resultsr1 = []
        resultsr2 = []

        for s in r1:
            # print(s)
            if s not in r2:
                # print("%s is not i s2" % s)
                resultsr1.append(s)

        for s in r2:
            if s not in r1:
                resultsr2.append(s)
        print("only in r1:\n")
        for r in resultsr1:
            print("%s\n" % r)
        print("-----------------------------\n")
        print("only in r2:\n")
        for r in resultsr2:
            print("%s\n" % r)

def diff(r1,r2):
    req1 = reqirement(r1)
    req2 = reqirement(r2)
    req1.diff(req2)


def main():
    args = docopt(__doc__)
    print(args)
    kwargs = {
        'r1': args['<req1>'],
        'r2': args['<req2>'],
    }
    diff(**kwargs)

if __name__ == '__main__':
    main()