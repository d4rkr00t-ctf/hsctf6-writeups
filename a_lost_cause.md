Problem Description:
> Pirate Keith loves cryptography and has protected his treasure with a very annoying caesar shift. He has witten “CGULKVIPFRGDOOCSJTRRVMORCQDZG” on his treasure chest and has left a piece of paper with the following message: “every subsequent letter is shifted one less than the previous.” Knowing this, can you unlock Pirate Keith’s treasure chest?
```
$ python
>>> x = "CGULKVIPFRGDOOCSJTRRVMORCQDZG"
>>> for k in range(26):
...     y = ""
...     shift = k
...     for i in range(len(x)):
...         y += chr((ord(x[i]) + shift) % 26 + 65)
...         shift += 1
...     print(y)

PUJBBNBJANDBNODUMXWXCUXBNCQNV
QVKCCOCKBOECOPEVNYXYDVYCODROW
RWLDDPDLCPFDPQFWOZYZEWZDPESPX
SXMEEQEMDQGEQRGXPAZAFXAEQFTQY
TYNFFRFNERHFRSHYQBABGYBFRGURZ
UZOGGSGOFSIGSTIZRCBCHZCGSHVSA
VAPHHTHPGTJHTUJASDCDIADHTIWTB
WBQIIUIQHUKIUVKBTEDEJBEIUJXUC
XCRJJVJRIVLJVWLCUFEFKCFJVKYVD
YDSKKWKSJWMKWXMDVGFGLDGKWLZWE
ZETLLXLTKXNLXYNEWHGHMEHLXMAXF
AFUMMYMULYOMYZOFXIHINFIMYNBYG
BGVNNZNVMZPNZAPGYJIJOGJNZOCZH
CHWOOAOWNAQOABQHZKJKPHKOAPDAI
DIXPPBPXOBRPBCRIALKLQILPBQEBJ
EJYQQCQYPCSQCDSJBMLMRJMQCRFCK
FKZRRDRZQDTRDETKCNMNSKNRDSGDL
GLASSESAREUSEFULDONOTLOSETHEM
HMBTTFTBSFVTFGVMEPOPUMPTFUIFN
INCUUGUCTGWUGHWNFQPQVNQUGVJGO
JODVVHVDUHXVHIXOGRQRWORVHWKHP
KPEWWIWEVIYWIJYPHSRSXPSWIXLIQ
LQFXXJXFWJZXJKZQITSTYQTXJYMJR
MRGYYKYGXKAYKLARJUTUZRUYKZNKS
NSHZZLZHYLBZLMBSKVUVASVZLAOLT
OTIAAMAIZMCAMNCTLWVWBTWAMBPMU
```
Flag - hsctf{GLASSESAREUSEFULDONOTLOSETHEM}