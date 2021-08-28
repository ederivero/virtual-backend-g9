-- 1. Trae todas las personas cuyo nombre sea Kevin
SELECT * FROM personales where nombre = 'Kevin';
-- 2. Traer todas las personas cuyo departamento sea el 2
SELECT * FROM personales where departamento_id = 2;

-- 3. Del ejercicio numer 2, agregar el nombre del departamento (
-- no solamente diga departamento_id = 2 | "PUBLICIDAD"

-- solamente quiero el nombre y apellido del personal y el nombre del
-- departamento
SELECT personales.nombre as nombre_personal, 
		personales.apellido as apellido_personal, 
        departamentos.nombre as nombre_departamento
FROM PERSONALES INNER JOIN DEPARTAMENTOS 
			ON PERSONALES.departamento_id = DEPARTAMENTOS.id
where departamento_id = 2;


SELECT p.nombre as nombre_personal, 
		p.apellido as apellido_personal, 
        d.nombre as nombre_departamento
FROM PERSONALES as p INNER JOIN DEPARTAMENTOS as d
			ON p.departamento_id = d.id
where departamento_id = 2;


-- NOMBRE_EMPLEADO | APELLIDO_EMPLEADO | NOMBRE_SUPERVISOR | APELLIDO_SUPERVISOR | NOMBRE_DEPARTAMENTO_EMP
SELECT 	p.nombre as NOMBRE_EMPLEADO,
		p.apellido as APELLIDO_EMPLEADO,
        s.nombre as NOMBRE_SUPERVISOR,
        s.apellido as APELLIDO_SUPERVISOR,
        d.nombre as NOMBRE_DEPARTAMENTO_EMPLEADO
from personales as p left JOIN personales as s
	on p.supervisor_id = s.id
    inner join departamentos as d
    on p.departamento_id = d.id
;

-- 	1	69c6a057-b82e-448a-aa4a-5f49c4b70a39	Brittany	Christensen	1	
SELECT * from personales;

DROP DATABASE pruebas;
