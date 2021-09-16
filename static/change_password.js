const pwd1 = document.getElementById("pwd1");
const pwd2 = document.getElementById("pwd2");
const btnEnviar = document.getElementById("btn-enviar");
const correo = document.getElementById("correo");
const formulario = document.getElementById("form-pwd");

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
      email: correo.innerText,
      password: pwd1.value,
    }),
  });

  const json = await respuesta.json();
  console.log(respuesta.status);
  console.log(json);
  if (respuesta.status === 400) {
    swal({
      title: json.message,
      icon: "error",
    });
  } else {
    swal({
      title: json.message,
      icon: "success",
    });
    formulario.remove();
  }
};
