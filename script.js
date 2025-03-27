let map = L.map('map').setView([20.5937, 78.9629], 5); 
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

let cities = {
    "Mumbai": [19.076, 72.8777],
    "Delhi": [28.7041, 77.1025],
    "Bangalore": [12.9716, 77.5946],
    "Hyderabad": [17.3850, 78.4867],
    "Chennai": [13.0827, 80.2707],
    "Kolkata": [22.5726, 88.3639],
    "Pune": [18.5204, 73.8567],
    "Jaipur": [26.9124, 75.7873],
    "Ahmedabad": [23.0225, 72.5714],
    "Lucknow": [26.8467, 80.9462],
    "Surat": [21.1702, 72.8311],
    "Nagpur": [21.1458, 79.0882],
    "Bhopal": [23.2599, 77.4126],
    "Indore": [22.7196, 75.8577],
    "Patna": [25.5941, 85.1376],
    
};

function findPath() {
    let startCity = document.getElementById("start").value;
    let endCity = document.getElementById("end").value;

    fetch(`/shortest-path?start=${startCity}&end=${endCity}`)
    .then(response => response.json())
    .then(data => {
        if (data.path) {
            // Clear existing layers (markers and polylines)
            map.eachLayer(layer => {
                if (!!layer.toGeoJSON) map.removeLayer(layer);
            });

            // Get the route coordinates
            let route = data.path.map(city => cities[city]);

            // Add markers for start and end cities
            L.marker(route[0]).addTo(map).bindPopup(`Start: ${startCity}`).openPopup();
            L.marker(route[route.length - 1]).addTo(map).bindPopup(`End: ${endCity}`).openPopup();

            // Draw the route on the map
            L.polyline(route, {color: 'red'}).addTo(map);

            // Fit the map to the route
            map.fitBounds(route);
        } else {
            alert("No path found!");
        }
    })
    .catch(error => console.error('Error:', error));
}