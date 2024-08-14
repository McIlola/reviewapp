CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE, 
    password TEXT
);
CREATE TABLE restaurant1 (
    id SERIAL PRIMARY KEY, 
    username TEXT, 
    review TEXT, 
    stars INTEGER, 
    created_at TIMESTAMP
);
CREATE TABLE restaurant2 (
    id SERIAL PRIMARY KEY, 
    username TEXT, 
    review TEXT, 
    stars INTEGER, 
    created_at TIMESTAMP
);
CREATE TABLE restaurant3 (
    id SERIAL PRIMARY KEY, 
    username TEXT, 
    review TEXT, 
    stars INTEGER, 
    created_at TIMESTAMP
);
CREATE TABLE restaurant4 (
    id SERIAL PRIMARY KEY, 
    username TEXT, 
    review TEXT, 
    stars INTEGER, 
    created_at TIMESTAMP
);