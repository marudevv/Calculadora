primero = input('Ingrese primer número: ')

try:
    primero = int(primero)
except:
    primero='noNumero'

segundo = input('Ingrese segundo número: ')

try:
    segundo = int(segundo)
except:
    segundo= 'noNumero'

if primero == 'noNumero' or segundo == 'noNumero':
    print('Ingresaste mal un dato, prueba de nuevo solo con números')
else:
    print(primero + segundo)