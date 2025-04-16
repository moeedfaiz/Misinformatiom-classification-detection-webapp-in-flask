function checkNews() {
    const newsText = document.getElementById('newsInput').value;
    fetch('/detect', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: newsText })
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = 'Result: ' + data.result;
        resultDiv.className = 'result ' + (data.result === 'True' ? 'true' : 'false');

        if (data.result === "True" && data.links && data.links.length > 0) {
            const linksHTML = data.links.map(link => `<a href="${link}" target="_blank">${link}</a>`).join('<br>');
            resultDiv.innerHTML += '<br>Relevant articles:<br>' + linksHTML;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = 'Error processing the request';
        resultDiv.className = 'result false';
    });
}

function uploadImage() {
    const fileInput = document.getElementById('imageUpload');
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select an image first!");
        return;
    }

    const formData = new FormData();
    formData.append('image', file);

    fetch('/extract_text', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.text) {
            document.getElementById('newsInput').value = data.text;
        } else {
            alert("No text detected in the image.");
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert("Error extracting text from the image.");
    });
}
