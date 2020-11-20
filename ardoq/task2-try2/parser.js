parser = new Object();

parser.get_all_stations = function (callback) {
  fetch('https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json')
  .then(response => response.json())
  .then(data => callback(data.data.stations));
}

parser.get_all_station_statuses = function (callback) {
  fetch('https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json')
  .then(response => response.json())
  .then(data => callback(data.data.stations));
}

parser.get_station_status = function (station_id, callback) {
  parser.get_all_station_statuses(function(data) {
    callback(data.filter(station => { return station.station_id == station_id })[0])
  });
}