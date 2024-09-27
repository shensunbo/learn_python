if __name__ == '__main__':
    print("main")
else:
    from .foo import foo
    print("mysubpack init")