**Taking OFF Writeup**

Found arguments from gdb from equation :
100b+10a+c=932:
a=3
b=9
c=2
giving "3 9 2 chicken"
When given:
```
$./taking_off 3 9 2 chicken
So you figured out how to provide input and command line arguments.
But can you figure out what input to provide?
Well, you found the arguments, but what's the password?
```

#then found the string :
#ZFOKYO\nMC\\O\nLFKM\n which is found to be xored with 42,
So:
```
x="ZFOKYO\nMC\\O\nLFKM*"
y=[]
for i in range (len(x)):
	y.append(chr(ord(x[i])^42))
print(''.join(y))
```
Prints:"please give flag"

This when given as password gives:
```
Good job! You're ready to move on to bigger and badder rev!
Cannot read flag file.
```
Hence when same process is done on the shell of the CTF give:
actf{th3y_gr0w_up_s0_f4st}
