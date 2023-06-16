# CalorEase
## Funciones
 Las palabras sin comillas son las palabras claves
 
 kcal 'alimento' 
 > muestra las kcal de 100 gramos de un alimento.
 
 'alimento'
 > muestra las kcal de 100 gramos de un alimento
 
 ate 'num' 'alimento'
 > simboliza ingerir 'num' gramos de 'alimento'
 
 average intake
 > retorna el promedio de calorias ingeridas por día
 
 limit 'num'
 > se establece un numero de kcal diarias a 'num' kcal
 
 'num'
 > muestra que alimento posee 'num' kcal
 
 kcal 'alimento_personalizado' = 'num'
 > el usuario puede ingresar las kcal de sus propios alimentos

sum day 'yyyy-mm-dd'
> retorna las calorias ingeridas en un dia ingresado por el usuario

food with 'num'
> muestra un plato con 'num' kcal con 55% proteinas, 40% carbohidratos y 5% verduras

## Ejemplos
 kcal pera
 > pera (frutas): 61 kcal en 100 gramos
 
 kcal manzana
 > manzana (frutas): 52 kcal en 100 gramos

 ate 10 salmon
 > Registro de consumo exitoso para el dí­a 2023-06-16: salmon (17.2 kcal)

 ate 50 pollo
 > Registro de consumo exitoso para el dí­a 2023-06-16: pollo (67.0 kcal)

 ate 40 pera
 > Registro de consumo exitoso para el dí­a 2023-06-16: pera (24.4 kcal)

 average intake
 > Promedio de calorí­as diario: 108.6 kcal

 limit 110
 > Lí­mite de calorí­as diarias establecido a 110 kcal

 ate 100 vino
 > Se ha superado el limite de calorí­as diarias 110 kcal

 > Quedan solo 1.4 kcal disponibles

 20
 > ALimentos con alrededor de 20 kcal:
 
 > apio: 20 kcal

 40
 > ALimentos con alrededor de 40 kcal:
 
 > frambuesa: 40 kcal
 
 > mandarina: 40 kcal

 pollo
  > pollo: 134 kcal

 leche_de_coco
 > Alimento leche_de_coco no disponible

 kcal leche_de_coco = 136
 > Registro de leche_de_coco exitoso

 limit 400
 > Lí­mite de calorí­as diarias establecido a 400 kcal

 ate 100 leche_de_coco
 > Registro de consumo exitoso para el dí­a 2023-06-16: leche_de_coco (136.0 kcal)
 
 > Quedan 154.0 kcal disponibles

 sum day 2023-06-16
 > Calorias totales del dí­a 2023-06-16: 246.0 kcal

 sum day 2023-01-01
 > No hay registros del dia 2023-01-01

 food with 100
 > A continuación se muestra un ejemplo de un plato que tiene un total de 100.0 kcal

 > lentejas : 16.369 gramos (55.0 kcal)

 > pan : 16.667 gramos (40.0 kcal)

 > brocoli : 16.129 gramos (5.0 kcal)
 
 food with 50
  > A continuación se muestra un ejemplo de un plato que tiene un total de 50.0 kcal

 > clara : 57.292 gramos (27.5 kcal)

 > harina_maiz : 5.731 gramos (20.0 kcal)

 > brocoli : 8.065 gramos (2.5 kcal)
