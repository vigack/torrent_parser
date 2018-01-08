"""A script to decode bencode string"""

__author__ = 'vigack'


def decode(x):
    return FUNC_MAP[x[0]](x, 0)


def decode_int(x, ptr):
    try:
        end = x.index(101, ptr)
        num = int(x[ptr+1:end])
        return num, end+1
    except ValueError:
        raise UnValidBencodeSourceException


def decode_str(x, ptr):
    try:
        idx = x.index(58, ptr)
        count = int(x[ptr:idx])
        string = x[idx+1:idx+count+1]
        return string, idx+count+1
    except ValueError:
        raise UnValidBencodeSourceException


def decode_list(x, ptr):
    try:
        lst = []
        ptr += 1
        while x[ptr] != 101:
            v, ptr = FUNC_MAP[x[ptr]](x, ptr)
            lst.append(v)
        return lst, ptr + 1
    except ValueError:
        raise UnValidBencodeSourceException


def decode_dict(x, ptr):
    try:
        dct = {}
        ptr += 1
        while x[ptr] != 101:
            key, ptr = decode_str(x, ptr)
            val, ptr = FUNC_MAP[x[ptr]](x, ptr)
            dct[key] = val
        return dct, ptr + 1
    except ValueError:
        raise UnValidBencodeSourceException


FUNC_MAP = {
    105: decode_int,
    108: decode_list,
    100: decode_dict,
    48: decode_str,
    49: decode_str,
    50: decode_str,
    51: decode_str,
    52: decode_str,
    53: decode_str,
    54: decode_str,
    55: decode_str,
    56: decode_str,
    57: decode_str
}


class UnValidBencodeSourceException(Exception):
    def __init__(self, err='Not a valid bencode source!'):
        Exception.__init__(self, err)
