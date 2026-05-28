from pagos import ProcesadorPagos

def test_calcular_total():
    servicio = ProcesadorPagos()

    resultado = servicio.calcular_total(100, 0.18)

    assert resultado == 118


def test_validar_limite_valido():
    servicio = ProcesadorPagos()

    resultado = servicio.validar_limite(3000)

    assert resultado is True


def test_validar_limite_invalido():
    servicio = ProcesadorPagos()

    resultado = servicio.validar_limite(7000)

    assert resultado is False


def test_reembolso_permitido():
    servicio = ProcesadorPagos()

    resultado = servicio.procesar_reembolso(20)

    assert resultado is True


def test_reembolso_rechazado():
    servicio = ProcesadorPagos()

    resultado = servicio.procesar_reembolso(45)

    assert resultado is False