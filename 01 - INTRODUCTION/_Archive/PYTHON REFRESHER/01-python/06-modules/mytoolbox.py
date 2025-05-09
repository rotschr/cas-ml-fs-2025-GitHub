# "exported" function
def headline(msg, n_stars=40):
    _print_asterisks(n_stars)
    print(msg)
    _print_asterisks(n_stars)


# "internal" function (starting with an underscore)
def _print_asterisks(n_stars):
    print("*" * n_stars)
