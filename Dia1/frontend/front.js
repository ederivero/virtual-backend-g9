const BASE_URL = "http://127.0.0.1:8000";
const btnProductos = document.getElementById("btn-traer-productos");
const nombre_producto = document.getElementById("nom_producto");
const precio_producto = document.getElementById("prec_producto");
const nombre_producto_actualizar = document.getElementById(
  "nom_producto_actualizar"
);
const precio_producto_actualizar = document.getElementById(
  "prec_producto_actualizar"
);
const id_producto_actualizar = document.getElementById(
  "id_producto_actualizar"
);
const btnAgregar = document.getElementById("btn-agregar-producto");
const productosTable = document.getElementById("productos");

fetch(BASE_URL + "/", { method: "GET" }).then((respuesta) => {
  console.log(respuesta.status); // 200
});

btnProductos.onclick = (e) => {
  // agregar codigo para solicitar los productos
  fetch(BASE_URL + "/productos", { method: "GET" })
    .then((respuesta) => {
      return respuesta.json();
    })
    .then((productos) => {
      console.log(productos);
    });
};

async function traerProductos() {
  console.log("Me hizo click 2");
  const respuesta = await fetch(BASE_URL + "/productos", { method: "GET" });
  const productos = await respuesta.json();

  const tbody = document.createElement("tbody");
  productos.content.forEach((producto, index) => {
    console.log(producto);
    const tr = document.createElement("tr");
    const td_id = document.createElement("td");
    const td_nombre = document.createElement("td");
    const td_precio = document.createElement("td");
    const td_acciones = document.createElement("td");

    td_id.innerText = index;
    td_nombre.innerText = producto.nombre;
    td_precio.innerText = producto.precio;
    td_acciones.innerHTML = `<button type="button" class="btn btn-danger" onclick="eliminar(${index})">Eliminar</button>
    <button type="button" class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#exampleModal" onclick="editar(1)">Editar</button>`;

    tr.appendChild(td_id);
    tr.appendChild(td_nombre);
    tr.appendChild(td_precio);
    tr.appendChild(td_acciones);
    tbody.appendChild(tr);
  });
  productosTable.innerHTML = `<thead>
  <tr>
    <th scope="col">#</th>
    <th scope="col">Nombre</th>
    <th scope="col">Precio</th>
    <th scope="col">Acciones</th>
  </tr>
</thead>`;
  productosTable.appendChild(tbody);
}

btnProductos.addEventListener("click", traerProductos);

btnAgregar.onclick = async (e) => {
  e.preventDefault();
  console.log(nombre_producto.value);
  console.log(precio_producto.value);

  const respuesta = await fetch(BASE_URL + "/productos", {
    method: "POST",
    body: JSON.stringify({
      nombre: nombre_producto.value,
      precio: +precio_producto.value,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  });

  const resultado = await respuesta.json();

  console.log(resultado);
  traerProductos();
};

async function eliminar(index) {
  console.log(index);
  const respuesta = await fetch(BASE_URL + "/producto/" + index, {
    method: "DELETE",
  });
  const productos = await respuesta.json();
  console.log(productos);
  traerProductos();
}

function editar(producto) {
  console.log(producto);
  // nombre_producto_actualizar.innerText = producto.nombre;
  // precio_producto_actualizar.innerText = producto.precio;
  // id_producto_actualizar.innerText = id;
  console.log("a");
}
