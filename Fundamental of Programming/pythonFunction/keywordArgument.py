def greet(**kwargs):
    if kwargs:
        print(kwargs['name'],kwargs['value'])


greet(name="srk",value="plattinum")
