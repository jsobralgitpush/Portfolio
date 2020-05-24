SELECT DISTINCT people.name FROM ratings JOIN directors ON ratings.movie_id = directors.movie_id JOIN people ON people.id = directors.person_id WHERE ratings.rating >=9.0;
