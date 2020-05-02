
r=True
def factor():
    n=int(input('enter a number'))
    o=str(input(' \'s\' for simple factor \'d\' for detailed factor'))
    if o=='s':
        simple(n)
    elif o=='d':
        detailed(n)
def detailed(n):
    i=2
    while i<=n:
        if n%i==0:
            print(i)
            n=n//i
            i=2
        i+=1
def simple(n):
    i=2
    for i in range(2,n):
        if n%i==0:
            print(i)
            n=n//i


while r:
    factor()
    print('to run again enter r')
    m=str(input())
    if m=='r':
        r=True
    else:
        r=False
