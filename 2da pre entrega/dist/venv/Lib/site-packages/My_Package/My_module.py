class Cliente:
    def __init__(self, nombre, edad, direccion, saldo_inicial):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.saldo = saldo_inicial

    def comprar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"{self.nombre} ha realizado una compra por ${monto}. Saldo restante: ${self.saldo}")
            return True
        else:
            print(f"{self.nombre} no tiene suficiente saldo para realizar la compra.")
            return False 

    def recargar_saldo(self, monto_recarga):
        self.saldo += monto_recarga
        print(f"{self.nombre} ha recargado saldo por ${monto_recarga}. Saldo actual: ${self.saldo}")

    def __str__(self):
        return f"Cliente: {self.nombre}, Edad: {self.edad}, Dirección: {self.direccion}, Saldo: ${self.saldo}"


def main():
    from My_Package import My_module, static

    print(static.SUBE_IMAGE)

    saldo_cliente = int(input("Ingrese saldo cliente en pesos "))

    saldo_kiosko = int(input("Ingrese saldo kiosko en pesos "))

    Cliente_ID_1 = My_module.Cliente("Alex", 27, "a la vuelta de la casa del kioskero", saldo_cliente)

    Cliente_ID_2 = My_module.Cliente("kioskero", 33, "a la vuelta de la casa de Alex", saldo_kiosko)

    print(Cliente_ID_1)
    print()
    print(Cliente_ID_2)


    while True:

        print("""
        Elija una opcion para continuar: 

        1. gastar en kiosko
        2. recargar billetera de usuario
        3. recargar billetera de kiosko
        4. status de usuarios
        5. exit

        """)

        option = input("\n")

        if int(option) == 1:
            monto_compra = int(input("\nIngrese monto gastado en kiosko\n"))

            if Cliente_ID_1.comprar(monto_compra):
                Cliente_ID_2.recargar_saldo(monto_compra)

        elif int(option) == 2:
            monto_recarga = int(input("\nIngrese recarga en billetera usuario\n"))  
            Cliente_ID_1.recargar_saldo(monto_recarga)

        elif int(option) == 3:
            monto_recarga = int(input("\nIngrese recarga en billetera kiosko\n"))  
            Cliente_ID_2.recargar_saldo(monto_recarga)

        elif int(option) == 4:
            print(Cliente_ID_1)
            print()
            print(Cliente_ID_2)

        elif int(option) == 5:
            break


if __name__ == "__main__":
    main()