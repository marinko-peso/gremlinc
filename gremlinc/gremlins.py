# -*- coding: UTF-8 -*-

# The mighty gremlins.
ZW_JOINER = u'\u200D'
ZW_NON_JOINER = u'\u200C'
ZW_SPACE = u'\u200B'
ZW_NO_BREAK_SPACE = u'\uFEFF'


def _convert_txt_to_binary(txt):
    return ' '.join(format(ord(x), 'b') for x in txt)


def _convert_binary_to_zwc(binary):
    def map_char(x):
        if x == '1':
            return ZW_JOINER
        elif x == '0':
            return ZW_NON_JOINER
        return ZW_SPACE

    return map(map_char, binary)


def release(txt):
    binary = _convert_txt_to_binary(txt)
    gremlins = list(_convert_binary_to_zwc(binary))

    # Lets make some borders around our gremlins.
    gremlins.insert(0, ZW_NO_BREAK_SPACE)
    gremlins.insert(len(gremlins), ZW_NO_BREAK_SPACE)

    return ''.join(gremlins)


def contain(text_with_gremlins):
    if type(text_with_gremlins) is not str:
        raise Exception('Expected input to be a type of string.')
    if text_with_gremlins.count(ZW_NO_BREAK_SPACE) != 2:
        raise Exception('Incorrect gremlins format, missing border characters.')

    binary = []
    bchar = []
    inside = False
    for ch in text_with_gremlins:
        if ch == ZW_NO_BREAK_SPACE:
            if not inside:
                inside = True
                continue
            binary.append(''.join(bchar))
            break

        if ch == ZW_SPACE:
            binary.append(''.join(bchar))
            bchar = []
            continue

        bchar.append('1' if ch == ZW_JOINER else '0')

    return ''.join(map(lambda x: chr(int(x[:8], 2)), binary))


if __name__ == '__main__':
    print('Currently not supported')
