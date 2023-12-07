const URL = "https://tpcodoacodo.pythonanywhere.com/";

document.getElementById('formAgregarPlato').addEventListener('submit', function(event) {
    event.preventDefault();

    var formData = new FormData();
    formData.append('nombre', document.getElementById('nombre').value);
    formData.append('descripcion', document.getElementById('descripcion').value);
    formData.append('precio', document.getElementById('precio').value);


    fetch(URL + 'platos/agregar', {
        method: 'POST',
        body: formData 
    })
    .then(function(response) {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error al agregar el plato.');
        }
    })
    .then(function() {
        alert('Plato agregado correctamente.');
        // Limpiar el formulario después de agregar
        document.getElementById('nombre').value = "";
        document.getElementById('descripcion').value = "";
        document.getElementById('precio').value = "";
    })
    .catch(function(error) {
        alert('Error al agregar el plato.');
        console.error('Error:', error);
    });
});
