from struct import *


FMT = dict(
    int8="b",
    uint8="B",
    int16="h",
    int32='i',
    int64='q',
    uint16="H",
    uint32="I",
    uint64="L",
    float="f",
    double="d",
    char='c',
)


def parse(buf, offs, ty):
    calc = calcsize(FMT[ty])
    return unpack_from(FMT[ty], buf, offs)[0], offs + calc


def parse_a(buf, offs):
    a1_size, offs = parse(buf, offs, 'uint16')
    a1_offs, offs = parse(buf, offs, 'uint16')
    a1 = []
    for _ in range(a1_size):
        val, a1_offs = parse(buf, a1_offs, 'char')
        a1.append(val.decode())
    a2, offs = parse(buf, offs, 'int32')
    a3_offs, offs = parse(buf, offs, "uint32")
    a3, a3_offs = parse_b(buf, a3_offs)
    a4, offs = parse_d(buf, offs)
    a5, offs = parse(buf, offs, "int8")
    a6, offs = parse(buf, offs, "float")
    return dict(A1=''.join(a1), A2=a2, A3=a3, A4=a4, A5=a5, A6=a6), offs


def parse_b(buf, offs):
    b1 = []
    for _ in range(7):
        b1_offs, offs = parse(buf, offs, "uint16")
        val, b1_offs = parse_c(buf, b1_offs)
        b1.append(val)
    b2_size, offs = parse(buf, offs, "uint32")
    b2_offs, offs = parse(buf, offs, "uint16")
    b2 = []
    for _ in range(b2_size):
        val, b2_offs = parse(buf, b2_offs, "float")
        b2.append(val)
    b3, offs = parse(buf, offs, "uint16")
    b4, offs = parse(buf, offs, "float")
    b5, offs = parse(buf, offs, "double")
    b6, offs = parse(buf, offs, "int32")
    b7, offs = parse(buf, offs, "float")
    b8, offs = parse(buf, offs, "int16")
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7, B8=b8), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, "uint8")
    c2_size, offs = parse(buf, offs, "uint32")
    c2_offs, offs = parse(buf, offs, "uint16")
    c2 = []
    for _ in range(c2_size):
        val, c2_offs = parse(buf, c2_offs, "uint8")
        c2.append(val)
    return dict(C1=c1, C2=c2), offs


def parse_d(buf, offs):
    d1 = []
    for _ in range(4):
        val, offs = parse(buf, offs, "int32")
        d1.append(val)
    d2, offs = parse(buf, offs, "float")
    d3, offs = parse(buf, offs, 'int64')
    return dict(D1=d1, D2=d2, D3=d3), offs


def main(buf):
    return parse_a(buf, 4)[0]

buff1 = (b'\xd0NUQ\x07\x001\x00?\xb9}\xf4\x83\x00\x00\x00\xc9\x92\xf7\xc9t(Rf'
 b'\xc4\x03\xc93\xf6\xa0j\x9e\x03\xc24\xbe\xcf\xd3\x12\xa6X]\x14\xb3q\x95\xcb1'
 b'\xbffounpki\xc1\xec\xdc@,\x04\x00\x00\x008\x00t\x80\x10\x02\x00\x00\x00C\x00'
 b'\x8e\xb4\x97\x02\x00\x00\x00L\x002\x08\xe2\x02\x00\x00\x00U\x00\xcb"'
 b')\xab\xe7\x04\x00\x00\x00^\x00\xf9\x93\xed\x02\x00\x00\x00i\x00\x7fR'
 b'\xe5\x02\x00\x00\x00r\x00\xb4\xb0\x00?\xdc>\x05\xbf<\x00E\x00N\x00W\x00b'
 b'\x00k\x00t\x00\x02\x00\x00\x00{\x00N\x16Co(\xbd\x84%\x85O\xa0\xf0\xd9'
 b'?6\xb6\x7f\xb1[]s?qM')

print(main(buff1))
