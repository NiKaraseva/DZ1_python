# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех
# значений предикат.


X = False
Y = False
Z = False

print((not(X or Y or Z)) == (not X and not Y and not Z))

X = False
Y = False
Z = True

print((not(X or Y or Z)) == (not X and not Y and not Z))

X = False
Y = True
Z = False

print((not(X or Y or Z)) == (not X and not Y and not Z))

X = False
Y = True
Z = True

print((not(X or Y or Z)) == (not X and not Y and not Z))

X = True
Y = False
Z = False

print((not(X or Y or Z)) == (not X and not Y and not Z))

X = True
Y = False
Z = True

print((not(X or Y or Z)) == (not X and not Y and not Z))

X = True
Y = True
Z = False

print((not(X or Y or Z)) == (not X and not Y and not Z))

X = True
Y = True
Z = True

print((not(X or Y or Z)) == (not X and not Y and not Z))