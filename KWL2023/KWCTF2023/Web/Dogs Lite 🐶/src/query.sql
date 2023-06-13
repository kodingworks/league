-- SQLite
CREATE TABLE IF NOT EXISTS `users` (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS `S3cR3tFl4g5` (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  value TEXT NOT NULL
);

INSERT INTO `users` (username, password) VALUES ('millo', 'hello'), ('Coco', '123654'), ('admin', 'qwerty'), ('rosie', 'abcd1234');

INSERT INTO `S3cR3tFl4g5` (value) VALUES ('K'), ('W'), ('C'), ('T'), ('F'), ('{'), ('d'), ('0'), ('g'), ('s'), ('Q'), ('l'), ('1'), ('t'), ('3'), ('_'), ('B'), ('1'), ('i'), ('n'), ('D'), ('_'), ('1'), ('n'),('7'), ('3'), ('c'), ('7'), ('i'), ('O'), ('n'), ('}');

SELECT name FROM sqlite_master WHERE type='table';