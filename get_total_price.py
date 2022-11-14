def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits in the list

    args:
        data: CSV file with the fruits data
    returns:
        list of fruits total price
    """
    l = data.split()
    l.remove('name,price')
    x = 0
    for i in l:
        x += float(i[i.index(',')+1:])

    

    return x
print(get_total_price(open('fruits.csv').read()))