
# Sistema de Gestión de Vehículos

## Descripción del Proyecto

Este proyecto es una aplicación en Python diseñada para gestionar el inventario de una flota vehicular. La aplicación permite registrar, buscar y mantener información detallada sobre vehículos, incluyendo:

- Marca
- Modelo
- Año de fabricación
- Historial de mantenimiento
- Color
- Potencia del vehículo

La aplicación está organizada en varias etapas de desarrollo, empezando por la creación de clases como `Vehiculo` y `HistorialMantenimiento`, e incluye funcionalidades como la búsqueda de vehículos por año o rango de años.

## Requisitos

- Python 3.8 o superior
- Git (para control de versiones)

## Instalación

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/jmontenegro88-org/sistema-gestion-vehiculos.git
cd sistema-gestion-vehiculos
```

### Paso 2: Crear y Activar el Entorno Virtual

#### En Windows:

```bash
python -m venv env
env\Scripts\activate
```

#### En MacOS/Linux:

```bash
python3 -m venv env
source env/bin/activate
```

### Paso 3: Ejecutar la Aplicación

```bash
python main.py
```

## Funcionalidades

- **Registro de Vehículos**: Permite añadir vehículos al sistema con sus respectivas características.
- **Búsqueda de Vehículos**: Búsqueda de vehículos por año de fabricación o rango de años.
- **Historial de Mantenimiento**: Registro y consulta del historial de mantenimiento de cada vehículo.
- **Filtrado por Características**: Búsqueda por características como color y potencia.

## Integrantes del Grupo

| Nombre de Usuario | Correo Electrónico                        |
|-------------------|-------------------------------------------|
| UsuarioA          | johnmontenegro33@gmail.com                |
| UsuarioB          | jmontenegro8@udenar.edu.co                |
| UsuarioC          | jhon.montenegrorosero@u.icesi.edu.co      |

## Contribución

Cada integrante del grupo ha colaborado en diferentes partes del proyecto, usando Git para el control de versiones, lo que ha permitido el desarrollo paralelo y la resolución de conflictos de manera eficiente.

## Ejemplos de Uso

### Calcular la Antigüedad de un Vehículo

La antigüedad de un vehículo se calcula utilizando el año actual y el año de fabricación del vehículo.

```python
from datetime import datetime

def calcular_antiguedad(vehiculo):
    año_actual = datetime.now().year
    return año_actual - vehiculo.get_año()

# Ejemplo de uso:
vehiculo = Vehiculo("Toyota", "Corolla", 2020, 25000, "En buen estado", "Gasolina")
antiguedad = calcular_antiguedad(vehiculo)
print(f"La antigüedad del vehículo {vehiculo.get_marca()} {vehiculo.get_modelo()} es de {antiguedad} años.")
```

### Ahora puedes buscar vehículos fabricados antes o después de un año específico utilizando los siguientes métodos:

#### Buscar Vehículos Fabricados Antes o Después de un Año

Para buscar vehículos que sean fabricados después de un año específico:

```python
# Buscar vehículos fabricados después del año 2019
sistema_vehiculos.buscar_vehiculos_mayores_a(2019)
# Buscar vehículos fabricados antes del año 2020
sistema_vehiculos.buscar_vehiculos_menores_a(2020)
```
## Atributos de Vehículo

Cada instancia de la clase `Vehiculo` cuenta con los siguientes atributos:

- **Marca**: Marca del vehículo (e.g., "Toyota").
- **Modelo**: Modelo del vehículo (e.g., "Corolla").
- **Año**: Año de fabricación del vehículo.
- **Kilometraje**: Kilometraje recorrido por el vehículo.
- **Estado Actual**: Estado actual del vehículo (e.g., "En buen estado").
- **Tipo de Combustible**: Tipo de combustible utilizado por el vehículo (e.g., "Gasolina", "Diesel", "Eléctrico").
- **Color**: Color del vehículo (e.g., "Rojo").

### Ejemplo de Uso

```python
# Crear una instancia de Vehiculo con el nuevo atributo 'color'
vehiculo = Vehiculo(
    marca="Toyota",
    modelo="Corolla",
    año=2020,
    kilometraje=25000,
    estado_actual="En buen estado",
    tipo_combustible="Gasolina",
    color="Rojo"
)

# Obtener el color del vehículo
print(f"El color del vehículo es: {vehiculo.get_color()}")