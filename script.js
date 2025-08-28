// Obtiene los elementos de la interfaz por su ID
const expressionInput = document.getElementById('expression-input');
const calculateButton = document.getElementById('calculate-button');
const resultDisplay = document.getElementById('result-display');

// Agrega un "escuchador de evento" al botón
calculateButton.addEventListener('click', async () => {
    // 1. Obtiene el texto de la caja de entrada
    const expression = expressionInput.value;

    // Si la caja de texto está vacía, no hace nada
    if (!expression) {
        resultDisplay.textContent = 'Por favor, ingresa una expresión.';
        return;
    }

    try {
        // 2. Realiza una solicitud al back-end de Django
        // El back-end está corriendo en localhost:8000
        const response = await fetch('http://127.0.0.1:8000/api/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ expression: expression }),
        });

        // 3. Revisa si la respuesta fue exitosa
        if (!response.ok) {
            throw new Error('Error en el servidor o expresión inválida.');
        }

        // 4. Parsea la respuesta JSON para obtener el resultado
        const data = await response.json();

        // 5. Muestra el resultado en la pantalla
        resultDisplay.textContent = data.result;

    } catch (error) {
        // Maneja cualquier error y lo muestra en la interfaz
        console.error('Hubo un error:', error);
        resultDisplay.textContent = 'Error: ' + error.message;
    }
});