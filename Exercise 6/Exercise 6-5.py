def list_remove_odd(list):
    for i in list:
        if i%2 != 0:
            list.remove(i)
    return list

