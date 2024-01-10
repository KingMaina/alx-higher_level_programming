$(function () {
  const URL = 'https://hellosalut.stefanbohacek.dev/?lang=';

  function translate () {
    const languageCode = $('INPUT#language_code').val();
    $.ajax({
      type: 'POST',
      url: URL + languageCode,
      data: 'Hello',
      success: function (response) {
        $('DIV#hello').text(response.hello);
      },
      error: function (error) {
        console.error(error);
      }
    });
  }

  $('INPUT#btn_translate').on('click', translate);
  $('INPUT#language_code').on('keypress', function (event) {
    if (event.which === 13) {
      translate();
    }
  });
});
