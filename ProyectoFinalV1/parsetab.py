
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN DIVIDE ID INT LBRACES LPAREN MINUS NUMBER PLUS PRINT RBRACES RETURN RPAREN SEMICOLON TIMESstatement : ID ASSIGN expr SEMICOLONstatement : PRINT LPAREN expr RPAREN SEMICOLONexpr : expr PLUS expr\n            | expr MINUS expr\n            | expr TIMES expr\n            | expr DIVIDE exprexpr : NUMBERexpr : ID'
    
_lr_action_items = {'ID':([0,4,5,11,12,13,14,],[2,6,6,6,6,6,6,]),'PRINT':([0,],[3,]),'$end':([1,10,20,],[0,-1,-2,]),'ASSIGN':([2,],[4,]),'LPAREN':([3,],[5,]),'NUMBER':([4,5,11,12,13,14,],[8,8,8,8,8,8,]),'SEMICOLON':([6,7,8,15,16,17,18,19,],[-8,10,-7,20,-3,-4,-5,-6,]),'PLUS':([6,7,8,9,16,17,18,19,],[-8,11,-7,11,11,11,11,11,]),'MINUS':([6,7,8,9,16,17,18,19,],[-8,12,-7,12,12,12,12,12,]),'TIMES':([6,7,8,9,16,17,18,19,],[-8,13,-7,13,13,13,13,13,]),'DIVIDE':([6,7,8,9,16,17,18,19,],[-8,14,-7,14,14,14,14,14,]),'RPAREN':([6,8,9,16,17,18,19,],[-8,-7,15,-3,-4,-5,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expr':([4,5,11,12,13,14,],[7,9,16,17,18,19,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> ID ASSIGN expr SEMICOLON','statement',4,'p_statement_assign','test.py',49),
  ('statement -> PRINT LPAREN expr RPAREN SEMICOLON','statement',5,'p_statement_print','test.py',53),
  ('expr -> expr PLUS expr','expr',3,'p_expr_binop','test.py',57),
  ('expr -> expr MINUS expr','expr',3,'p_expr_binop','test.py',58),
  ('expr -> expr TIMES expr','expr',3,'p_expr_binop','test.py',59),
  ('expr -> expr DIVIDE expr','expr',3,'p_expr_binop','test.py',60),
  ('expr -> NUMBER','expr',1,'p_expr_number','test.py',64),
  ('expr -> ID','expr',1,'p_expr_id','test.py',68),
]