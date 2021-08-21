.read lab13.sql

CREATE TABLE su19favpets AS
  SELECT pet, count(pet) FROM students GROUP BY pet ORDER BY count(pet) DESC LIMIT 10;


CREATE TABLE su19dog AS
  SELECT pet, count(pet) FROM students GROUP BY pet ORDER BY count(pet) DESC LIMIT 1;


CREATE TABLE obedienceimages AS
  SELECT seven, instructor, count(instructor) FROM students WHERE seven = "7" GROUP BY instructor;
