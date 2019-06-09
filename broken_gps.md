We are given a [zip file](./data/input.zip) and following problem description:
> Ella is following a broken GPS. The GPS tells her to move in the opposite direction than the one she should be travelling in to get to her destination, and she follows her GPS exactly. For instance, every time she is supposed to move west, the GPS tells her to move east and she does so. What is the shortest distance between the intended location and actual location? Assume that she moves one unit every time a direction is specified. Round your answer to the nearest whole number and then divide by 26. Discard the quotient (mod 26). Each possible remainder corresponds to a letter in the alphabet. (0=a, 1=b… 25=z).
```
$ unzip input.zip
Archive:  input.zip
   creating: input/
  inflating: input/1.txt             
  inflating: input/10.txt            
  inflating: input/11.txt            
  inflating: input/12.txt            
  inflating: input/2.txt             
  inflating: input/3.txt             
  inflating: input/4.txt             
  inflating: input/5.txt             
  inflating: input/6.txt             
  inflating: input/7.txt             
  inflating: input/8.txt             
  inflating: input/9.txt
```
I quickly wrote a [script](./data/solve.py) for this.
```
$ python solve.py
garminesuckz
```
Flag - hsctf{garminesuckz}
