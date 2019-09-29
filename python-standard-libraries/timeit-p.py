import timeit

if __name__ == "__main__":
    #timeit.timeit( "-".join( () ) )
    print(timeit.timeit('2000%10', number=10000))
    print ( "_".join ( str(n) for n in range(100)))
    print ( timeit.timeit('"_".join ( str(n) for n in range(100))', number=1000))

    #%timeit "_".join ( str(n) for n in range(100))  # does not work, works only jupiter notbook
