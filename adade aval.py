while True :
    user = int(input("Enter number: "))

    is_prime = True

    for i in range(2, user):
        if user % i == 0:
            is_prime = False
            print(f'{user} % {i}')
            break

    if is_prime == True:
        print(f'{user} is prime.')
    else :
        print(f'{user} is not Prime.')
    
    print('\n', '-'*15, '\n')