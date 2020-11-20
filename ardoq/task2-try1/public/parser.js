import "/axios"
export function get_all_stations(callback) {
  axios({
    method: 'get',
    url: 'https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json',
    responseType: 'stream'
  })
  .then(function (response) {
    console.log(response)
  });
}