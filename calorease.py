# -*- coding: utf-8 -*-
import ply.lex as lex
import ply.yacc as yacc

reserved={
   'kcal' : 'KCAL',
   'ate' : 'ATE',
   'limit' : 'LIMIT',
   'intake': 'INTAKE',
   '=' : 'ASIGN'
}

tokens = [
    'NUMBER', #gramos consumidos de x comida
    'ID' #tipo de alimento
    ]+list(reserved.values())
    
t_KCAL = r'kcal'
t_ATE = r'ate'
t_LIMIT = r'limit'
t_INTAKE = r'intake'
t_ASIGN = r'='

def t_NUMBER(t):
    r'[0-9]+' #como reconocer un numero: valores entre 0 y 9 repetidos 1 o mas veces
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_]+' #reconcocer letras
    t.type = reserved.get(t.value,'ID') #asociar a un ID
    return t

t_ignore  = ' \t' #ignorar espacio o tabulacion

#error de interpretacion
def t_error(t):
    print(f"Error léxico: Carácter no válido {t.value[0]}")
    t.lexer.skip(1) #no se cierra el programa si hay error

#precedence=(('left', 'SU', 'RE'),) #***************************************************************

variables={} #food_type: in grams intake
calorias = {
    'verduras': {
        'ajo': 169,
        'apio': 20,
        'cebolla': 47,
        'brocoli': 31,
        'berenjena': 29,
        'lechuga': 18,
        'esparragos': 26,
        'espinaca': 32,
        'zanahoria': 42,
        'tomate': 22,
        'pepino': 12,
        'repollo': 19
    },
    'frutas': {
        'arandanos': 41,
        'cereza': 47,
        'ciruela': 44,
        'coco': 646,
        'frambuesa': 40,
        'frutilla': 36,
        'granada': 65,
        'kiwi': 51,
        'limon': 39,
        'mandarina': 40,
        'mango': 57,
        'manzana': 52,
        'melon': 31,
        'naranja': 44,
        'pera': 61,
        'pina': 51,
        'platano': 90,
        'pomelo': 30,
        'sandia': 30,
        'uva': 81
    },
    'lacteos': {
        'helado': 167,
        'leche_condensada': 350,
        'leche_descremada': 36,
        'crema': 298,
        'queso_blanco': 70,
        'queso_cheddar': 381,
        'queso_mozzarella': 245,
        'queso_parmesano': 393,
        'yogur': 62
    },
    'carnes': {
        'bacon': 665,
        'lomo_cerdo': 208,
        'chorizo': 468,
        'gallina': 369,
        'hamburgues': 230,
        'jamon': 380,
        'pollo': 134,
        'salami': 325,
        'salchicha': 315,
        'vacuno': 129,
        'asado': 401
    },
    'productos del mar': {
        'almejas': 50,
        'atun': 280,
        'calamar': 82,
        'cangrejo': 85,
        'caviar': 233,
        'langosta': 67,
        'mejillon': 74,
        'ostras': 80,
        'pulpo': 57,
        'salmon': 172,
        'sardina': 151,
        'sardinas': 151,
        'salmon_ahumado': 154,
        'trucha': 94
    },
    'azucares': {
        'azucar': 380,
        'chocolate': 550,
        'cacao': 366,
        'miel': 300,
        'mermelada': 280,
        'nutella': 549,
        'helado_de_agua': 139
    },
    'cereales': {
        'arroz_blanco': 354,
        'arroz_integral': 350,
        'avena': 367,
        'cereal': 360,
        'harina_maiz': 349,
        'harina_trigo': 340,
        'pan': 240 
    },
    'legunmbres': {
        'garbanzos': 361,
        'lentejas': 336
    },
    'huevos': {
        'clara': 48,
        'yema': 368,
        'huevo_duro': 147,
        'huevo_entero': 162
    },
    'refrescos': {
        'agua_tonica': 34,
        'cafe': 1,
        'cerveza': 45,
        'champaña': 100,
        'leche_almendra': 335,
        'pisco': 210,
        'te': 1,
        'ron': 244,
        'vodka': 315,
        'whisky': 244,
        'vino': 160,
    },
    'aceites': {
        'aceite_girasol': 900,
        'aceite_oliva': 900,
        'mantequilla': 752,
        'margarina': 752
    },
}
#reglas gramaticales
import datetime
intakes = {}
def p_expresion(t):
    '''
    expresion : kcal_expr
              | ate_expr
              | average_intake
              | limit
    '''
    #print(t[1])
    
def p_expr_numero(t):
    'expresion : NUMBER'
    t[0]=t[1]

def p_expr_id(t):
    'expresion : ID'
    global calorias
    alimento = t[1]
    for tipo, alimentos in calorias.items():
        if alimento in alimentos:
            t[0] = alimentos[alimento]
            print(f"El alimento {alimento} tiene {alimentos[alimento]} kcal")
            return
    print(f"Alimento {alimento} no disponible")
    t[0] = 0
    
limit = 1000000
def p_limit(t):
    'limit : LIMIT NUMBER'
    global limit
    cal_max = t[2]
    limit = t[2]
    print(f"Límite de calorías diarias establecido a {cal_max} kcal")

# expresion -> ate number id
def p_expr_ate(t):
    'ate_expr : ATE NUMBER ID'
    global calorias
    gramos = t[2]
    alimento = t[3]
    fecha = datetime.date.today()
    for tipo, alimentos in calorias.items():
        if alimento in alimentos:
            cal_100g = alimentos[alimento] 
            cal_total = (cal_100g/100) * int(gramos)
            
            suma_cal = sum(intakes.get(fecha, {}).values())
            if (suma_cal + cal_total) > limit:
                print(f"Se ha superado el limite de calorías diarias {limite} kcal")
                t[0] = 0
                return
            
            t[0] = cal_total
            if fecha in intakes:
                intakes[fecha][alimento] = cal_total
            else:
                intakes[fecha] = {alimento: cal_total}
            return
    print(f"Alimento {alimento} no disponible")
    t[0] = 0
    
#ej: kcal pera
def p_kcal_expr(t):
    '''kcal_expr : KCAL ID 
                | registro_consumo'''
    global calorias
    food = ""
    alimento = t[2]
    cal = -1
    for tipo, alimentos in calorias.items():
        if alimento in alimentos:
            food = tipo
            cal = alimentos[alimento]
            break
    if cal != -1:
        print(f"El alimento {alimento} ({food}) tiene {cal} kcal")
    else:
        print(f"No se encontraron calorías para el alimento {alimento}")


#ej: kcal carne = 200
def p_registro_consumo(t):
    'registro_consumo : KCAL ID ASIGN NUMBER'
    alimento = t[2]
    cal = t[4]
    global calorias
    if alimento not in calorias['otros']:
        calorias['otros'][alimento] = cal
        print("Registro de {alimento} exitoso")
    else:
        print(f"El alimento {alimento} ya existe")


def p_average_intake(t):
    'average_intake : INTAKE'
    cal_total = 0
    dias = 0
    for consumidos in intakes.values():
        cal_total += sum(consumidos.values())
        dias +=1
    if dias > 0:
        average = cal_total/dias
        print(f"Promedio de calorías diario: {average} kcal")
    else:
        print("No hay registros")


def p_error(t):
    print("Error de sintaxis")


lexer=lex.lex()
parser=yacc.yacc()
while True:
    try:
        data = input()
    except EOFError:
        break
    parser.parse(data)
