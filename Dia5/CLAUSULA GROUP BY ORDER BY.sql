-- PARECIESE
-- LOS NOMBRE QUE EMPIECEN CON LA LETRA A
SELECT * FROM ALUMNOS WHERE NOMBRE LIKE 'A%';
-- LOS NOMBRES QUE TERMINEN CON LA LETRA A
SELECT * FROM ALUMNOS WHERE NOMBRE LIKE '%A';
-- LOS NOMBRES QUE CONTENGAN LA LETRA A
SELECT * FROM ALUMNOS WHERE NOMBRE LIKE '%A%';
-- LOS NOMBRES QUE EMPIECEN CON LA LETRA A Y QUE CONTENGAN LA LETRA E
SELECT * FROM ALUMNOS WHERE NOMBRE LIKE 'A%E%';

-- TODOS LOS ALUMNOS CUYO CORREO SEA HOTMAIL
SELECT * FROM ALUMNOS WHERE CORREO LIKE '%hotmail%';

-- FUNCION DE AGREGACION
-- son funciones de SQL que se usan para calculos en multiples valores realizados
-- por un select y retorna un unico valor
-- NOTA: si usamos una funcion de agregacion esta tiene que ir acompañada de la clausula
-- GROUP BY en los casos que agreguemos una columna adicional que no tenga nada que ver
-- con la funcion de agregacion (tambien se puede usar la clausula having by)
SELECT count(correo), nombre 
from alumnos 
where correo like '%hotmail%'
group by nombre;

select correo, nombre from alumnos where correo like '%hotmail%';


SELECT count(nombre) total, nombre
from alumnos
group by nombre
-- EL ORDER BY SIEMPRE VA DESPUES DEL GROUP BY y del WHERE o FROM 
order by total desc, nombre asc;

-- SELECT COLUMNAS | *
-- [WHERE CONDICION]
-- FROM TABLAS [JOIN]
-- [GROUP BY AGRUPAMIENTOS]
-- [ORDER BY COL ASC | DESC];

-- Traer 
-- NOMBRE_ALUMNO | APELLIDO_ALUMNO | NOMBRE_CURSO | ESTADO_CURSO


