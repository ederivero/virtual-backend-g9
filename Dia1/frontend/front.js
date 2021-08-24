console.log("Hola");
const BASE_URL = "http://127.0.0.1:8000";

fetch(BASE_URL + "/", { method: "GET" }).then((respuesta) => {
  console.log(respuesta.status); // 200
});
