"""
Below are the commands that are being used to create a table and handle the table in different ways

#CREATE A TABLE 
CREATE TABLE flights (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 origin TEXT NOT NULL,
 destination TEXT NOT NULL,
 duration INTEGER NOT NULL
);

# Adding the values to the table 
INSERT INTO flights
 (origin, destination, duration)
 VALUES ("New York", "London", 415);

# Returns all the data from the table 
SELECT * FROM flights;

# Selects and returns specific from the table 
SELECT origin, destination FROM flights;


# Custemization FOR SEARCH
SELECT * FROM flights WHERE id = 3;
SELECT * FROM flights WHERE origin = "New York";
SELECT * FROM flights WHERE duration > 500;
SELECT * FROM flights WHERE duration > 500 AND destination = "Paris";
SELECT * FROM flights WHERE origin IN ("New York", "Lima");  # returns all the details of flights where the origin is newyork or lima
SELECT * FROM flights WHERE origin LIKE "%a%"; # return if the origin contains char "a"

# UPDATE THE TABLE 
UPDATE flights SET duration = 430 WHERE origin = "New York" AND destination = "London";

# DELETE THE TABLE 
DELETE FROM flights WHERE destination = "Tokyo";
"""
