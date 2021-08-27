-- continuamos con la clase

USE pruebas;

-- TRAEME TODAS LAS COLUMAS DE LA TABLA HISTORIA_VACUNACIONES Y MEDICOS CUANDO HIS_VAC.MEDICO_ID SEA IGUAL
-- QUE MEDICOS_ID
SELECT * FROM historial_vacunaciones 
		INNER JOIN medicos 
			ON historial_vacunaciones.medico_id = medicos.id
		INNER JOIN personas
			ON historial_vacunaciones.paciente_id = personas.id;
            
-- SIRVE PARA VER LA DESCRIPCION DE LA TABLA 
DESC MEDICOS;
            
INSERT INTO MEDICOS (CMP, NOMBRE, APELLIDO) VALUES ('129', 'JUAN', 'ZEGARRA'); 
            
DESC HISTORIAL_VACUNACIONES;

INSERT INTO HISTORIAL_VACUNACIONES (VACUNA, LOTE, FECHA, PACIENTE_ID) 
							VALUES ('ASTRAZENECA','15964', now(), 5);

SELECT * FROM HISTORIAL_VACUNACIONES;


-- consulta para saber que medico es el id=1
SELECT * FROM MEDICOS where id = 1;



-- LEFT JOIN (todo lo que concierne en el lado izquierdo y adicionalmente si esta en el
-- lado derecho
SELECT * FROM MEDICOS LEFT JOIN HISTORIAL_VACUNACIONES
					ON MEDICOS.ID = HISTORIAL_VACUNACIONES.MEDICO_ID;

-- RIGHT JOIN (todo lo que concierne en el lado DERECHO y adicionalmente si esta en el
-- lado IZQUIERDO
SELECT * FROM MEDICOS RIGHT JOIN HISTORIAL_VACUNACIONES
					ON MEDICOS.ID = HISTORIAL_VACUNACIONES.MEDICO_ID;




