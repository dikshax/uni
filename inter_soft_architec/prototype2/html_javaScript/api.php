<?php

// connecting to database/api
$mysqli = new mysqlu('localhost', '1916829', '19chiffchaff92', 'db1916829');

// checking for error
if ($mysqli -> connect_errno) {
    echo 'Failed to connect to MySQL: ' . $mysqli -> connect_errno;
    exit()
}

// Executing SQL query to get the data from the table
$sql = 'SELECT * FROM weather_info ORDER BY city DESC LIMIT 1';

$result = $mysqli -> query($sql);

// convert the data into json form and print
$row = $result -> fetch_assoc();
print(json_encode($row));

// Free result  set and close connection
$result -> free_result();
$mysqli -> close();

?>