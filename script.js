```javascript
// Replace with your actual API key
var mapApiKey = 'YOUR_API_KEY';

// Initialize Google Map
function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 2,
        center: {lat: 0, lng: 0}
    });
}

// Fetch real-time disaster data from the server
function fetchDisasterData() {
    fetch('/disaster-data')
        .then(response => response.json())
        .then(data => {
            var dataTable = document.getElementById('data-table');
            dataTable.innerHTML = '';
            data.forEach(row => {
                var tr = document.createElement('tr');
                row.forEach(cell => {
                    var td = document.createElement('td');
                    td.textContent = cell;
                    tr.appendChild(td);
                });
                dataTable.appendChild(tr);
            });
        });
}

// Fetch recommended resource allocation from the server
function fetchResourceAllocation() {
    fetch('/resource-allocation')
        .then(response => response.json())
        .then(data => {
            var resourceTable = document.getElementById('resource-table');
            resourceTable.innerHTML = '';
            data.forEach(row => {
                var tr = document.createElement('tr');
                row.forEach(cell => {
                    var td = document.createElement('td');
                    td.textContent = cell;
                    tr.appendChild(td);
                });
                resourceTable.appendChild(tr);
            });
        });
}

// Update the disaster map with new data
function updateDisasterMap(data) {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 2,
        center: {lat: 0, lng: 0}
    });
    data.forEach(location => {
        var marker = new google.maps.Marker({
            position: {lat: location.lat, lng: location.lng},
            map: map
        });
    });
}

// Fetch new data every 5 seconds
setInterval(fetchDisasterData, 5000);
setInterval(fetchResourceAllocation, 5000);

// Initialize the map when the page loads
window.onload = initMap;
```
