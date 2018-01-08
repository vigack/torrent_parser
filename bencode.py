import binascii
from deben import decode


def parse_torrent(path):
    with open(path, 'rb') as bt:
        data = bt.read()
        binary_torrent = decode(data)[0]
        encoding = binary_torrent[b'encoding'].decode()
        return b2s(binary_torrent, encoding)


def b2s(tar, encoding):
    if type(tar) is list:
        return b2s_list(tar, encoding)
    elif type(tar) is dict:
        return b2s_dict(tar, encoding)
    elif type(tar) is bytes:
        return tar.decode(encoding)
    else:
        return tar


def b2s_dict(d, encoding):
    res = {}
    for k, v in d.items():
        if k != b'pieces':
            res[k.decode(encoding)] = b2s(v, encoding)
        else:
            res[k.decode(encoding)] = [binascii.hexlify(v[i:i+20]).decode() for i in range(0, len(v), 20)]
    return res


def b2s_list(lst, encoding):
    res = []
    for x in lst:
        res.append(b2s(x, encoding))
    return res
