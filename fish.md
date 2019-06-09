We are given following image

![](./data/fish.jpg)

```
$ strings fish.jpg | tail
.$iw<
W7sG
~v>/|H
Oh C
:UgJ\
$:$1
O'#Z
QU$K
B5%Go
bobross63
```
Hmmm, what is `bobross63`? A key, a password, or something else? Well image shows twitch user fishy150, so I went looking about it, but was a dead end.
What else? I tried steghide and it worked.
```
$ steghide extract -sf fish.jpg 
Enter passphrase: 
wrote extracted data to "flag.txt".

$ cat flag.txt
hsctf{fishy_fishy_fishy_fishy_fishy_fishy_fishy123123123123}
```
