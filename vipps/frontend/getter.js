var api_base_url = 'http://127.0.0.1:8000/string_count_in_article'

function get_api_url(title, string) {
  return api_base_url + '/' + title + '/' + string
}

function show_count(count) {
  $('#count').html(count);
}

function show_error() {
  show_count('-');
}

$('#form').submit(function(e) {
  e.preventDefault();
  
  var string = $('#stringField').val();
  var title = $('#titleField').val();
  
  var url = get_api_url(title, string);
  
  $.ajax({
    url: url,
    type: 'GET',
    dataType: 'json',
    success: function(data) {
      show_count(data.count);
    },
    error: function() {
      show_error();
    }
  });
  
});