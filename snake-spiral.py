def spiralize(size):
    #Создание матрицы в виде змейки
    spiral = list(map(lambda x: list(map(lambda y: 1 
                                        if (int(size + 1) / 2) % 2 == 1 else 0, range(0, size))), 
                                        range(0, size)))
    base_spiral = 1
    for i in range(0, int(size / 2)):
        for u in range(0, size - i * 2):
            spiral[i][u+i] = base_spiral
            spiral[u+i][i] = base_spiral
            spiral[size - i - 1][u+i] = base_spiral
            spiral[u+i][size - i - 1] = base_spiral
            
            if size % 4 == 0:
                if i != int(size / 2) - 1:
                    spiral[i+1][i] = 1 - base_spiral
            else:
                spiral[i+1][i] = 1 - base_spiral
        base_spiral = 1 - base_spiral

    return spiral

size = int(input())
spiral = spiralize(size)
print(spiral)