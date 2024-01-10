$(function () {
  const URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.get(URL, function (data) {
    const movies = data.results || [];

    try {
      if (movies.length > 0) {
        for (let index = 0; index < movies.length; index++) {
          $('UL#list_movies').append(`<li>${movies[index].title}</li>`);
        }
      }
    } catch (error) {
      console.error(error);
    }
  });
});
