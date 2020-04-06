# RE
**CRACKME**


debugging is done by using IDA , GDB
Let the input be "AAAA"
  
when input is given ecx stores 2 which is compared :

   0x804857b <main+39>:	xor    eax,eax
=> 0x804857d <main+41>:	cmp    DWORD PTR [ecx],0x2
   0x8048580 <main+44>:	je     0x80485ae <main+90>
   0x8048582 <main+46>:	xor    eax,eax

Furthur another string is stored to the stack
   0x80485ba <main+102>:	mov    DWORD PTR [ebp-0x94],eax
   0x80485c0 <main+108>:	mov    DWORD PTR [esp+0x8],0x1f
=> 0x80485c8 <main+116>:	mov    DWORD PTR [esp+0x4],0x8048910
   0x80485d0 <main+124>:	mov    eax,DWORD PTR [ebp-0x94]
  
  where 0x8048910:"_0cGj35m9V5T3Ç8CJ0À9H95h3xdh"
  let it be string1

 string 1 stored in edx is moved to [ebp-0xa4]
   0x80485e4 <main+144>:	mov    DWORD PTR [ebp-0xa4],edx
   0x80485ea <main+150>:	mov    DWORD PTR [ebp-0xa8],0x0

Further next string is pushed onto the stack
=> 0x804861c <main+200>:	mov    DWORD PTR [esp+0x8],0xd
   0x8048624 <main+208>:	mov    DWORD PTR [esp+0x4],0x804892f
   
  where 0x804892f:_Celebration
  let it be string 2

Furthur we can see that changes are made in string1
the stack pinter is moved to the point and then the changes are made there.

0x0804863a <+230>:	mov    eax,DWORD PTR [ebp-0x94]   
   0x08048640 <+236>:	add    eax,0x5                   
   0x08048643 <+239>:	mov    BYTE PTR [eax],0x63                //changing string1[5] to c
   0x08048646 <+242>:	mov    eax,DWORD PTR [ebp-0x94]
   0x0804864c <+248>:	add    eax,0x16                           //removing elements after eax[16]
   0x0804864f <+251>:	mov    BYTE PTR [eax],0x0
The changed string is stored in [ebp-0x94]
input stored in  [esp+0x4]
STRING1:"_0cGjc5m9V5T3Ç8CJ0À9"


again string1 is changed
   0x08048676 <+290>:	mov    eax,DWORD PTR [ebp-0x94]
=> 0x0804867c <+296>:	add    eax,0x8
   0x0804867f <+299>:	mov    BYTE PTR [eax],0x5f                //changing string1[8] to '_'
   0x08048682 <+302>:	mov    eax,DWORD PTR [ebp-0x94]
   0x08048688 <+308>:	add    eax,0x9
   0x0804868b <+311>:	mov    BYTE PTR [eax],0x2e                //changing string[9]  to '.'
STRING1:"_0cGjc5m_.5T3Ç8CJ0À9"

0x0804868e <+314>:	mov    edx,DWORD PTR ds:0x804a038
The address of the function is given to edx where it is :
In IDA:
mov     edx, ds:function_ptr_217  


the function is WPA:
Dump of assembler code for function WPA:
   0x080486c4 <+0>:	push   ebp
   0x080486c5 <+1>:	mov    ebp,esp
   0x080486c7 <+3>:	sub    esp,0x8
   0x080486ca <+6>:	mov    eax,DWORD PTR [ebp+0xc]
   0x080486cd <+9>:	add    eax,0xb
   0x080486d0 <+12>:	mov    BYTE PTR [eax],0xd
   0x080486d3 <+15>:	mov    eax,DWORD PTR [ebp+0xc]
   0x080486d6 <+18>:	add    eax,0xc
   0x080486d9 <+21>:	mov    BYTE PTR [eax],0xa
   0x080486dc <+24>:	mov    DWORD PTR [esp],0x804893c
   0x080486e3 <+31>:	call   0x804846c <puts@plt>
   0x080486e8 <+36>:	mov    eax,DWORD PTR [ebp+0xc]
   0x080486eb <+39>:	mov    DWORD PTR [esp+0x4],eax
   0x080486ef <+43>:	mov    eax,DWORD PTR [ebp+0x8]
   0x080486f2 <+46>:	mov    DWORD PTR [esp],eax
   0x080486f5 <+49>:	call   0x804847c <strcmp@plt>
   0x080486fa <+54>:	test   eax,eax
   0x080486fc <+56>:	jne    0x804870f <WPA+75>
   0x080486fe <+58>:	call   0x804872c <blowfish>
   0x08048703 <+63>:	mov    DWORD PTR [esp],0x0
   0x0804870a <+70>:	call   0x804848c <exit@plt>
   0x0804870f <+75>:	call   0x8048803 <RS4>
   0x08048714 <+80>:	mov    DWORD PTR [esp],0x8048964
   0x0804871b <+87>:	call   0x804846c <puts@plt>
   0x08048720 <+92>:	mov    DWORD PTR [esp],0x1
   0x08048727 <+99>:	call   0x804848c <exit@plt>
End of assembler dump.


   0x080486a4 <+336>:	call   edx \\calls to fuctn WPA 
 
which in IDA:
void __cdecl __noreturn WPA(char *s1, char *s2)
{
  s2[11] = 13;
  s2[12] = 10;
  puts(s);
  if ( !strcmp(s1, s2) )
    blowfish();
  RS4();
}


HERE :
2 arguments are taken as 
1:String1
2:input

   0x80486ca <WPA+6>:	mov    eax,DWORD PTR [ebp+0xc]
=> 0x80486cd <WPA+9>:	add    eax,0xb                            '\r'
   0x80486d0 <WPA+12>:	mov    BYTE PTR [eax],0xd
   0x80486d3 <WPA+15>:	mov    eax,DWORD PTR [ebp+0xc]
   0x80486d6 <WPA+18>:	add    eax,0xc                          
   0x80486d9 <WPA+21>:	mov    BYTE PTR [eax],0xa                 '\n'  

changes the string to :"_0cGjc5m_.5\r\nÇ8CJ0À9"

=> 0x80486eb <WPA+39>:	mov    DWORD PTR [esp+0x4],eax
   0x80486ef <WPA+43>:	mov    eax,DWORD PTR [ebp+0x8]
   0x80486f2 <WPA+46>:	mov    DWORD PTR [esp],eax
THe changed string1 and input is being moved to stack to get compared by function <strcmp@plt>

if the input is string1 then it gives positive o/p else it exploads



HENCE:
The input to be given is _0cGjc5m_.5\r\nÇ8CJ0À9"
 [But as '\r' and '\n' are escape charecters '\' are not read]

 So the input to be given is :"_0cGjc5m_.5$'\r'$'\n'Ç8CJ0À9"


      giving o/p:
Vérification de votre mot de passe..
'+) Authentification réussie...
 U'r root! 

 sh 3.0 # password: liberté!


 sh 3.0 # password: liberté!

  
