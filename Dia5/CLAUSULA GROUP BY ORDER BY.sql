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
-- FROM TABLAS [JOIN]
-- [WHERE CONDICION]
-- [GROUP BY AGRUPAMIENTOS]
-- [ORDER BY COL ASC | DESC]
-- LIMIT 0
-- OFFSET 0;

use calificaciones;
-- Traer 
-- NOMBRE_ALUMNO | APELLIDO_ALUMNO | NOMBRE_CURSO | ESTADO_CURSO
SELECT alumnos.nombre as NombreAlumno, alumnos.apellido as ApellidoAlumno, 
		cursos.nombre as NombreCurso, cursos.estado as EstadoCurso
FROM ALUMNOS
INNER JOIN ALUMNOS_CURSOS ON alumnos.id = alumnos_cursos.id_alumno
INNER JOIN cursos ON cursos.id = alumnos_cursos.id_curso;

-- SABER CUANTOS ALUMNOS ESTAN INSCRITOS EN CADA CURSO

select * from cursos;
-- que este ordenado de mas a menos alumnos inscritos y si es el mismo numero
-- de alumnos inscritos que me de los cursos ordenados alfabeticamente
-- CURSO_NOMBRE | ALUMNOS_INSCRITOS 
SELECT count(id_alumno) as ALUMNOS_INSCRITOS, nombre as CURSO_NOMBRE
from alumnos_cursos INNER JOIN cursos 
	ON alumnos_cursos.id_curso = cursos.id
group by nombre
order by 1 desc, 2 asc;

-- para el order by se puede poner los siguiente valores en relacion a los nombres
-- de las columnas
-- nombre original | alias | numero de la columna empezando en 1









