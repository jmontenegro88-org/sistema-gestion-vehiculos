from vehiculo import Vehiculo

class Main:
    """
    Clase que gestiona una lista de vehículos, permitiendo agregar vehículos
    y buscarlos por año.

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

def main():
    # Crear una instancia de Main
    sistema_vehiculos = Main()

    # Crear algunos vehículos de prueba
    vehiculo1 = Vehiculo("Toyota", "Corolla", 2020, 25000, "En buen estado", "Gasolina")
    vehiculo2 = Vehiculo("Honda", "Civic", 2020, 30000, "En buen estado", "Gasolina")
    vehiculo3 = Vehiculo("Ford", "Mustang", 2018, 15000, "En muy buen estado", "Gasolina")

    # Agregar vehículos al sistema
    sistema_vehiculos.agregar_vehiculo(vehiculo1)
    sistema_vehiculos.agregar_vehiculo(vehiculo2)
    sistema_vehiculos.agregar_vehiculo(vehiculo3)

    # Buscar vehículos por año
    sistema_vehiculos.buscar_vehiculos_por_año(2020)
    sistema_vehiculos.buscar_vehiculos_por_año(2019)

    try:
        Vehiculo("Toyota", "Corolla", 2020, 25000, "En buen estado", "Agua") # Ejemplo vehiculo invalido
    except ValueError as e:
        print('Error:', e)

    vehiculo_valido = Vehiculo("Honda", "Civic", 2021, 15000, "En buen estado", "Gasolina")
    print(f"Vehículo creado con tipo de combustible: {vehiculo_valido.get_tipo_combustible()}")

    sistema_vehiculos.agregar_vehiculo(vehiculo_valido)
    sistema_vehiculos.buscar_vehiculos_por_año(2021)

if __name__ == "__main__":
    main()
