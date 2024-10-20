
# Guía de Estilo de Código

## 1. Nombres de Variables y Funciones
- **Variables**: Utilizar el estilo camelCase para los nombres de variables, por ejemplo: `miVariable`, `nombreUsuario`.
- **Funciones/Clases**: Usar PascalCase para los nombres de clases y métodos, por ejemplo: `ClaseVehiculo`, `HistorialMantenimiento`.

## 2. Reglas de Indentación
- **Espacios vs. Tabuladores**: Usar 4 espacios por nivel de indentación. No utilizar tabuladores.

## 3. Longitud Máxima de Líneas de Código
- Mantener una longitud máxima de 80 caracteres por línea de código para asegurar que sea fácil de leer.

## 4. Formato de Comentarios y Documentación
- **Comentarios en línea**: Utilizar `//` para comentarios en línea que expliquen partes específicas del código.
- **Comentarios de bloque**: Utilizar `/* */` para comentarios de bloque y documentar funciones o clases con una breve descripción de lo que hacen.

## 5. Nombres de Commits
Los nombres de los commits deben seguir las reglas de Conventional Commits, estructurados de la siguiente manera:

```
tipo: Descripción del cambio
```

- **Ejemplos**:
  - `feat: añadir funcionalidad de búsqueda de vehículos por año`
  - `fix: corregir error en la validación de tipo de combustible`
  - `docs: agregar estilo de codificación a CODESTYLE.md`

- **Tipos de commits permitidos**:
  - `feat`: Para nuevas características o funcionalidades.
  - `fix`: Para correcciones de errores.
  - `docs`: Para cambios en la documentación.
  - `style`: Para cambios que no afectan la lógica del código (e.g., formato, estilo).
  - `refactor`: Para refactorizaciones del código.

## 6. Nombres de Ramas
- Utilizar una convención de nombres para las ramas, basados en las funcionalidades que se están desarrollando. Por ejemplo:
  - `feat/<nombre-funcionalidad>`: Para el desarrollo de nuevas características.
  - `fix/<descripción-error>`: Para corregir errores.
  - `docs/<actualización-documentación>`: Para cambios en la documentación.

## 7. Ejemplos:
- `feat/agregar-vehiculo`
- `fix/corregir-validacion-combustible`
- `docs/actualizar-readme`
