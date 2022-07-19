DROP TABLE IF EXISTS tabla_raw;
CREATE TABLE IF NOT EXISTS tabla_raw(
    Cod_Localidad INT NOT NULL,
    Id_Provincia INT NOT NULL,
    Id_Departamento INT NOT NULL,
    Categoría VARCHAR(150) NOT NULL,
    Provincia VARCHAR(150) NOT NULL,
    Localidad VARCHAR(150) NOT NULL,
    Nombre VARCHAR(150) NOT NULL,
    Domicilio VARCHAR(200) NOT NULL,
    Código_postal VARCHAR(100) NOT NULL,
    Número_de_teléfono VARCHAR(150) NOT NULL,
    Mail VARCHAR(255) NOT NULL,
    Web VARCHAR(150) NOT NULL,
    Create_at VARCHAR(100)
);