fetch('http://localhost:5000/')
    .then(response => response.text())
    .then(data => console.log(data));
