CREATE TABLE Users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE, 
    password TEXT,
    mod BOOLEAN
);
CREATE TABLE Restaurants (
    id SERIAL PRIMARY KEY, 
    restaurantname TEXT,
    info TEXT
);
CREATE TABLE Reviews (
    id SERIAL PRIMARY KEY,
    restaurant_id INTEGER REFERENCES Restaurants, 
    user_id INTEGER REFERENCES Users, 
    review TEXT, 
    stars INTEGER, 
    created_at TIMESTAMP
);
CREATE TABLE Followers (
    user_id INTEGER REFERENCES Users, 
    follow_id INTEGER REFERENCES Users
);
CREATE TABLE Suggestions (
    suggestion TEXT,
    info TEXT,
    user_id INTEGER REFERENCES Users
);
INSERT INTO Restaurants (restaurantname, info) VALUES ('oljenkorsi', 'tietoa paikasta');
INSERT INTO Restaurants (restaurantname, info) VALUES ('Unicafe chemicum', 'tietoa paikasta');
INSERT INTO Restaurants (restaurantname, info) VALUES ('Unicafe physicum', 'tietoa paikasta');
INSERT INTO Restaurants (restaurantname, info) VALUES ('Unicafe exactum', 'tietoa paikasta');