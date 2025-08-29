// Obtiene los elementos de la interfaz por su ID.
// Los IDs ahora coinciden con tu HTML.
const expressionInput = document.getElementById('expression-input');
const calculateButton = document.getElementById('calculate-button');
const resultDisplay = document.getElementById('result-display');

calculateButton.addEventListener('click', async () => {
    // Obtiene el texto de la caja de entrada
    const expression = expressionInput.value;

    if (!expression) {
        resultDisplay.textContent = 'Por favor, ingresa una expresión.';
        return;
    }

    try {
        // Realiza una solicitud al back-end de Django
        // La URL ha sido corregida
        const response = await fetch('http://127.0.0.1:8000/api/calcular/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            // El nombre de la clave es 'expresion' para coincidir con tu backend
            body: JSON.stringify({ expresion: expression }),
        });

        const data = await response.json();

        if (response.ok) {
            // Muestra el resultado de la API. La clave es 'resultado'
            resultDisplay.textContent = data.resultado;
        } else {
            // Si el servidor envía un error, lo muestra
            resultDisplay.textContent = 'Error: ' + data.error;
        }

    } catch (error) {
        // Maneja errores de red
        console.error('Hubo un error:', error);
        resultDisplay.textContent = 'Error de conexión. Asegúrate de que el servidor de Django esté corriendo.';
    }
    
});

const clearButton = document.getElementById('clear-button');

if (clearButton) {
    clearButton.addEventListener('click', () => {
        expressionInput.value = '';
        resultDisplay.textContent = '';
    });
}