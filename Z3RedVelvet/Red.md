***REd velvet***

The pgm is basic Z3 ... where functions have to be solved.

The input is takes 27 size string where all the letters have to satisfy its specific equation

```
#funct1:
from z3 import *
a1=BitVec('a1',32)
a2=BitVec('a2',32)
a3=BitVec('a3',32)
a4=BitVec('a4',32)
a5=BitVec('a5',32)
a6=BitVec('a6',32)
a7=BitVec('a7',32)
a8=BitVec('a8',32)
a9=BitVec('a9',32)
a10=BitVec('a10',32)
a11=BitVec('a11',32)
a12=BitVec('a12',32)
a13=BitVec('a13',32)
a14=BitVec('a14',32)
a15=BitVec('a15',32)
a16=BitVec('a16',32)
a17=BitVec('a17',32)
a18=BitVec('a18',32)
a19=BitVec('a19',32)
a20=BitVec('a20',32)
a21=BitVec('a21',32)
a22=BitVec('a22',32)
a23=BitVec('a23',32)
a24=BitVec('a24',32)
a25=BitVec('a25',32)
a26=BitVec('a26',32)
a27=BitVec('a27',32)

s=Solver()
#funct1
s.add(a1*2*(a2^a1)-a2==10858)
s.add(a1>85)
s.add(a1<=95)
s.add(a2<=111)

#funct2
s.add(a2%a3==7)
s.add(a3>90)

#funct3
s.add(a3/a4+(a4^a3)==21)
s.add(a3<=99)
s.add(a4<=119)

#funct4
s.add(a5==95)

#funct5
s.add(((a6+a5)^(a5^a6^a5))==225)
s.add(a5>90)
s.add(a6<=89)

#funct6
s.add(a6<=a7)
s.add(a6>85)
s.add(a7>110)
s.add(a8>115)
s.add(((a7+a8)^(a6+a7))==44)
s.add((a7+a8)%a6+a7==161)

#funct7
s.add(a8>=a9)
s.add(a9>=a10)
s.add(a8<=119)
s.add(a9>90)
s.add(a10<=89)
s.add((a8+a10)^(a9+a10)==122)
s.add((a8+a10)%a9+a10==101)


#func8
s.add(a10<=a11)
s.add(a11<=a12)
s.add(a12<=114)
s.add((a10+a11)/a12*a11==97)
s.add((a12^(a10-a11))*a11 ==-10088)

#func9
s.add(a12==a13)
s.add(a13>=a14)
s.add(a14<=99)
s.add(a14+a12*(a14-a13)-a12==-1443)

#func10
s.add(a14>=a15)
s.add(a15>=a16)
s.add(a15*(a14+a16+1)-a16==15514)
s.add(a15>90)
s.add(a15<=99)

#func11
s.add(a17>=a16)
s.add(a16>=a18)
s.add(a17>100)
s.add(a17<=104)
s.add(a16+(a17 ^(a17- a18))-a18==70)
s.add((a17+a18)/a16+a16==68)

#func12
s.add(a18>=a19)
s.add(a19>=a20)
s.add(a19<=59)
s.add(a20<=44)
s.add(a18+(a19^(a20+a19))-a20 ==111)
s.add((a19^(a19-a20))+a19==101)

#func13
s.add(a20<=a21)
s.add(a21<=a22)
s.add(a20>40)
s.add(a21>90)
s.add(a22<=109)
s.add(a22+(a21^(a22+ a20))-a20==269)
s.add((a22 ^(a21-a20))+a21==185)

#func14
s.add(a22>=a24)
s.add(a23>=a24)
s.add(a23<=99)
s.add(a24>90)
s.add(a22+(a23 ^(a23+ a22))-a24==185)

#func15
s.add(a25>=a26)
s.add(a25>=a24)
s.add(a26>95)
s.add(a25<=109)
s.add(((a25-a24)*a25^a26)-a24==1214)
s.add(((a26-a25)*a26^a24)+a25==-1034)
````

>>> s.check()
sat
>>> val=s.model()
>>> print(val)
[a23 = 98,
 a2 = 104,
 a16 = 66,
 a13 = 110,
 a26 = 97,
 a19 = 58,
 a9 = 95,
 a14 = 97,
 a24 = 95,
 a25 = 108,
 a7 = 111,
 a12 = 110,
 a21 = 95,
 a22 = 108,
 a10 = 87,
 a18 = 63,
 a11 = 97,
 a4 = 116,
 a20 = 41,
 a3 = 97,
 a8 = 117,
 a17 = 101,
 a6 = 89,
 a15 = 95,
 a1 = 87,
 a5 = 95]



Converting each decimal to char
we get :
 What_You_Wanna_Be?:)_lb_la


when submited gives:
HAPPINESS:)
HAPPINESS:)
HAPPINESS:)
HAPPINESS:)
HAPPINESS:)
HAPPINESS:)
HAPPINESS:)
HAPPINESS:)
HAPPINESS:)
HAPPINESS:)
HAPPINESS:)
HAPPINESS:)
HAPPINESS:)
HAPPINESS:)
HAPPINESS:)

But does not give flag format. so i tryed changing to "b" to "a"
Your flag : What_You_Wanna_Be?:)_la_la  


Giving:
flag : {" What_You_Wanna_Be?:)_la_la "}

 

