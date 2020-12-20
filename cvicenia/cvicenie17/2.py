def cele(n):
    try:
        return int(n)
    except TypeError:
        return 0
    except ValueError:
        return 0


# cele(12.3)
# cele('13')
# cele([])
# cele('12.3')
