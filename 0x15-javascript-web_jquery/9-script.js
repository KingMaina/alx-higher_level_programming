$(function () {
  const URL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  $.get(URL, function (data) {
    $('DIV#hello').text(data.hello);
  });
});
