def get_data():
    f = open('names.txt', 'r')
    
    names= f.read()

    names= names.split()

    return names

    f.close()