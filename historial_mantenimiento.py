class HistorialMantenimiento:
    """
    Clase que representa el historial de mantenimiento de un vehículo.

    Atributos:
    ----------
    fecha : str
        Fecha en la que se realizó el mantenimiento o reparación.
    descripcion_servicio : str
        Descripción del servicio realizado.
    kilometraje_en_servicio : int
        Kilometraje del vehículo en el momento del mantenimiento.
    costo : float
        Costo del servicio de mantenimiento.
    nombre_mecanico : str
        Nombre del mecánico que realizó el servicio.
    """

    def __init__(self, fecha, descripcion_servicio, kilometraje_en_servicio, costo, nombre_mecanico):
        """
        Inicializa una nueva instancia de la clase HistorialMantenimiento.

        Parámetros:
        -----------
        fecha : str
            Fecha en la que se realizó el mantenimiento o reparación.
        descripcion_servicio : str
            Descripción del servicio realizado.
        kilometraje_en_servicio : int
            Kilometraje del vehículo en el momento del mantenimiento.
        costo : float
            Costo del servicio de mantenimiento.
        nombre_mecanico : str
            Nombre del mecánico que realizó el servicio.
        """
        self._fecha = fecha
        self._descripcion_servicio = descripcion_servicio
        self._kilometraje_en_servicio = kilometraje_en_servicio
        self._costo = costo
        self._nombre_mecanico = nombre_mecanico

    # Getters
    def get_fecha(self):
        """
        Obtiene la fecha del mantenimiento.

        Retorna:
        --------
        str
            La fecha del mantenimiento.
        """
        return self._fecha

    def get_descripcion_servicio(self):
        """
        Obtiene la descripción del servicio realizado.

        Retorna:
        --------
        str
            La descripción del servicio.
        """
        return self._descripcion_servicio

    def get_kilometraje_en_servicio(self):
        """
        Obtiene el kilometraje del vehículo al momento del mantenimiento.

        Retorna:
        --------
        int
            El kilometraje del vehículo.
        """
        return self._kilometraje_en_servicio

    def get_costo(self):
        """
        Obtiene el costo del mantenimiento.

        Retorna:
        --------
        float
            El costo del servicio.
        """
        return self._costo

    def get_nombre_mecanico(self):
        """
        Obtiene el nombre del mecánico que realizó el servicio.

        Retorna:
        --------
        str
            El nombre del mecánico.
        """
        return self._nombre_mecanico

    # Setters
    def set_fecha(self, fecha):
        """
        Establece la fecha del mantenimiento.

        Parámetros:
        -----------
        fecha : str
            La nueva fecha del mantenimiento.
        """
        self._fecha = fecha

    def set_descripcion_servicio(self, descripcion_servicio):
        """
        Establece la descripción del servicio realizado.

        Parámetros:
        -----------
        descripcion_servicio : str
            La nueva descripción del servicio.
        """
        self._descripcion_servicio = descripcion_servicio

    def set_kilometraje_en_servicio(self, kilometraje_en_servicio):
        """
        Establece el kilometraje del vehículo al momento del mantenimiento.

        Parámetros:
        -----------
        kilometraje_en_servicio : int
            El nuevo kilometraje del vehículo.
        """
        self._kilometraje_en_servicio = kilometraje_en_servicio

    def set_costo(self, costo):
        """
        Establece el costo del mantenimiento.

        Parámetros:
        -----------
        costo : float
            El nuevo costo del servicio.
        """
        self._costo = costo

    def set_nombre_mecanico(self, nombre_mecanico):
        """
        Establece el nombre del mecánico que realizó el servicio.

        Parámetros:
        -----------
        nombre_mecanico : str
            El nuevo nombre del mecánico.
        """
        self._nombre_mecanico = nombre_mecanico
