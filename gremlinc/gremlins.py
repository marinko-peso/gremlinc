# -*- coding: UTF-8 -*-

# The mighty gremlins.
ZW_JOINER = u'\u200D'
ZW_NON_JOINER = u'\u200C'
ZW_SPACE = u'\u200B'
ZW_NO_BREAK_SPACE = u'\uFEFF'


def convert_txt_to_binary(txt):
    return ' '.join(format(ord(x), 'b') for x in txt)


def convert_binary_to_zwc(binary):
    def map_char(x):
        if x == '1':
            return ZW_JOINER
        elif x == '0':
            return ZW_NON_JOINER
        return ZW_SPACE

    return map(map_char, binary)


def release(txt):
    binary = convert_txt_to_binary(txt)
    gremlins = convert_binary_to_zwc(binary)

    # Lets make some borders around our gremlins.
    gremlins.insert(0, ZW_NO_BREAK_SPACE)
    gremlins.insert(len(gremlins), ZW_NO_BREAK_SPACE)

    return ''.join(gremlins)


def contain(gremlins):
    pass


if __name__ == '__main__':
    print('Currently not supported')
