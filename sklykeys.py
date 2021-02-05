#!/usr/bin/python3
# a cli interface for nfctoys libraries
# requires tnp3xxx.py from nfc.toys at:
# https://github.com/nfctoys/nfctoys
#
#
# This software was coded by Toni Cunyat in 2021
# This software is for educational purposes.
# sklykeys.py creates a file that include the keys
# from your skylander copy.
#



import getopt, sys, binascii
import tnp3xxx
argv = sys.argv[1:]


file=None
to_file=None
uid=None
bin_output=None

def generate_keys(uid):
    keysa = []
    for sector in range(0, 16):
        keysa.append(tnp3xxx.calc_keya(uid, sector))
    return keysa

def get_bin_file(filename):
    with open(filename, 'rb') as f:
        content = f.read()
        f.close()
    return content

def write_file(filename,data):
    write_format='wb+' if bin_output is True else 'w+'

    with open(filename, write_format) as f:
        f.write(data)
        f.close()


def get_sectors_ascii(filename):
    content=get_bin_file(filename)
    hexcontent = binascii.hexlify(content).decode("utf-8")
    n = 32
    chunks = [hexcontent[i:i+n] for i in range(0, len(hexcontent), n)]
    return chunks
def get_uid_from_file(filename):
    chunks = get_sectors_ascii(filename)
    return chunks[0][:8]



def generate_signed_ascii(filename):
    chunks=get_sectors_ascii(filename)
    uid=get_uid_from_file(filename)
    keys=generate_keys(uid)
    key=0
    for i in range(0,16):
        sector=4*i+3
        chunks[sector]=keys[i] + chunks[sector][12:]
    return chunks


def print_help():
    print("sklykeys.py a cli interface for tnp3xxx.py library from nfc.toys \n"
          "that allows us to read a copy in binary mode and write in eml format\n"
          "or in binary format\n"
          "  -u uid (6 bytes in hex) prints keys in stdout\n"
          "  -f file read from file (in binary mode)\n"
          "  -t file write to file otherwise to stdout\n"
          "  -b output format binary otherwise in Proxmark emulator format (EML)\n"
          "example: ./sklykeys.py -f spiro.bin -t spiro_keys.bin -b")


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(argv, 'hu:f:t:b',)

    except getopt.GetoptError:

        print('Something went wrong!')
        sys.exit(2)

    for opt,arg in opts:
        if opt in ['-u']:
            uid=arg

        if opt in ['-h']:
            print_help()

        if opt in ['-f']:
            file=arg
        if opt in ['-t']:
            to_file=arg
        if opt in ['-b']:
            bin_output=True

    if uid is not None:

        print("\n".join(generate_keys(uid)))
    elif file is not None:

        data=generate_signed_ascii(file)
        if bin_output is None:
            data = "\n".join(data)
        else:
            data="".join(data)
            data=binascii.unhexlify(data)
            data=bytearray(data)
        if to_file is not None:
            write_file(to_file,data)
        else:
            print(data)
    else:
        print_help()