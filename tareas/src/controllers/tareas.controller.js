import { Tarea } from "../config/models";

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
