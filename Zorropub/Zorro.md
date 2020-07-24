***Zorropub writeup:***

 When the binary is run it asks for no.of drinks:
```
  puts("Welcome to Pub Zorro!!");

  printf("Straight to the point. How many drinks you want?", a2);
  __isoc99_scanf("%d", &v5);
```
If the number is < 0 :
```
  if ( v5 <= 0 )
  {
    printf("You are too drunk!! Get Out!!", &v5);
    exit(-1);
  }
```
Then it asks forthe details of drink:
```
  printf("OK. I need details of all the drinks. Give me %d drink ids:", (unsigned int)v5);
```
Then according to the no.of drinks and drink id:
Then it makes sure the id is btw 16  and  65535

```
  for ( i = 0; i < v5; ++i )
  {
    __isoc99_scanf("%d", &v6);
    if ( v6 <= 16 || v6 > 0xFFFF )
    {
      puts("Invalid Drink Id.");
      printf("Get Out!!", &v6);
      exit(-1);
    }
    seed ^= v6;                   //And then it xors with seed oone by one
  }
```
The seed is then given to i and then counted to know how many 1s re there in the binary of seed, and can only continue if it is 10

```
  i = seed;
  v9 = 0;
  while ( i )
  {
    ++v9;
    i &= i - 1;
  }
  if ( v9 != 10 )
  {
    puts("Looks like its a dangerous combination of drinks right there.");
    puts("Get Out, you will get yourself killed");
    exit(-1);
  }
```
After that :


```
  srand(seed);
  MD5_Init(&v10);
  for ( i = 0; i <= 29; ++i )
  {
    v9 = rand() % 1000;
    sprintf(&s, "%d", v9);
    v3 = strlen(&s);
    MD5_Update(&v10, &s, v3);
    v12[i] = v9 ^ LOBYTE(dword_6020C0[i]);
  }
  v12[i] = 0;
  MD5_Final(v11, &v10);
  for ( i = 0; i <= 15; ++i )
    sprintf(&s1[2 * i], "%02x", (unsigned __int8)v11[i]);
  if ( strcmp(s1, "5eba99aff105c9ff6a1a913e343fec67") )
  {
    puts("Try different mix, This mix is too sloppy");
    exit(-1);
  }
  return printf("\nYou choose right mix and here is your reward: The flag is nullcon{%s}\n", v12);

```
Here we can conclude that,as xor is an operation that just maps onto itself, and as  there's no other use of the input values of no.of drinks and if there is more than one drink it would creat same value so we can conclude that we really only need 1 drink for this  
So the only information we have is that the input ID is between 17 to 65535
So i tryed bruteforcing with 1 drink and find the Correct id:

```
#!/bin/bash
for i in {17..65535}
do
	x=$(echo -e "1\n$i"|./zorro_bin| grep  nullcon)
	# echo $x
	if [ -n "$x" ]
	then
		echo $x
		echo "Id is" $i 
	fi
done
```
Giving output:
You choose right mix and here is your reward: The flag is nullcon{nu11c0n_s4yz_x0r1n6_1s_4m4z1ng}
And,Id is : 59306



