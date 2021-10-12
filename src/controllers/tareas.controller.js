import { Tarea } from "../config/models";
import { Op } from "sequelize";

// esto es un middleware porque tenemos el metodo next declarado y este indicara que si la data es correcta podra continuar, caso contrario indicar el error
export const serializadorTarea = (req, res, next) => {
  const data = req.body;
  const dataTarea = {
    tareaNombre: data.nombreTarea,
    tareaDias: data.diasTarea,
    tareaHora: data.horaTarea,
  };

  if (dataTarea.tareaNombre) {
    req.body = dataTarea;
    next();
  } else {
    return res.status(400).json({
      message: "Falta el nombreTarea",
      content: null,
    });
  }
};

export const crearTarea = async (req, res) => {
  // registrar una nueva tarea
  const data = req.body;
  try {
    const nuevaTarea = await Tarea.create(data);
    return res.status(201).json({
      message: "Tarea creada exitosamente",
      content: nuevaTarea,
    });
  } catch (error) {
    return res.status(500).json({
      message: "error al crear la tarea",
      content: error,
    });
  }
};

export const listarTareas = async (req, res) => {
  // https://sequelize.org/master/manual/model-querying-finders.html
  const tareas = await Tarea.findAll();

  return res.json({
    content: tareas,
    message: null,
  });
};

export const actualizarTarea = async (req, res) => {
  // extraigo de la url el id enviado para modificar la tarea
  const { id } = req.params;

  // UPDATE tareas SET .... WHERE id = id;
  const [total, model] = await Tarea.update(req.body, {
    where: { tareaId: id },
    returning: true,
  });

  // console.log(total);
  // console.log(model);
  // validar si se actualizo algun registro (total muestra cuantos registros se modificaron)
  // si no se actualizo retornar un 404
  if (total === 0) {
    return res.status(404).json({
      message: "No se encontro tarea a actualizar",
      content: null,
    });
  }

  // retornar el registro actualizado (model muestra los registros actualizados, en este caso SIEMPRE sera 1 porque estamos usando la clausula de la PK)
  // content: {...}
  return res.json({
    message: "Tarea actualizada exitosamente",
    content: model[0],
  });
};

export const eliminarTarea = async (req, res) => {
  const { id } = req.params;
  const resultado = await Tarea.destroy({ where: { tareaId: id } });
  // operador ternario
  const message =
    resultado !== 0
      ? "Tarea eliminada exitosamente"
      : "No se encontro la tarea a eliminar";
  console.log(resultado);

  return res.status(resultado !== 0 ? 200 : 404).json({
    message,
  });
};

export const devolverTarea = async (req, res) => {
  const { id } = req.params;
  // buscara UNA SOLA INSTANCIA y si es que la encuentra, la devolvera , caso contrario, dara null
  const tarea = await Tarea.findOne({ where: { tareaId: id } });

  return res.json({
    // si tarea == null entonces el message sera null caso contrario indicara 'Tarea no encontrada'
    message: tarea ? null : "Tarea no encontrada",
    content: tarea,
  });
};

export const filtrarTareas = async (req, res) => {
  // /buscarTarea?dias=['Sab']
  // /buscarTarea?hora=09:00
  // /buscarTarea?hora=09:00&dias=['Sab']
  // /buscarTarea?nombre=ejercicio
  const { dias, hora, nombre } = req.query;
  // SELECT nombre FROM tareas WHERE nombre LIKE '%...%'

  let filtros = [];

  if (nombre) {
    filtros = [
      ...filtros,
      {
        tareaNombre: {
          [Op.iLike]: "%" + nombre + "%",
        },
      },
    ];
  }

  if (hora) {
    filtros = [
      ...filtros,
      {
        tareaHora: hora,
      },
    ];
  }

  if (dias) {
    // BUSCAR SI HAY UNA , (coma) Y SI LA HAY, HACER UN SPLIT con todos los elementos
    const dias_array = dias.split(",");

    filtros = [
      ...filtros,
      {
        tareaDias: {
          [Op.contains]: dias_array,
        },
      },
    ];
  }
  try {
    const tareas = await Tarea.findAll({
      where: {
        [Op.and]: filtros,
      },
      // si queremos indicar que columnas queremos retornar entonces usaremos el atributo attributes indicando en un array la lista de columnas a retornar, ademas si queremos modificar (añadir un alias) a la columna tendremos que agregar un array indicando como primer parametro el nombre de la col. en la bd y como segundo el alias
      // attributes: [["nombre", "nombrecito"], "tareaDias"],
      // si queremos EXCLUIR una determinada columna O columnas entonces ahora el attributes seria un objeto en el cual le tendriamos que indicar el exclude que sera un array de todas las columnas que no queremos mostrar
      // si usamos el exclude e include a la vez solamente tomara en cuenta el exclude
      attributes: {
        exclude: ["createdAt", "fecha_de_actualizacion"],
      },
      // logging: console.log,
    });

    return res.json({
      content: tareas,
    });
  } catch (e) {
    console.log(e);
    return res.json({
      message: "Valores incorrectos",
      content: [],
    });
  }
};
