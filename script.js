document.getElementById('rotatingObject').addEventListener('click', function() {
    fetch('http://127.0.0.1:5000/generate-idea')
        .then(response => response.json())
        .then(data => {
            // Display the generated idea in a user-friendly way
            document.getElementById('idea-container').innerText = data.idea;
        })
        .catch(error => console.error('Error:', error));
});
