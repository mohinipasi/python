'''
Python divides the operators in the following groups:

1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Identity operators
6. Membership operators
7. Bitwise operators
'''


#PYTHON ARITHMATIC OPERATOR
'''
Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator	Name	       Example	
+	      Addition  	    x + y	
-	     Subtraction	    x - y	
*	    Multiplication	    x * y	
/	      Division  	    x / y	
%	       Modulus	        x % y	
**	    Exponentiation	    x ** y	
//	    Floor division	    x // y	
'''

X=12
Y=10
print(X+Y)

X=12
Y=10
print(X-Y)

X=12
Y=10
print(X*Y)

X=12
Y=10
print(X/Y)

X=12
Y=10
print(X%Y)

X=12
Y=10
print(X**Y)

X=12
Y=10
print(X//Y)

#PYTHON ASSIGNMENT OPERATOR
'''
Assignment operators are used to assign values to variables:

Operator	Example	       Same As	
=	           x = 5	    x = 5	
+=	           x += 3	    x = x + 3	
-=	           x -= 3	    x = x - 3	
*=	           x *= 3	    x = x * 3	
/=	           x /= 3	    x = x / 3	
%=	           x %= 3	    x = x % 3	
//=            x //= 3	    x = x // 3	
**=	           x **= 3	    x = x ** 3	
&=	           x &= 3	    x = x & 3	
|=         	   x |= 3	    x = x | 3	
^=	           x ^= 3	    x = x ^ 3	
>>=	           x >>= 3	    x = x >> 3	
<<=	           x <<= 3	    x = x << 3	
:=	         print(x := 3)	x = 3
                            print(x)	
'''

#PYTHON COMPARSION OPERATORS
'''
Comparison operators are used to compare two values:

Operator	Name	                   Example	
==	       Equal	                    x == y	
!=	       Not equal	                x != y	
>	       Greater than	                x > y	
<	       Less than	                x < y	
>=	       Greater than or equal to 	x >= y	
<=	       Less than or equal to	    x <= y
'''

#PYTHON LOGICAL OPERATOR
'''
Logical operators are used to combine conditional statements:

Operator	                   Description	                                 Example	
and 	           Returns True if both statements are true	              x < 5 and  x < 10	
or	             Returns True if one of the statements is true	          x < 5 or x < 4	
not          Reverse the result, returns False if the result is true	  not(x < 5 and x < 10)	

AND TRUTH TABLE (&)
A + B =  C       # 0 = FALSE  # 1 = TRUE 
0 + 0 =  0
0 + 1 =  0
1 + 0 =  0
1 + 1 =  1 

OR TRUTH TABLE (|)
A + B =  C       # 0 = FALSE  # 1 = TRUE 
0 + 0 =  0
0 + 1 =  1
1 + 0 =  1
1 + 1 =  1

EOR TRUTH TABLE (^)
A + B =  C       # 0 = FALSE  # 1 = TRUE 
0 + 0 =  0
0 + 1 =  1
1 + 0 =  1
1 + 1 =  0 
'''

#PYTHON IDENTIFY OPERATOR
'''
Identity operators are used to compare the objects, not if they are equal, 
but if they are actually the same object, with the same memory location:

Operator	   Description	                                                 Example	
is 	        Returns True if both variables are the same object	             x is y	
is not	    Returns True if both variables are not the same object	         x is not y
'''
#IS
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # returns True because z is the same object as x
print(x is y) # returns False because x is not the same object as y, even if they have the same content
print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

#IS NOT
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z) # returns False because z is the same object as x
print(x is not y) # returns True because x is not the same object as y, even if they have the same content
print(x != y)     # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y


#PYTHON MEMBERSHIP OPERATOR
'''
Membership operators are used to test if a sequence is presented in an object:

Operator	                                        Description	                                  Example	
in 	            Returns True if a sequence with the specified value is present in the object	  x in y	
not in	        Returns True if a sequence with the specified value is not present in the object  x not in y
'''
#IN
x = ["apple", "banana"]
print("banana" in x)   #OUTPUT WILL BE TRUE

#NOT IN
x = ["apple", "banana"]
print("pineapple" not in x)   #OUTPUT WILL BE TRUE


#PYTHON BITWISE OPERATOR
'''
Bitwise operators are used to compare (binary) numbers:

Operator	Name	                Description	                                       Example	
& 	        AND	                Sets each bit to 1 if both bits are 1	                x & y	
|	        OR	                Sets each bit to 1 if one of two bits is 1	            x | y	
^	        XOR       	        Sets each bit to 1 if only one of two bits is 1	        x ^ y	
~	        NOT	                Inverts all the bits	                                ~x	
<<	     Zero fill left shift	Shift left by pushing zeros in from the right
                                and let the leftmost bits fall off	                    x << 2	
>>	    Signed right shift	    Shift right by pushing copies of the leftmost bit in 
                                from the left, and let the rightmost bits fall off      x >> 2
'''

#OPERATOR PRECEDENCE
'''
Operator precedence describes the order in which operations are performed.

The correct order of precedence 
is given by PEMDAS which means
 Parenthesis (), Exponential **, Multiplication *, Division /, Addition +, Subtraction -.
'''
print(100 + 5 * 3) #Multiplication has higher precedence than addition, and needs to be evaluated first.
                   #The calculation above reads 100 + 15 = 115