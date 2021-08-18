# y => significa que ambas comparaciones tienen que ser verdaderas para que todo sea verdadero
# en JS es &&
# en python es 'and'
print((10 > 5) and (100 < 500))

# o => significa que basta con que alguna de las comparaciones sea verdadera para que todo sea verdadero
# en JS es || (alt+124)
# en python es 'or'
print((10 < 5) or (50 > 1))

#   TABLA DE LA VERDAD
#   V1  V2  |   AND  |   OR
#   V   V   |    V   |    V
#   V   F   |    F   |    V
#   F   V   |    F   |    V
#   F   F   |    F   |    F
