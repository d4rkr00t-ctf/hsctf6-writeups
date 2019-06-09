We are given a string `KZ6UaztNnau6z39oMHUu8UTvdmq1bhob3CcEFdWXRfxJqdUAiNep4pkvkAZUSn9CvEvPNT5r2zt6JPg9bVBPYuTW4xr8v2PuPxVuCT6MLJWDJp84` and nothing else.
So we have to figure out the encryption ourself.

Our ciphertext consists of alpha-numeric characters, so most probably some base encoding. We know it can't be base32. Searching for encoding bases, I found [this](https://github.com/multiformats/multibase/blob/master/multibase.csv).
So, base58 was new for me... Let's try the two plausible options at the moment - base64 and base58.

Base64 decoding just gives garbage output. Let's check for base58 decoding.

Using this online [tool](https://www.browserling.com/tools/base58-decode) for base58 decoding, we get `Welcome to HSCTF! This is your flag: hsctf{w0w_th1s_1s_my_f1rst_crypt0_chall3ng3?}`. :)
