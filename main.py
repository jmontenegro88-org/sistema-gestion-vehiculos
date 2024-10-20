from vehiculo import Vehiculo

def main():
    # Crear una instancia de Vehiculo
    mi_vehiculo = Vehiculo(
        marca="Toyota",
        modelo="Corolla",
        año=2020,
        kilometraje=25000,
        estado_actual="En buen estado",
        tipo_combustible="Gasolina"
    )

    # Imprimir detalles del vehículo usando getters
    print("Detalles del vehículo:")
    print(f"Marca: {mi_vehiculo.get_marca()}")
    print(f"Modelo: {mi_vehiculo.get_modelo()}")
    print(f"Año: {mi_vehiculo.get_año()}")
    print(f"Kilometraje: {mi_vehiculo.get_kilometraje()} km")
    print(f"Estado Actual: {mi_vehiculo.get_estado_actual()}")
    print(f"Tipo de Combustible: {mi_vehiculo.get_tipo_combustible()}")

    # Modificar algún atributo usando setters
    mi_vehiculo.set_kilometraje(30000)
    print("\nKilometraje actualizado:")
    print(f"Kilometraje: {mi_vehiculo.get_kilometraje()} km")

if __name__ == "__main__":
    main()
