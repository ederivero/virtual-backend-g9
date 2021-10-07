// CRUD ACTIVIDADES
const actividades = [];

export const crearActividad = (req, res) => {
  console.log(req.body); // me dara todo el body enviado por el usuario
  const { body } = req;
  actividades.push(body);

  return res.status(201).json({
    message: "Actividad creada exitosamente",
    content: body,
  });
};

export const listarActividades = (req, res) => {
  return res.status(200).json({
    message: "Las actividades son:",
    content: actividades,
  });
};
