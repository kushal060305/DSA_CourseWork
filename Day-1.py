# Counting the number of even numbers from 1 to n
'''def count_even(n):

    count=0
    for i in range(1,n+1):
        if i%2==0:
            count+=1
    return count
n=int(input("Enter a number: "))
print("Number of even numbers from 1 to",n,"is:",count_even(n))
'''

###############################################################

# Counting the number of digits in a number
def count_digits(num):
    count=0
    while num>0:
        num=num//10
        count+=1    
    return count

def main():
    num=int(input("Enter a number: "))
    print("Number of digits in",num,"is:",count_digits(num))
main()  
