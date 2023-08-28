def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in range(x):
            print("{:d}".format(int(my_list[i])), end="")
        print()
        return i + 1
    except ValueError:
        print("", end="")
        return i
