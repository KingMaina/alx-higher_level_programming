$(function () {
  const URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  $.get(URL, function (data) {
    $('DIV#character').text(data.name);
  });
});
