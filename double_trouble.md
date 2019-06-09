So we are given two similar images.

![](./data/koala.png) ![](./data/koala2.png)

Using zsteg on first image gives us a url.
```
$ zsteg -l 0 koala.png
...
b1,rgb,msb,xy       .. text: "_UL~T!yy>"
b1,bgr,lsb,xy       .. text: "<https://www.mediafire.com/file/0n67qsooy8hcy30/hmmm.txt/fileA"
b1,bgr,msb,xy       .. text: ">bT)Q#5."
...
```
From the url, we get a txt [file](./data/hmmm.txt).
```
$ file hmmm.txt
hmmm.txt: GPG symmetrically encrypted data (AES cipher)
```
Nice, so we know now hmmm.txt is encrypted with GPG. We need the key. Lets check other image.
```
$ zsteg -l 0 koala2.png
...
b1,rgb,msb,xy       .. text: "_UL~T!yy>"
b1,bgr,lsb,xy       .. text: "passkey: whatdowehavehereJo"
b1,bgr,msb,xy       .. text: ">bT)Q#5."
...
```
We were told to remove last two characters from the key.
```
$ echo "whatdowehavehere" | gpg -d hmmm.txt 
gpg: AES encrypted data
gpg: encrypted with 1 passphrase
hsctf{koalasarethecutestaren'tthey?}
```
