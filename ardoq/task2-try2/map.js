// Create a Leaflet map centered in Oslo
var map = new Object();
map.map = L.map('map').setView([59.915279, 10.748559], 13);
map.create_map = function () {
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: 'Openstreetmap',
      maxZoom: 18,
      id: 'mapbox/streets-v11',
      tileSize: 512,
      zoomOffset: -1
  }).addTo(map.map);
}

map.add_stations = function (stations) {
  // Add a marker for each station
  var markers = [];
  for (var i = 0; i < stations.length; i++) {
    var marker = L.marker([stations[i].lat, stations[i].lon]).addTo(map.map);
    marker.bindPopup();
    marker.station = stations[i]
    marker.on('popupopen', function() {
      set_popup_contents(this);
    });
    markers.push(marker);
  }
  
  // Change the color of the marker according to the availability of bikes
  parser.get_all_station_statuses(function (station_statuses) {
    for (var i = 0; i < station_statuses.length; i++) {
      var marker = markers.filter(marker => { return marker.station.station_id == station_statuses[i].station_id })[0];
      if (station_statuses[i].num_bikes_available == 0) {
        marker.setIcon(redIcon);
      } else {
        marker.setIcon(greenIcon);
      }
    }
  });
}

// Internals
function set_popup_contents(marker) {
  parser.get_station_status(marker.station.station_id, function (station_status) {
    console.log(station_status);
    marker.setPopupContent(
      marker.station.name
      + "<br>Ledige sykler: " + station_status.num_bikes_available
      + "<br>Ledige stativer: " + station_status.num_docks_available
    );
  });
}