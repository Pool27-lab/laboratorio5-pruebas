class ProcesadorPagos:

    def calcular_total(self, monto, impuesto):
        return monto + (monto * impuesto)

    def validar_limite(self, monto):
        return monto <= 5000

    def procesar_reembolso(self, dias):
        return dias <= 30