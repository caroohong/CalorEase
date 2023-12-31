
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASIGN ATE AVERAGE DATE DAY FOOD ID INTAKE KCAL LIMIT NUMBER SUM WITH\n    expresion : kcal_expr\n              | ate_expr\n              | average_intake\n              | limit\n              | sum_day\n              | food_with\n    expresion : NUMBERexpresion : IDlimit : LIMIT NUMBERate_expr : ATE NUMBER IDkcal_expr : KCAL ID kcal_expr : KCAL ID ASIGN NUMBERaverage_intake : AVERAGE INTAKEsum_day : SUM DAY DATEfood_with : FOOD WITH NUMBER'
    
_lr_action_items = {'NUMBER':([0,11,13,21,22,],[8,17,19,25,26,]),'ID':([0,10,17,],[9,16,23,]),'KCAL':([0,],[10,]),'ATE':([0,],[11,]),'AVERAGE':([0,],[12,]),'LIMIT':([0,],[13,]),'SUM':([0,],[14,]),'FOOD':([0,],[15,]),'$end':([1,2,3,4,5,6,7,8,9,16,18,19,23,24,25,26,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-11,-13,-9,-10,-14,-15,-12,]),'INTAKE':([12,],[18,]),'DAY':([14,],[20,]),'WITH':([15,],[21,]),'ASIGN':([16,],[22,]),'DATE':([20,],[24,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expresion':([0,],[1,]),'kcal_expr':([0,],[2,]),'ate_expr':([0,],[3,]),'average_intake':([0,],[4,]),'limit':([0,],[5,]),'sum_day':([0,],[6,]),'food_with':([0,],[7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expresion","S'",1,None,None,None),
  ('expresion -> kcal_expr','expresion',1,'p_expresion','calorease.py',191),
  ('expresion -> ate_expr','expresion',1,'p_expresion','calorease.py',192),
  ('expresion -> average_intake','expresion',1,'p_expresion','calorease.py',193),
  ('expresion -> limit','expresion',1,'p_expresion','calorease.py',194),
  ('expresion -> sum_day','expresion',1,'p_expresion','calorease.py',195),
  ('expresion -> food_with','expresion',1,'p_expresion','calorease.py',196),
  ('expresion -> NUMBER','expresion',1,'p_expr_numero','calorease.py',200),
  ('expresion -> ID','expresion',1,'p_expr_id','calorease.py',204),
  ('limit -> LIMIT NUMBER','limit',2,'p_limit','calorease.py',217),
  ('ate_expr -> ATE NUMBER ID','ate_expr',3,'p_expr_ate','calorease.py',225),
  ('kcal_expr -> KCAL ID','kcal_expr',2,'p_kcal_expr','calorease.py',253),
  ('kcal_expr -> KCAL ID ASIGN NUMBER','kcal_expr',4,'p_registro_consumo','calorease.py',271),
  ('average_intake -> AVERAGE INTAKE','average_intake',2,'p_average_intake','calorease.py',283),
  ('sum_day -> SUM DAY DATE','sum_day',3,'p_sum_day','calorease.py',297),
  ('food_with -> FOOD WITH NUMBER','food_with',3,'p_expr_food_with','calorease.py',313),
]
