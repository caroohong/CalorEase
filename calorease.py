# -*- coding: utf-8 -*-
#Integrantes: Carolina Hong y Andrés Pirela

import ply.lex as lex
import ply.yacc as yacc

reserved={
   'kcal' : 'KCAL',
   'ate' : 'ATE',
   'limit' : 'LIMIT',
   'average' : 'AVERAGE',
   'intake': 'INTAKE',
   '=' : 'ASIGN',
   'sum': 'SUM',
   'day': 'DAY',
   'food': 'FOOD',
   'with': 'WITH'
}

tokens = [
    'NUMBER', #gramos consumidos de x comida
    'ID', #tipo de alimento
    'DATE'
    ]+list(reserved.values())
    
t_KCAL = r'kcal'
t_ATE = r'ate'
t_LIMIT = r'limit'
t_AVERAGE = r'average'
t_INTAKE = r'intake'
t_ASIGN = r'='
t_SUM = r'sum'
t_DAY = r'day'
t_FOOD = r'food'
t_WITH = r'with'

# Expresión regular para la fecha (yyyy-mm-dd)
def t_DATE(t):
    r'\d{4}-\d{2}-\d{2}'
    #\d reconoce enteros
    #{n}: numero de digitos
    return t

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
    print(f"Error lexico: Carácter no valido {t.value[0]}")
    t.lexer.skip(1) #no se cierra el programa si hay error

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
        'hamburguesa': 230,
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
    'legumbres': {
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
        'champaÃ±a': 100,
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
    'otros': {}
}
#reglas gramaticales
import datetime
from numpy import random
intakes = {}
def p_expresion(t):
    '''
    expresion : kcal_expr
              | ate_expr
              | average_intake
              | limit
              | sum_day
              | food_with
    '''
    
def p_expr_numero(t):
    'expresion : NUMBER'
    target_kcal=t[1]
    foods = {}
    min_diff = float('inf')
    for tipo, alimentos in calorias.items():
        for alimento, kcal in alimentos.items():
            diff = abs(kcal - target_kcal)
            if diff < min_diff:
                foods = {alimento: kcal}
                min_diff = diff
            elif diff == min_diff:
                foods[alimento] = kcal
    
    print(f"ALimentos con alrededor de {target_kcal} kcal:")
    for alimento, kcal in foods.items():
        print(f"{alimento}: {kcal} kcal")

def p_expr_id(t):
    'expresion : ID'
    global calorias
    alimento = t[1]
    for tipo, alimentos in calorias.items():
        if alimento in alimentos:
            t[0] = alimentos[alimento]
            print(f"{alimento}: {alimentos[alimento]} kcal")
            return
    print(f"Alimento {alimento} no disponible")
    t[0] = 0
    
limit = 1000000
#ej: limit 1050, se interpreta como limite de 1050 kcal
def p_limit(t):
    'limit : LIMIT NUMBER'
    global limit
    cal_max = t[2]
    limit = t[2]
    print(f"Li­mite de calori­as diarias establecido a {cal_max} kcal")

# expresion -> ate number id
#ej: ate 50 tomate, se interpreta como 50 gramos de tomate
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
                print(f"Se ha superado el limite de calori­as diarias {limit} kcal")
                print(f"Quedan solo {round(limit - suma_cal,3)} kcal disponibles")
                t[0] = 0
                return
            
            t[0] = cal_total
            if fecha in intakes:
                if alimento in intakes[fecha].keys():
                    intakes[fecha][alimento] += cal_total
                else:
                    intakes[fecha][alimento] = cal_total
            else:
                intakes[fecha] = {alimento: cal_total}
            print(f"Registro de consumo exitoso para el dia {fecha}: {alimento} ({round(cal_total, 3)} kcal)")
            if limit != 1000000:
                print(f"Quedan {round(limit - suma_cal - cal_total, 3)} kcal disponibles")
            return
    print(f"Alimento {alimento} no disponible")
    t[0] = 0
    
#ej: kcal pera
def p_kcal_expr(t):
    'kcal_expr : KCAL ID '
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
        print(f"{alimento} ({food}): {cal} kcal en 100 gramos")
    else:
        print(f"No se encontraron calori­as para el alimento {alimento}")


#ej: kcal carne = 200
def p_registro_consumo(t):
    'kcal_expr : KCAL ID ASIGN NUMBER'
    alimento = t[2]
    cal = t[4]
    global calorias
    if alimento not in calorias['otros']:
        calorias['otros'][alimento] = cal
        print(f"Registro de {alimento} exitoso")
    else:
        print(f"El alimento {alimento} ya existe")

# average_intake -> average intake
def p_average_intake(t):
    'average_intake : AVERAGE INTAKE'
    cal_total = 0
    dias = 0
    for consumidos in intakes.values():
        cal_total += sum(consumidos.values())
        dias +=1
    if dias > 0:
        average = cal_total/dias
        print(f"Promedio de calorí­as diario: {average} kcal")
    else:
        print("No hay registros")

from datetime import date
# sum_day -> sum day yyyy-mm-dd  
#ej: sum day 2023-06-14
def p_sum_day(t):
    'sum_day : SUM DAY DATE'
    fecha_str = t[3]
    year, month, day = fecha_str.split('-')
    fecha = date(int(year), int(month), int(day))
    cal_total = 0
    if fecha in intakes:
        daily_intake = intakes[fecha]
        for calorias in daily_intake.values():
            cal_total += calorias
        print(f"Calorias totales del dia {fecha}: {round(cal_total, 3)} kcal")
    else:
        print(f"No hay registros del dia {fecha}");

# expression -> food with number 
#ej: food with 400
def p_expr_food_with(t):
    'food_with : FOOD WITH NUMBER'
    global calorias
    comida = {}
    cal_disp = float(t[3])
    #Un plato promedio lo consideraremos que de las calori­as totales 55% son de alguna proteina, 44% de algun cereal y 5% de alguna verdura
    p = cal_disp*0.55
    c = cal_disp*0.4
    v = cal_disp*0.05

    proteina = random.randint(0,4) #de carne si es igual a 0, de mar si es igual a 1, legumbres si es igual a 2 y huevo si es igual a 3
    if proteina == 0:
        d = calorias['carnes']
        alimento = random.choice(list(d.keys()))
        cal = d[alimento]
        gramos = p*100/(cal)
        comida[alimento] = [gramos, p]
    elif proteina == 1:
        d = calorias['productos del mar']
        alimento = random.choice(list(d.keys()))
        cal = d[alimento]
        gramos = p*100/(cal)
        comida[alimento] = [gramos, p]
    elif proteina == 2:
        d = calorias['legumbres']
        alimento = random.choice(list(d.keys()))
        cal = d[alimento]
        gramos = p*100/(cal)
        comida[alimento] = [gramos, p]
    else:
        d = calorias['huevos']
        alimento = random.choice(list(d.keys()))
        cal = d[alimento]
        gramos = p*100/(cal)
        comida[alimento] = [gramos, p]

    cereal = random.choice(list(calorias['cereales'].keys()))
    cal_c = calorias['cereales'][cereal]
    gramos_c = c*100/(cal_c)
    comida[cereal] = [gramos_c, c]

    verdura = random.choice(list(calorias['verduras'].keys()))
    cal_v = calorias['verduras'][verdura]
    gramos_v = v*100/(cal_v)
    comida[verdura] = [gramos_v, v]

    print(f"A continuacion se muestra un ejemplo de un plato que tiene un total de {cal_disp} kcal")
    for alimento in comida:
        print(f"{alimento} : {round(comida[alimento][0], 3)} gramos ({round(comida[alimento][1], 3)} kcal)")

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
