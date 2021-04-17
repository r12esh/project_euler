def no_of_devisors(n):
    lst = []
    count2 = 0
    if n%2 == 0:
        while n%2 == 0:
            n=n/2
            count2+= 1
        lst.append(['count2',count2])
    for i in range(3,int(n**0.5)+1,2):
        counti = 0
        if n%i==0:
            while n%i == 0:
                n = n/i
                counti+=1
            lst.append(['count{}'.format(i),counti])
    if n>2:
        lst.append(['count{}'.format(int(n)),1])

    lst2 = []
    for i in lst:
        lst2.append(i[1])
    product = 1    
    for i in lst2:
        product*=i+1
    return(product)    
k=28
while True:
    triangular_number_of_k = k*(k+1)/2
    k+=1
    if no_of_devisors(triangular_number_of_k) > 500:
        print(int(triangular_number_of_k))
        break

