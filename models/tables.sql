CREATE TABLE users(
  id INTEGER PRIMARY KEY ASC    NOT NULL,
  email           TEXT    NOT NULL
);

CREATE TABLE business(
  id INTEGER PRIMARY KEY ASC    NOT NULL,
  name           TEXT    NOT NULL,
  points_to_offer           INTEGER    NOT NULL DEFAULT 0
);

CREATE TABLE points(
  id INTEGER PRIMARY KEY ASC    NOT NULL,
  user_id INTEGER,
  business_id INTEGER,
  active_round BOOLEAN,
  FOREIGN KEY(user_id) REFERENCES users(id),
  FOREIGN KEY(business_id) REFERENCES business(id)
);