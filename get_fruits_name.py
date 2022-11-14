def get_frutis_name(data:str)->list:
    """
    This function returns the name of the fruits in the list

    args:
        data: CSV file with the fruits data
    returns:
        list of fruits names
    """
    l = data.split()
    l.remove('name,price')
    x = []
    for i in l:
        x.append(i[:i.index(',')])

    

    return x


print(get_frutis_name(open('fruits.csv').read()))    