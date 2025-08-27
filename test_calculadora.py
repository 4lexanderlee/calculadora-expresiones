from calculadoraexpresiones import evaluar_expresion

def test_suma_simple():
    assert evaluar_expresion("2+3") == 5

def test_orden_operaciones():
    assert evaluar_expresion("2+3*4") == 14  # 3*4=12 → 2+12=14
