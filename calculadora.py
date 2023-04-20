primero = input('Ingrese primer número: ')

try:
    primero = int(primero)
except:
    primero = 'noNúmero'

if primero == 'noNúmero':
    print('El valor ingresado no es un entero')
    exit()

segundo = input('Ingrese segundo número: ')

try:
    segundo = int(segundo)
except:
    segundo = 'noNúmero'

if segundo == 'noNúmero':
    print('El valor ingresado no es un entero')
    exit()

simbolo = input('Ingrese operación: ')

if simbolo == '+':
    print('Suma:', primero + segundo)
elif simbolo == '-':
    print('Resta:', primero - segundo)
elif simbolo == '*':
    print('Multiplicación:', primero * segundo)
elif simbolo == '/':
    print('División:', primero / segundo)
else:
    print('El símbolo ingresado no es válido')
