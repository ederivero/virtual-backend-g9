-- Esto es un comentario
CREATE DATABASE pruebas;
-- Para indicar que bd voy a utilizar
USE pruebas;
CREATE TABLE personas(
    -- Ahora definiremos las columnas de la tabla personas
    -- las llaves primarias (primary key) siempre deben de ser UNICAS E
    -- IRREPETIBLES
    -- nombre_col tipo_dato [primary key | not null ]
    id int primary key not null auto_increment,
    -- el unique indica que si ingreso un valor, ese valor no se 
    -- puede repetir con otro ingresado anteriormente, mas no obliga al usuario
    -- a ingresarlo
    documento varchar(20) unique,
    tipo_documento enum('DNI', 'C.E.', 'PASAPORTE', 'S/ DOCUMENTO'),
    nombre varchar(25),
    apellido varchar(50),
    correo varchar(100) unique,
    sexo enum('FEMENINO', 'MASCULINO', 'OTRO') not null,
    fecha_nacimiento date
);
-- FORMA DE AGREGAR VALORES A LA BD
INSERT INTO personas (
        documento,
        tipo_documento,
        nombre,
        apellido,
        correo,
        fecha_nacimiento,
        sexo
    )
VALUES (
        '73500741',
        'DNI',
        'EDUARDO',
        'DE RIVERO',
        'ederiveroman@gmail.com',
        '1990-08-01',
        'MASCULINO'
    );
-- FORMA DE VISUALIZAR LOS DATOS DE UNA TABLA INDICANDO LAS COLUMNAS
SELECT documento,
    nombre,
    fecha_nacimiento
FROM personas;
-- FORMA DE VISUALIZAR TODAS LAS COLUMNAS DE UNA TABLA
SELECT *
FROM personas;
INSERT INTO personas (
        documento,
        tipo_documento,
        nombre,
        apellido,
        correo,
        fecha_nacimiento,
        sexo
    )
VALUES (
        null,
        'S/ DOCUMENTO',
        'JUAN',
        'MARTINEZ',
        'jmartinez@gmail.com',
        '1989-05-15',
        'OTRO'
    );
INSERT INTO personas (
        documento,
        tipo_documento,
        nombre,
        apellido,
        correo,
        fecha_nacimiento,
        sexo
    )
VALUES (
        '12345678',
        'C.E.',
        'MARIA',
        'PEREZ',
        'mperez@gmail.com',
        '1995-12-10',
        'FEMENINO'
    );
INSERT INTO personas (
        documento,
        tipo_documento,
        nombre,
        apellido,
        correo,
        fecha_nacimiento,
        sexo
    )
VALUES (
        '12345677',
        'C.E.',
        'EDUARDO',
        'PEREZ',
        'eperez@gmail.com',
        '1995-12-10',
        'FEMENINO'
    );
-- MODIFICAR ALGUNA COLUMNA DE LA TABLA (tiene algunas restricciones si es que ya tengo informacion grabada)
ALTER TABLE personas
MODIFY documento varchar(20) unique;
SELECT *
FROM personas
WHERE nombre = 'EDUARDO'
    AND sexo = 'MASCULINO';
-- ELIMINAR UN REGISTRO
DELETE FROM personas
WHERE correo = 'mperez@gmail.com';
SELECT *
from personas;
-- ACTUALIZAR UNO O VARIOS REGISTROS
UPDATE personas
SET nombre = 'RAMIRO'
WHERE id = 1;
CREATE TABLE medicos(
    id int primary key not null auto_increment,
    cmp varchar(5) unique not null,
    -- colegio medico del peru
    nombre varchar(30),
    apellido varchar(50)
);
CREATE TABLE historial_vacunaciones(
    id int primary key not null auto_increment,
    vacuna enum('PFIZER', 'SINOPHARM', 'ASTRAZENECA'),
    lote varchar(10),
    fecha date,
    medico_id int,
    paciente_id int,
    -- para crear las relaciones
    foreign key (medico_id) references medicos(id),
    foreign key (paciente_id) references personas(id)
);
INSERT INTO medicos (cmp, nombre, apellido)
VALUES ('1234', 'RAUL', 'MUÑOZ'),
    ('1236', 'ROSA', 'HIDALGO'),
    ('5829', 'SOFIA', 'ALEMAN');
select *
from pruebas.personas;
INSERT INTO historial_vacunaciones (vacuna, lote, medico_id, paciente_id, fecha)
VALUES ('PFIZER', '1234', 1, 1, '2021-07-24'),
    ('SINOPHARM', '1598', 2, 2, '2021-08-01'),
    ('ASTRAZENECA', '1959', 1, 5, '2021-08-24'),
    ('PFIZER', '1234', 1, 1, now()),
    ('SINOPHARM', '5948', 3, 2, now());
SELECT *
FROM historial_vacunaciones;
-- DEVOLVER TODOS LOS REGISTROS DE HISTORIALES DE VACUNACION QUE SEAN PFIZER O ASTRAZENECA
SELECT *
FROM historial_vacunaciones
WHERE vacuna = 'PFIZER'
    OR vacuna = 'ASTRAZENECA';
SELECT *
FROM historial_vacunaciones
WHERE vacuna IN ('PFIZER', 'ASTRAZENECA');
-- DELETE FROM HISTORIAL_VACUNACIONES;
-- set SQL_SAFE_UPDATES = 1;