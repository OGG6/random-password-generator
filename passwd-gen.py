script.py

# Python - random password generator #
1    print("Hello World!")
2    print("Generating a random password for you...")
3    import random as r; p = 'abcdefghijklmnopqrstuvwxyz0123456789%^*(-_=+)'; print(''.join([p[r.randint(0,len(p)-1)] for i in range(10)]))
4    print("Goodbye Cruel World!")
