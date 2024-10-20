
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
````
