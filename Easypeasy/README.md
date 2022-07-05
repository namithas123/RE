# ECPC_writeup


The challenge is not that easy as it sounds to be.

Here we can see that the program begins with statement
*welcome to easypeasy.*

the Entry Point is 0x401529

The code has many functions and it involves MD5 and SHA functions as hashing of the input is done



At the start while running we can see a function which takes in the input
I went through IDA and found out that there starts a loop from the begining of program that continues 7 times at 0x4015d5
That means the input is being asked 3 times.

Further while going in through function , a function in 0x4016a8 address which had:
```c
 v8 = a3;
  v9 = 0;
  v12 = 0LL;
  v13 = 0LL;
  v11 = 8;
  if ( sub_401DDA((_QWORD *)*a1) != 0 )
  {
    for ( i = 0LL; sub_401DDA((_QWORD *)*a1) > i; ++i )
    {
      v10 = *(_BYTE *)sub_401DFC((_QWORD *)*a1, i);
      if ( v9 )
      {
        v11 = sub_401AD7(v10);
      }
      else if ( i )
      {
        if ( v11 == 8 )
          return 0LL;
        v15 = v10 - 48;
        if ( v15 < 0 || v15 > 9 )
          return 0LL;
        v6 = sub_401E18((_QWORD *)a2) < v12 || *(_QWORD *)sub_401E3E((_QWORD *)a2, v12) != v15;
        if ( v6 )
          return 0LL;
        if ( v11 == 3 )
        {
          v13 += v15;
        }
        else if ( v11 > 3 )
        {
          if ( v11 == 5 )
          {
            v13 -= v15;
          }
          else
          {
            if ( v11 != 7 )
              return 0LL;
            if ( v10 == 48 )
              std::operator<<<std::char_traits<char>>(
                &std::cerr,
                "Warning: Bad things might happen.\nYou are the one to blame\n",
                v5);
            v13 /= v15;
          }
        }
        else
        {
          if ( v11 != 2 )
            return 0LL;
          v13 *= v15;
        }
        ++v12;
        v11 = 8;
      }
      else
      {
        v13 = v10 - 48;
        if ( v13 < 0 || v13 > 9 )
          return 0LL;
        v4 = sub_401E18((_QWORD *)a2) < v12 || *(_QWORD *)sub_401E3E((_QWORD *)a2, v12) != v13;
        if ( v4 )
          return 0LL;
        ++v12;
      }
      v9 ^= 1u;
    }
  }
  v7 = (unsigned __int64)sub_401E18((_QWORD *)a2) > 1 && v11 != 8 || sub_401E18((_QWORD *)a2) != v12;
  if ( v7 )
    return 0LL;
  *v8 = v13;
  return 1LL;
}
```
Thi function decides what the input must be.
the input basically contains numbers and operations.


At the begining of this function , 
 the length of inputed string is checked at:
 ```asm
=> 0x401d72:	call   0x401dda
   0x401d77:	cmp    rax,QWORD PTR [rbp-0x10]
```
at the begining , the first charecter is checked if it is a number or not:
0x401bed:	sub    eax,0x30
 ```asm
 0x401bf0:	cdqe   
   0x401bf2:	mov    QWORD PTR [rbp-0x18],rax
=> 0x401bf6:	cmp    QWORD PTR [rbp-0x18],0x0
   0x401bfb:	js     0x401c04
   0x401bfd:	cmp    QWORD PTR [rbp-0x18],0x9
   0x401c02:	jle    0x401c0e
```
HERE:the hex of input number is being subtracted from 0x30, and then checked: 
v15 = v10 - 48;
        if ( v15 < 0 || v15 > 9 )   //if it is btw 0 and 9
          return 0LL;
then:
```asm
   0x401c12:	mov    rdi,rax
   0x401c15:	call   0x401e18
   0x401c1a:	cmp    rax,QWORD PTR [rbp-0x20]
   0x401c1e:	jb     0x401c3c
```
checks the number of numbers possible in the input(not counting the operators) 

then it compares the number in input with the required number:
````asm
   0x401c2b:	mov    rdi,rax
   0x401c2e:	call   0x401e3e               //returns number to be compared
   0x401c33:	mov    rax,QWORD PTR [rax]
   0x401c36:	cmp    rax,QWORD PTR [rbp-0x18]
````

After checking the first number , it goes to a function which checks ifsecond charecter is +,-,* or /
```c
  v1 = a1 - 40;
  if ( v1 == 3 )
    return 3LL;
  if ( v1 > 3 )
  {
    if ( v1 == 5 )
      return 5LL;
    if ( v1 == 7 )
      return 7LL;
  }
  else if ( v1 == 2 )
  {
    return 2LL;
  }
  return 8LL;
}
```
This returns the respective numbers outside this function to make sure that it is an operator


This cycle continues till the size of particular string is completely checked,


Furthur as we continue in the main,if the string size required is correct we can mov to :
```asm
   0x4016d2:	call   0x4014d9
=> 0x4016d7:	mov    rdx,QWORD PTR [rbp-0x1f0]
   0x4016de:	add    rax,rdx
   0x4016e1:	mov    rdx,QWORD PTR [rax*8+0x6052a0]
   0x4016e9:	mov    rax,QWORD PTR [rbp-0x1f8]
   0x4016f0:	cmp    rdx,rax
   
 ```
the result of the computation is then compared to another value which will help us choose the correct operators for that input string.



After each string, SHA and MD5 is updated by
< _SHA1_Update> and  <_MD5_Update>



i went through each cycle manually 7 times and found the 7 operations to be done:


that is :
```
7+6-3/2
1+4+8
3
9*9
8+4*9
5/6
3*0
```

after giving all the strings , a hash is finally made and then compared with a string already given inside.
If its true:

Giving the output
```
That was easy anyways.
Here is your flag: flag{c0u8a_3dgety7_33hygt_donfos_9uck3d_up_NN}
```
