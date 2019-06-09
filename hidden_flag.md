We are given a [png file](./data/chall.png).
```
$ file chall.png
chall.png: data
$ # hmm, not a png??
$ strings chall.png | tail
hbl<gnv
Znsi
UeiN
mei7xis
_nbl
PnvI
hnv0}ib
i03-?
ible +8-
key is invisible
```
Notice the `key is invisible` at the end? So, our png file has been encrypted. But what's the key? I wasted so much time looking for key hidden somewhere :P, later it struck to me that `key is "invisible"`. Let's check for the simplest and most basic XOR encryption...
```
$ python
>>> with open("chall.png", "rb") as f: data = f.read()
>>> key = "invisible"
>>> padded_key = key * (len(data) // len(key)) + key[:len(data) % len(key)]
>>> xorred = bytearray(x ^ y for x, y in zip(*map(bytearray, [data, padded_key])))
>>> # let's check first few bytes...
>>> print(xorred[:10])
�PNG

>>> # nice, we got our png!
>>> with open("flag.png", "wb") as f: f.write(xorred)
```
![flag.png](./data/flag.png)
