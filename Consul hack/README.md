Consul RE challenge
-------------------

xxxx$./consul
Poor Bernie.


here the main function is
Dump of assembler code for function main:
   0x0000000000400b3d <+0>:	push   rbp
   0x0000000000400b3e <+1>:	mov    rbp,rsp
   0x0000000000400b41 <+4>:	sub    rsp,0x10
   0x0000000000400b45 <+8>:	mov    DWORD PTR [rbp-0x4],edi
   0x0000000000400b48 <+11>:	mov    QWORD PTR [rbp-0x10],rsi
   0x0000000000400b4c <+15>:	mov    edi,0x400c11
   0x0000000000400b51 <+20>:	call   0x4004e0 <puts@plt>
   0x0000000000400b56 <+25>:	mov    eax,0x0
   0x0000000000400b5b <+30>:	leave  
   0x0000000000400b5c <+31>:	ret    
End of assembler dump.
here the only call is going to puts,so i tryed to display the other functions in ida.

x00000000004004f0  strlen@plt
0x0000000000400500  printf@plt
0x0000000000400510  __libc_start_main@plt
0x0000000000400520  malloc@plt
0x0000000000400530  usleep@plt
0x0000000000400540  _start
0x000000000040056c  call_gmon_start
0x0000000000400590  deregister_tm_clones
0x00000000004005c0  register_tm_clones
0x0000000000400600  __do_global_dtors_aux
0x0000000000400620  frame_dummy
0x000000000040064c  sub_43E8
0x00000000004006c0  sub_41F2
0x0000000000400738  sub_9F36
0x00000000004007b0  sub_198A
0x0000000000400828  c4
0x0000000000400874  c1
0x0000000000400892  c1_
0x00000000004008ef  c2
0x0000000000400925  c3
0x00000000004009b3  c5
0x0000000000400a09  c8
0x0000000000400a3a  c55
0x0000000000400a77  dont_call_me
0x0000000000400ab2  fake_help
0x0000000000400ad9  real_help
0x0000000000400b16  help

i tryed going thrugh the functions using
  set $pc=0xxxxxxx


As i went through the function real_help(as it seemed helpfull)
 i got a string which says -
"Leonardo De Pisa? Who's that–The next president?" 
this string was made using another string :
"?XbaTeWb\023\067X\023C\\fT2\023J[b\032f\023g[Tg\325s\206G[X\023aXkg\023ceXf\\WXag2"

   0x400699 <sub_43E8+77>:	add    eax,ecx            
   0x40069b <sub_43E8+79>:	mov    BYTE PTR [rdx],al

eax has'\r'(13),ecx(each letter of string)

python:

x='"?XbaTeWb\023\067X\023C\\fT2\023J[b\032f\023g[Tg\325s\206G[X\023aXkg\023ceXf\\WXag2"'
y=[]
>>> for i in range(len(x)):
...     y.append(chr(ord(x[i])+13))
>>> print(''.join(y))
Leonardo De Pisa? Who's that-The next president?


this when googled gives the info about "FIBONACCI NUMBER"

this when realted to the functions in this binary reminds us of functions c1,c1_...c8
when arranged gives the fibonacci series:
c1
c1_
c2
c3
c5
c8

so i tryed calling each function in the order but as soon as i reached c8() gives segmentation fault error

   0x0000000000400a0a <+1>:	mov    rbp,rsp
   0x0000000000400a0d <+4>:	mov    eax,DWORD PTR [rip+0x20094d]        # 0x601360 <mem>
   0x0000000000400a13 <+10>:	add    eax,0x9
   0x0000000000400a16 <+13>:	mov    DWORD PTR [rip+0x200944],eax        # 0x601360 <mem>
   0x0000000000400a1c <+19>:	mov    edi,0x601280
   0x0000000000400a21 <+24>:	call   0x400738 <sub_9F36>                                   //the function terminates as error


inside the function:sub_9F36
   0x0000000000400741 <+9>:	mov    QWORD PTR [rbp-0x28],rdi
   0x0000000000400745 <+13>:	mov    rbx,QWORD PTR [rip+0x200c1c]        # 0x601368 <m0>
   0x000000000040074c <+20>:	mov    rax,QWORD PTR [rbp-0x28]
   0x0000000000400750 <+24>:	mov    rdi,rax
   0x0000000000400753 <+27>:	call   0x4004f0 <strlen@plt>
   0x0000000000400758 <+32>:	mov    rdi,rax
   0x000000000040075b <+35>:	call   rbx                                                  //this is function responsible for termination


at <sub_9F36+13>rbx gives input by function  m0 which is supposed to contain a address as it wont call to any adress as it was suposed to give it an address
so we need to find the function were m0 is being assigned with an adress

So i checked the remaining functions using ida and found that c55 does this task

```
   0x0000000000400a3e <+4>:	sub    rsp,0x10
   0x0000000000400a42 <+8>:	mov    DWORD PTR [rbp-0x4],0x0
   0x0000000000400a49 <+15>:	jmp    0x400a64 <c55+42>
   0x0000000000400a4b <+17>:	mov    eax,0x0
   0x0000000000400a50 <+22>:	call   0x400828 <c4>
   0x0000000000400a55 <+27>:	mov    edi,0x64
   0x0000000000400a5a <+32>:	mov    eax,0x0
   0x0000000000400a5f <+37>:	call   0x400530 <usleep@plt>
   0x0000000000400a64 <+42>:	cmp    DWORD PTR [rbp-0x4],0xe
   0x0000000000400a68 <+46>:	jle    0x400a4b <c55+17>
   0x0000000000400a6a <+48>:	mov    QWORD PTR [rip+0x2008f3],0x400520        # 0x601368 <m0>
   0x0000000000400a75 <+59>:	leave  
   0x0000000000400a76 <+60>:	ret    
```
in this function <c55+48> instrtruction provides the adress needed for m0..
but due to line <+46> it does not reach the required position and hence acts as an infinit loop.
This is where i tryed patching
by changing jle to jge using:
$disass 0x400a68,0x400a69
```
Dump of assembler code from 0x400a68 to 0x400a69:
   0x0000000000400a68 <c55+46>:	jle    0x400a4b <c55+17>
End of assembler dump.
````
gdb-peda$  set *(char*)0x400a68 = 0x7d
Changed to :

````
gdb-peda$ disass 0x400a68,0x400a69
Dump of assembler code from 0x400a68 to 0x400a69:
   0x0000000000400a68 <c55+46>:	jge    0x400a4b <c55+17>
End of assembler dump.
```
This alowed me to exit the infinite loop to the line<+48>

Then again i tryed to go through all function in sequence and reached c8, where i passed the segmentation error

````
  0x400a1c <c8+19>:	mov    edi,0x601280
   0x400a21 <c8+24>:	call   0x400738 <sub_9F36>
=> 0x400a26 <c8+29>:	mov    rsi,rax
   0x400a29 <c8+32>:	mov    edi,0x400c0c
   0x400a2e <c8+37>:	mov    eax,0x0
When we exit from <sub_9F36> gives:
RAX: 0x602260 ("flag{write_in_bernie!}")

````
Hence flag: flag{write_in_bernie!}
  
 

 
