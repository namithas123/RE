**Sharp challenge writeup!!**

The challenge is basic challenge involving comparisons of strings

3 main strings are used in this
v14="r0be4t1sn0dspr0p34ly "

v22="12345}iyoom"

v37="lego"
v45="TU\\]uAH%I'aiPQXYpqxyFGNOfoDELMdelm545<=!()08&/-9"

The code:
```
if ( v12 != 95 || v13 != 95 )    //Checking whether 4th and 11th pos is"_"
  {
    puts("Commonsense daa!");
  }
//Then they check the string specifically:
  else
  {

    for ( i = 12; i <= 19; ++i )
    {
      if ( src[i] == *((_BYTE *)&v14 + i) )
        ++v6;
    }
    for ( j = 5; j <= 10; ++j )
    {
      for ( k = 0; k <= 51; ++k )
      {
        v21[j] = src[j] & 0x76;
        v29[j] = v21[j] | 0x69;
        if ( v29[j] == *((_BYTE *)&v22 + j) && src[j] != *((_BYTE *)&v45 + k) )
          ++v6;
      }
    }
    for ( l = 0; l <= 3; ++l )
    {
      v4 = src[l];
      if ( v4 > 96 && v4 <= 122 )
      {
        v5 = v4 + 4;
        if ( v5 > 122 )
          v5 -= 26;
        src[l] = v5;
      }
      if ( src[l] == *((_BYTE *)&v37 + l) )
        ++v6;
    }
    if ( v6 == 324 )
      printf("YO! The flag is - inctf{%s}", &dest);
    else
      puts("Commonsense daa!");
  }
  return 0;
}
```

//1st loop
//Below , the charecters from input[12] is compared with charecters from v14[12],if so v6 is incremented to 8 times
```
for ( i = 12; i <= 19; ++i )
    {
      if ( src[i] == *((_BYTE *)&v14 + i) )
        ++v6;
    }
```
//Hence String from pos 12 to 19 is "pr0p34ly" and v6=8

//2nd loop
```
for ( j = 5; j <= 10; ++j )
    {
      for ( k = 0; k <= 51; ++k )
      {
        v21[j] = src[j] & 0x76;
        v29[j] = v21[j] | 0x69;
        if ( v29[j] == *((_BYTE *)&v22 + j) && src[j] != *((_BYTE *)&v45 + k) )
          ++v6;
      }
    }
```
Here the string from 5th to 10th position of input is evaluated.
Takes in input string ,And it, then or it and pass to v29

Then it checks if v29==v22 along with checking if input!=v45:
So i used this code to find charecters that is not in v45
```
import string
x=string.printable
l1=len(x)
print(x)
fin=[]
j=0
y="TU]uAH%I'aiPQXYpqxyFGNOfoDELMdelm545<=!()08&/-9"
l2=len(y)
for j in range(l1):
	k=0
	for k in range(l2):
		if(x[j]==y[k]):
			break
	if(k==l2-1):
		fin.append(x[j])
print(''.join(fin))	
```
giving:	123679bcghjknrstvwzBCJKRSVWZ"#$*+,.:;>?@[\^_`{|}~
Then i checked manually with:
```
x=input()
y=[]
z=[]
j=0
for j in range (6):
	y.append(chr(ord(x[j])&118))
	z.append(chr(ord(y[j])|105))  
print(''.join(z))

```
To form v22="}iyoom"
giving:"th1gg$" and counting till 52*6 times of v6

now v6=320

//3rd loop
```
    for ( l = 0; l <= 3; ++l )
    {
      v4 = src[l];
      if ( v4 > 96 && v4 <= 122 )
      {
        v5 = v4 + 4;
        if ( v5 > 122 )
          v5 -= 26;
        src[l] = v5;
      }
      if ( src[l] == *((_BYTE *)&v37 + l) )
        ++v6;
    }
```
This function should give v37="lego"
solved this using:
```
v37="lego"
v5=[]
v6=[]
i=0
for i in range(4):
	v5.append(chr((ord(v4[i]) + 4 - 97) % 26 + 97))
	v6.append(chr((ord(v5[i]) -26 - 97) % 26 + 97)) 
print(''.join(v6))
```

giving "hack"
```
THis increments v6 to 324:giving flag here:
   if ( v6 == 324 )
      printf("YO! The flag is - inctf{%s}", &dest);
    else
      puts("Commonsense daa!");
```



Hence Output:YO! The flag is - inctf{hack_th1gg$_pr0p34ly}
