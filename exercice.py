#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    mot_maj = ""
    for i in mot :
        mot_maj += chr(ord(i) - 32)
    return mot_maj


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
