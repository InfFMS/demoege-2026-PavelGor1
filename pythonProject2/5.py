for n in range(1,100):

    m = format(n , 'b')

    if n % 3 ==0 :

        m = m + m[-3:]

    else:

        m = m+ format(n% 3 * 3,'b')
    R=int(m, 2)
    if R >=200:
        print(n)
        break
