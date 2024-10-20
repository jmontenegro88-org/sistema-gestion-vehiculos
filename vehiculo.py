class Vehiculo:
    """
    Clase que representa un vehículo con su información básica.

    Atributos:
    ----------
    marca : str
        Marca del vehículo.
    modelo : str
        Modelo del vehículo.
    año : int
        Año de fabricación del vehículo.
    kilometraje : int
        Kilometraje recorrido por el vehículo.
    estado_actual : str
        Estado actual del vehículo (e.g., "En buen estado", "Necesita mantenimiento").
    tipo_combustible : str
        Tipo de combustible que usa el vehículo (e.g., "Gasolina", "Diesel", "Eléctrico").
    """

    TIPOS_COMBUSTIBLE_VALIDOS = {"Gasolina", "Diesel", "Eléctrico"}

    def __init__(self, marca, modelo, año, kilometraje, estado_actual, tipo_combustible):
        """
        Inicializa una nueva instancia de la clase Vehiculo.

        Parámetros:
        -----------
        marca : str
            Marca del vehículo.
        modelo : str
            Modelo del vehículo.
        año : int
            Año de fabricación del vehículo.
        kilometraje : int
            Kilometraje recorrido por el vehículo.
        estado_actual : str
            Estado actual del vehículo.
        tipo_combustible : str
            Tipo de combustible que usa el vehículo.

        Lanza:
        ------
        ValueError:
            Si el tipo de combustible no es uno de los valores permitidos.
        """
        self._marca = marca
        self._modelo = modelo
        self._año = año
        self._kilometraje = kilometraje
        self._estado_actual = estado_actual
        self.set_tipo_combustible(tipo_combustible)

    # Getters
    def get_marca(self):
        """
        Obtiene la marca del vehículo.

        Retorna:
        --------
        str
            La marca del vehículo.
        """
        return self._marca

    def get_modelo(self):
        """
        Obtiene el modelo del vehículo.

        Retorna:
        --------
        str
            El modelo del vehículo.
        """
        return self._modelo

    def get_año(self):
        """
        Obtiene el año de fabricación del vehículo.

        Retorna:
        --------
        int
            El año de fabricación del vehículo.
        """
        return self._año

    def get_kilometraje(self):
        """
        Obtiene el kilometraje del vehículo.

        Retorna:
        --------
        int
            El kilometraje del vehículo en kilómetros.
        """
        return self._kilometraje

    def get_estado_actual(self):
        """
        Obtiene el estado actual del vehículo.

        Retorna:
        --------
        str
            El estado actual del vehículo.
        """
        return self._estado_actual

    def get_tipo_combustible(self):
        """
        Obtiene el tipo de combustible que usa el vehículo.

        Retorna:
        --------
        str
            El tipo de combustible del vehículo.
        """
        return self._tipo_combustible

    # Setters
    def set_marca(self, marca):
        """
        Establece la marca del vehículo.

        Parámetros:
        -----------
        marca : str
            La nueva marca del vehículo.
        """
        self._marca = marca

    def set_modelo(self, modelo):
        """
        Establece el modelo del vehículo.

        Parámetros:
        -----------
        modelo : str
            El nuevo modelo del vehículo.
        """
        self._modelo = modelo

    def set_año(self, año):
        """
        Establece el año de fabricación del vehículo.

        Parámetros:
        -----------
        año : int
            El nuevo año de fabricación del vehículo.
        """
        self._año = año

    def set_kilometraje(self, kilometraje):
        """
        Establece el kilometraje del vehículo.

        Parámetros:
        -----------
        kilometraje : int
            El nuevo kilometraje del vehículo en kilómetros.
        """
        self._kilometraje = kilometraje

    def set_estado_actual(self, estado_actual):
        """
        Establece el estado actual del vehículo.

        Parámetros:
        -----------
        estado_actual : str
            El nuevo estado del vehículo.
        """
        self._estado_actual = estado_actual

    def set_tipo_combustible(self, tipo_combustible):
        """
        Establece el tipo de combustible del vehículo.

        Parámetros:
        -----------
        tipo_combustible : str
            El nuevo tipo de combustible del vehículo.

        Lanza:
        ------
        ValueError:
            Si el tipo de combustible no es uno de los valores permitidos.
        """
        if tipo_combustible not in self.TIPOS_COMBUSTIBLE_VALIDOS:
            raise ValueError(
                f"Tipo de combustible inválido: {tipo_combustible}. "
                f"Debe ser uno de: {', '.join(self.TIPOS_COMBUSTIBLE_VALIDOS)}."
            )
        self._tipo_combustible = tipo_combustible
