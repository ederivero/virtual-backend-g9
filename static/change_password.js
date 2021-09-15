const pwd1 = document.getElementById("pwd1");
const pwd2 = document.getElementById("pwd2");
const btnEnviar = document.getElementById("btn-enviar");

btnEnviar.onclick = async (e) => {
  if (pwd1.value !== pwd2.value) {
    alert("Las contraseñas no coinciden");
    return;
  }

  const respuesta = await fetch("/change-password", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email: "",
      password: pwd1.value,
    }),
  });

  const json = await respuesta.json();
  console.log(json);
};
