document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('predictionForm');
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission
        
        // Get the form data
        const formData = new FormData(form);
        
        // Convert form data to JSON
        const jsonData = {};
        for (const [key, value] of formData.entries()) {
            jsonData[key] = parseFloat(value);
        }
        
        // Make a POST request to the server with the form data
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsonData)
        })
        .then(response => response.json())
        .then(data => {
            // Display the prediction result
            alert(`Predicted price category: ${data.prediction}`);
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again later.');
        });
    });
});
