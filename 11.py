'''
Реализовать разбор двоичного формата данных. 
Данные начинаются с сигнатуры 0x5e 0x51 0x45 0x42, за которой следует структура A. 
Порядок байт: от младшего к старшему. Адреса указаны в виде смещений от начала данных.
'''


from struct import *


FMT = dict(
    int8='b',
    uint8='B',
    int16='h',
    uint16='H',
    uint32='I',
    uint64='Q',
    float='f',
    double='d'
)


def parse(buf, offs, ty):
    calc = calcsize(FMT[ty])
    print(calc)
    return unpack_from(FMT[ty], buf, offs)[0], offs + calc


def parse_a(buf, offs):
    a1_offs, offs = parse(buf, offs, 'uint32')
    a1, a1_offs = parse_b(buf, a1_offs)
    a2 = []
    for _ in range(2):
        val, offs = parse(buf, offs, 'int8')
        a2.append(val)
    a3, offs = parse(buf, offs, 'int8')
    return dict(a1, a2, a3), offs


def parse_b(buf, offs):
    b1, offs = parse(buf, offs, 'float')
    b2, offs = parse(buf, offs, 'uint8')
    b3_offs, offs = parse(buf, offs, 'uint16')
    b3, b3_offs = parse_c(buf, b3_offs)
    b4, offs = parse(buf, offs, 'uint64')
    b5, offs = parse(buf, offs, 'int16')
    b6_offs, offs = parse(buf, offs, 'uint32')
    b6 = []
    for _ in range(2):
        val, offs = parse_g(buf, b6_offs)
        b6.append(val)
    b7_size, offs = parse(buf, offs, 'uint16')
    b7_offs, offs = parse(buf, offs, 'uint32')
    b7 = []
    for _ in range(b7_size):
        val, b7_offs = parse(buf, b7_offs, 'int16')
        b7.append(val)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'int16')
    c2_offs, offs = parse(buf, offs, 'uint16')
    c2, c2_offs = parse_d(buf, c2_offs)
    c3, offs = parse(buf, offs, 'uint32')
    c4, offs = parse(buf, offs, 'uint16')
    return dict(C1=c1, C2=c2, C3=c3, C4=c4), offs


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'uint8')
    d2, offs = parse(buf, offs, 'float')
    d3, offs = parse_e(buf, offs)
    d4, offs = parse(buf, offs, 'int16')
    d5_offs, offs = parse(buf, offs, 'uint32')
    d5, d5_offs = parse_f(buf, d5_offs)
    d6, offs = parse(buf, offs, 'uint16')
    d7, offs = parse(buf, offs, 'float')
    d8, offs = parse(buf, offs, 'int8')
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5, D6=d6, D7=d7, D8=d8), offs


def parse_e(buf, offs):
    e1, offs = parse(buf, offs, 'int8')
    e2, offs = parse(buf, offs, 'uint8')
    e3, offs = parse(buf, offs, 'uint16')
    e4 = []
    for _ in range(3):
        val, offs = parse(buf, offs, 'uint64')
        e4.append(val)
    e5, offs = parse(buf, offs, 'uint8')
    return dict(E1=e1, E2=e2, E3=e3, E4=e4, E5=e5), offs


def parse_f(buf, offs):
    f1, offs = parse(buf, offs, 'float')
    f2, offs = parse(buf, offs, 'double')
    return dict(F1=f1, F2=f2), offs


def parse_g(buf, offs):
    g1, offs = parse(buf, offs, 'uint8')
    g2_size, offs = parse(buf, offs, 'uint32')
    g2_offs, offs = parse(buf, offs, 'uint16')
    g2 = []
    for _ in range(g2_size):
        val, g2_offs = parse(buf, g2_offs, 'int16')
        g2.append(val)
    return dict(G1=g1, G2=g2), offs


def main(buf):
    return parse_a(buf, 5)[0]

buff1 = (b'^QEBx\x00\x00\x00#&\xe4&\x97\xda\xf7<\xb5\xa4\x8e \xecxe\xd0\xbfl\t\xe8'
 b">\xe4\x15\xb6v?\xf2#\x98Y\xc15P\x08T\x1a\xff\xbd\xe8g'\x811\xa3"
 b"\x89\xd2\xdf\x0e\x15\x8a\xe0\xc0\xe9\xfb'\xa4n\x11\x00\x00\x00SvkOY\xbcH"
 b'\xd0\x86\x1d\x00\xa69\x86\xc3\x95f,Or=i+\xb2\x03\x00\x00\x00V\x00y'
 b'\xa0\xcf\xcd\xbdq\x9d\x18\xb9z*\x05\x00\x00\x00c\x00\x95\xd5\x1a\xea/xc\xbf'
 b'2L\x00\n\xaet\x1b\xf3=\x93[:f\\\x00\x00\x00m\x00\x00\x00\x02\x00t'
 b'\x00\x00\x00')

print(main(buff1))
