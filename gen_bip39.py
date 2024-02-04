#!/usr/bin/env python

import hashlib
import sys
from mnemonic import Mnemonic


phrase = ' '.join(sys.argv[1:])
memo = Mnemonic("english")

#validate string
for word in phrase.split(' '):
    try:
        i = memo.wordlist.index(memo.normalize_string(word))
        if i<0:
            raise ValueError("invalid index value")
    except:
        print("word not in dictionary :", word)
        sys.exit(1)




seed = memo.to_seed(phrase, "")

#seed = memo.to_entropy(phrase)

print("Phrase length:", len(sys.argv)-1)
print("Phrase: ",phrase)
print("Seed:", seed.hex())

phrase2 = memo.to_mnemonic(hashlib.sha256(seed).digest())

print("Phrase: ",phrase2)
