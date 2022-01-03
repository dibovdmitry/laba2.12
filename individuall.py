#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def to_lat(func):
    def simv(text, chars=' !?'):
        tmp = ''.join(map(lambda x: x if x not in chars else '-', func(text)))
        while '--' in tmp:
            tmp = tmp.replace('--', '-')
        return tmp
    return simv


@to_lat
def alphabet(text):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    return ''.join(map(lambda x: t.get(x, x), text.lower()))


text = input()
print(alphabet(text, chars='?!:;,. '))
