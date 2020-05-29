def show_params(*args, **kwargs):
    if args:
        for i in args:
            print(i)
    else:
        for i in kwargs.items():
            print(i)

show_params(1,2 ,3 ,4)
show_params(a=1, b=2)