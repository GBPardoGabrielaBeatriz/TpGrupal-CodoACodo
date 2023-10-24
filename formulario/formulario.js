document.getElementById('reservationForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const fullName = document.getElementById('fullName').value.trim();
    const email = document.getElementById('email').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const date = document.getElementById('date').value;
    const people = document.getElementById('people').value;
    const message = document.getElementById('message').value.trim();

    if (validateForm(fullName, email, phone, date, people, message)) {
        const formData = new FormData(event.target);
        const response = await fetch(event.target.action, {
            method: 'POST',
            body: formData,
            headers: {
                'Accept': 'application/json'
            }
        });

        if (response.ok) {
            alert('Reserva realizada con éxito');
            event.target.reset();  
        } else {
            alert('Hubo un error al enviar el formulario.');
        }
    } else {
        alert('Por favor, completa todos los campos correctamente.');
    }
    // Imprimir los valores en consola
    console.log("Nombre y Apellido:", fullName);
    console.log("Correo Electrónico:", email);
    console.log("Número de Teléfono:", phone);
    console.log("Fecha de Reserva:", date);
    console.log("Cantidad de Comensales:", people);
    console.log("Restricciones alimenticias:", message);
});

function validateForm(fullName, email, phone, date, people, message) {
    if (!fullName || !email || !phone || !date || !people) {
        return false;
    }

    let emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!email.match(emailPattern)) {
        alert('Formato de correo electrónico no válido.');
        return false;
    }

    let phonePattern = /^[0-9]{10}$/;
    if (!phone.match(phonePattern)) {
        alert('Formato de número de teléfono no válido. Debe contener exactamente 10 dígitos.');
        return false;
    }

    return true;
}