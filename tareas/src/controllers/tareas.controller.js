import { Tarea } from "../config/models";

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
