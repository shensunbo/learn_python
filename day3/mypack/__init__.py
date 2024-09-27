if __name__ == '__main__':
    print("main")
else:
    from .bar import bar
    print("mypack init")