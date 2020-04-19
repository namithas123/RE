#Nasssi
*Mainly involves Patching *
To move furthur in the program , certain instructions are edited
```
set *(char*)0x5555555548bb = 0x7e(from jg to jle)
   0x00005555555548bb <+107>:	jle    0x555555554896 <fun1+70>
```
and
```
set *(char*)0x5555555548c2 = 0x74(from jne to je)
   0x00005555555548c2 <+114>:	je     0x55555555491c <fun1+204>
```

Reached decrypt function with the string 

: cixd{v0r_e4s3_cf6ro3a_7e3_p3o13p}

Reached decrypt function,decrypted to :
````

flag{y0u_h4v3_fi6ur3d_7h3_s3r13s}
````
