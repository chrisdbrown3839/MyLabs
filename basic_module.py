print('Imported basic_module...')


def find_index(to_search, target):
    #Find the index of a value in a sequence

    for index, value in enumerate(to_search):
        if value == target:
            return index, target

    return -1,'na'
