def get_expensive_fruit(data:str)->str:
    """
    This function returns the name of the most expensive fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the most expensive fruit
    """
    list_of_fruits = data.split()[1:]
    e = 0.0
    for i in list_of_fruits:
        p = i[i.index(',')+1:]
        if e < float(p):
            e = float(p)

    return e

print(get_expensive_fruit(open('fruits.csv').read()))
