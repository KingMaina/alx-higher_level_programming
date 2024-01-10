$(function () {
  const URL = 'https://hellosalut.stefanbohacek.dev/?lang=';

  $('INPUT#btn_translate').on('click', function () {
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
  });
});
