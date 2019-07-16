from area import area

if __name__ == '__main__':
    print("Hello, world!")

    # From the example in the library's README: https://pypi.org/project/area/
    obj = {'type':'Polygon','coordinates':[[[-180,-90],[-180,90],[180,90],[180,-90],[-180,-90]]]}
    print(area(obj))
