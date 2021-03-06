'''Question:Inserti on: You are given two 32-bit numbers, Nand M, and two bit positions, i and
j. Write a method to insert Minto N such that M starts at bit j and ends at bit i. You
can as sume that the bits j through i have enough space to fit all of M.
Example : 
mask = 11100011  suppose we want this mask 
j=4,i=2
let start

Algorithms
Step 1:clear bits from higher location to lower i.e from j to i in 'N'
        A.left_mask = ~0<<(j+1)    higher j bits are now 1's rest are 0's      --->>     11111111(4+1)=11100000
        B.right_mask = 1<<i-1      only lower i bits are 1 higher bits will now 0's---->>00000000(2)-->>00000100-1-->>00000011
        C.mask = left_mask | right_mask         =>>>11100000 | 00000011 ==>>   11100011 
Step 2: Align 'M' by shifting it by i bits (M<<i)   
Step 3: Take or operation of N and mask i.e N | mask


input : N,M,j,i=5 3 2 1
output : 7
input : 1024 19 6 2
output : 1100
NOTE : One thing is worth to take care is that you prior need need to check that number of bits in "M" must be greater than j-i+1

following is valid python program for the above explaination'''

data=input('Enter N,M,i,j : ')
data=list(data.split(' '))
data=[int(x) for x in data]
N,M,j,i=data[0],data[1],data[2],data[3]
left_mask=~0<<(j+1)
right_mask=1<<i-1
mask=left_mask | right_mask
aligned_m=M<<i;
print(N|aligned_m)
