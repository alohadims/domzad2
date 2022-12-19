for x in range(2):
    for y in range(2):
        for z in range(2):
          if not(x or y or z) == (not x and not y and not z):
              print('Выражение истинно')
              print(x,y,z)
        else:
            print('Выражение ложно')
            print(x,y,z)