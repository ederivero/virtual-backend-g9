use empresa;

select count(departamento_id), departamento_id, nombre
from personales
group by departamento_id, nombre;

select departamento_id, nombre,  count(departamento_id)
from personales
group by nombre, departamento_id 
order by departamento_id;

-- MOSTRAR CUANTOS EMPLEADOS HAY EN EL DEPARTAMENTO = 2
SELECT 'departamento 2' departamento, count(*) total
from personales 
where departamento_id = 2;


-- MOSTRAR CUANTAS PERSONAS NO TIENE JEFE
-- TOTAL
--   20
SELECT COUNT(*) TOTAL
FROM PERSONALES
WHERE SUPERVISOR_ID IS NULL;


-- DE ESAS PERSONAS INDICAR DE QUE DEPARTAMENTOS SON ORDENADO DE MAYOR
-- A MENOR
-- DEPARTAMENTO | TOTAL
-- 		1			10
-- 		2			4
-- 		3			2
--      4 			4
SELECT COUNT(*) TOTAL, DEPARTAMENTO_ID
FROM PERSONALES
WHERE SUPERVISOR_ID IS NULL
GROUP BY DEPARTAMENTO_ID
ORDER BY 1 DESC;

-- Mostrar el nombre del departamento y su cantidad de empleados

-- DEPARTAMENTO 	|  CANTIDAD DE EMPLEADOS
-- Ventas			|   		150
-- Administracion	|   		200
-- Finanzas			|   		85
-- Marketing		|   		56


SELECT departamentos.nombre, count(personales.id) as 'CANTIDAD DE EMPLEADOS'
FROM departamentos inner join personales
	on departamentos.id = personales.departamento_id
GROUP BY departamentos.nombre;

















