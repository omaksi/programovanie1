def postupnost(start, koniec, krok=1):
    return ' '.join(map(str, list(range(start, koniec, krok))))


print(postupnost(5, 13))
print(postupnost(13, 5, -2))
