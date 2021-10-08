// CRUD ACTIVIDADES
const actividades = [
  {
    nombre: "Ir al gimnasio",
    hora: "6:00",
    dias: ["LUN", "MIE", "VIE"],
  },
  {
    nombre: "Aprender MongoDb",
    hora: "22:00",
    dias: ["MAR", "SAB"],
  },
];

// Documentacion del request http://expressjs.com/en/5x/api.html#req
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

export const devolverActividad = (req, res) => {
  console.log(req.params);
  const { id } = req.params;
  // buscar en el array esa posicion y si no hay retornar una res con estado 404
  //{
  //   message: 'Actividad no encontrada'
  //}
  // y si si existe entonces retornar esa actividad
  if (actividades.length > id) {
    return res.json({
      message: null,
      content: actividades[id],
    });
  } else {
    return res.status(404).json({
      message: "Actividad no encontrada",
      content: null,
    });
  }
};

export const actualizarActividad = (req, res) => {
  const { id } = req.params;
  if (actividades.length > id) {
    actividades[id] = req.body;

    return res.json({
      message: "actividad actualizada exitosamente",
      content: actividades[id],
    });
  } else {
    return res.status(404).json({
      message: "No se encontro la actividad a actualizar",
      content: null,
    });
  }
};

export const eliminarActividad = (req, res) => {
  const { id } = req.params;

  if (actividades.length > id) {
    actividades.splice(id, 1);
    return res.json({
      message: "Actividad eliminada exitosamente",
      content: actividades,
    });
  } else {
    return res.status(404).json({
      message: "No se encontro la actividad",
      content: null,
    });
  }
};
