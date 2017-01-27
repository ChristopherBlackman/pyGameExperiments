class Point(dict):
    def __missing__(self,key):
        return False


