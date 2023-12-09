const URL = "http://127.0.0.1:5000/"
// Capturamos el evento de envío del formulario
document.getElementById('formulario').addEventListener('submit', function
(event) {
event.preventDefault(); // Evitamos que se envie el form
var formData = new FormData();
formData.append('nombre_completo', document.getElementById('nombre').value);
formData.append('email',document.getElementById('email').value);
formData.append('telefono',document.getElementById('telefono').value);
formData.append('fecha', document.getElementById('fecha').value);
formData.append('cantidad_personas',document.getElementById('personas').value);
formData.append('sucursal',document.getElementById('sucursal').value);
formData.append('restricciones',document.getElementById('restricciones').value);
// Realizamos la solicitud POST al servidor
fetch('http://127.0.0.1:5000/reservas', {
method: 'POST',
body: formData // Aquí enviamos formData en lugar de JSON
})
//Después de realizar la solicitud POST, se utiliza el método then() para manejar la respuesta del servidor.
.then(function (response) {
if (response.ok) {
return response.json();
} else {
// Si hubo un error, lanzar explícitamente una excepción
// para ser "catcheada" más adelante
throw new Error('Error al agregar el reserva.');
}
})
// Respuesta OK
.then(function () {
// En caso de éxito
alert('Reserva agregada correctamente.');
})
.catch(function (error) {
// En caso de error
alert('Error al agregar la reserva.');
console.error('Error:', error);
})
.finally(function () {
// Limpiar el formulario en ambos casos (éxito o error)
document.getElementById('nombre').value = "";
document.getElementById('email').value = "";
document.getElementById('telefono').value = "";
document.getElementById('fecha').value = "";
document.getElementById('cantidad_personas').value = "";
document.getElementById('sucursal').value = "";
document.getElementById('restricciones').value = "";
});
})