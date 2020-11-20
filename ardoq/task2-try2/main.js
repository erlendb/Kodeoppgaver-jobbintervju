map.create_map();

parser.get_all_stations(function(stations) {
  map.add_stations(stations)
});