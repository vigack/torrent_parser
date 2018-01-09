def encode(x):
    if type(x) is int:
        return encode_int(x)
    elif type(x) is str:
        return encode_str(x)
    elif type(x) is list:
        return encode_list(x)
    elif type(x) is dict:
        return encode_dict(x)


def encode_int(x):
    return 'i{}e'.format(x)


def encode_str(x):
    return '{}:{}'.format(len(x), x)


def encode_list(x):
    return 'l{}e'.format(''.join([encode(item) for item in x]))


def encode_dict(x):
    return 'd{}e'.format(''.join(encode(key)+encode(val) for key, val in x.items()))



