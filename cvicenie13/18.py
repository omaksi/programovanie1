def do_dvojrozmernej(a, sirka):
    res = []
    for i in range(0, len(a), sirka):
        resinner = []
        for j in range(sirka):
            if i+j < len(a):
                resinner.append(a[i+j])
        res.append(resinner)
    return res


# t1 = do_dvojrozmernej(range(10), 3)
# vypis(t1)
# vypis(do_dvojrozmernej('programovanie', 5))
