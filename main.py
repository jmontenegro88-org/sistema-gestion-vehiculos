from vehiculo import Vehiculo

class Main:
    """
    Clase que gestiona una lista de vehículos, permitiendo agregar vehículos,
    buscarlos por año e imprimir todos los vehículos registrados.

    Atributos:
    ----------
    vehiculos : list
        Lista que almacena instancias de la clase Vehiculo.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de la clase Main con una lista vacía de vehículos.
        """
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        """
        Agrega un nuevo vehículo a la lista de vehículos.

        Parámetros:
        -----------
        vehiculo : Vehiculo
            Una instancia de la clase Vehiculo que se desea agregar a la lista.
        """
        self.vehiculos.append(vehiculo)
        print(f"Vehículo {vehiculo.get_marca()} {vehiculo.get_modelo()} agregado con éxito.")

    def buscar_vehiculos_por_año(self, año):
        """
        Busca y retorna una lista de vehículos que coincidan con el año proporcionado.

        Parámetros:
        -----------
        año : int
            El año de fabricación de los vehículos que se desean buscar.

        Retorna:
        --------
        list
            Una lista de instancias de la clase Vehiculo que coinciden con el año.
        """
        vehiculos_encontrados = [v for v in self.vehiculos if v.get_año() == año]
        
        if vehiculos_encontrados:
            print(f"Se encontraron {len(vehiculos_encontrados)} vehículos del año {año}:")
            for vehiculo in vehiculos_encontrados:
                print(f"- {vehiculo.get_marca()} {vehiculo.get_modelo()} (Kilometraje: {vehiculo.get_kilometraje()} km)")
        else:
            print(f"No se encontraron vehículos del año {año}.")

        return vehiculos_encontrados

    def imprimir_vehiculos_registrados(self):
        """
        Imprime todos los vehículos registrados, mostrando sus características
        como marca, modelo, año, kilometraje, estado actual y tipo de combustible.
        """
        if not self.vehiculos:
            print("No hay vehículos registrados.")
            return

        print("Lista de vehículos registrados:")
        for vehiculo in self.vehiculos:
            print(
                f"\nMarca: {vehiculo.get_marca()}, "
                f"\nModelo: {vehiculo.get_modelo()}, "
                f"\nAño: {vehiculo.get_año()}, "
                f"\nKilometraje: {vehiculo.get_kilometraje()} km, "
                f"\nEstado: {vehiculo.get_estado_actual()}, "
                f"\nTipo de Combustible: {vehiculo.get_tipo_combustible()}"
            )


def main():
    # Crear una instancia de Main
    print("\n\n-------Crear una instancia de Main--------")
    sistema_vehiculos = Main()

    # Crear algunos vehículos de prueba
    print("\n\n-------Crear algunos vehículos de prueba--------")
    vehiculo1 = Vehiculo("Toyota", "Corolla", 2020, 25000, "En buen estado", "Gasolina")
    vehiculo2 = Vehiculo("Honda", "Civic", 2020, 30000, "En buen estado", "Gasolina")
    vehiculo3 = Vehiculo("Ford", "Mustang", 2018, 15000, "En muy buen estado", "Gasolina")

    # Agregar vehículos al sistema
    print("\n\n-------Agregar vehículos al sistema--------")
    sistema_vehiculos.agregar_vehiculo(vehiculo1)
    sistema_vehiculos.agregar_vehiculo(vehiculo2)
    sistema_vehiculos.agregar_vehiculo(vehiculo3)

    # Buscar vehículos por año
    print("\n\n-------Buscar vehículos por año--------")
    sistema_vehiculos.buscar_vehiculos_por_año(2020)
    sistema_vehiculos.buscar_vehiculos_por_año(2019)

    print("\n\n-------Ejemplo vehiculo invalido--------")
    try:
        Vehiculo("Toyota", "Corolla", 2020, 25000, "En buen estado", "Agua") # Ejemplo vehiculo invalido
    except ValueError as e:
        print('Error:', e)

    vehiculo_valido = Vehiculo("Honda", "Civic", 2021, 15000, "En buen estado", "Gasolina")
    print(f"Vehículo creado con tipo de combustible: {vehiculo_valido.get_tipo_combustible()}")

    sistema_vehiculos.agregar_vehiculo(vehiculo_valido)
    sistema_vehiculos.buscar_vehiculos_por_año(2021)

    # Imprimir todos los vehículos registrados
    print("\n\n-------Imprimir todos los vehículos registrados--------")
    sistema_vehiculos.imprimir_vehiculos_registrados()

if __name__ == "__main__":
    main()
