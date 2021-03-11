<?php
// connecting to the database
$mysqli = new
mysqli('localhost', '1916829', '19chiffchaff92', 'db1916829');

if ($mysqli -> connect_errno) {
    echo 'Failed to connect to MySQL:' . $mysqli -> connect_error; 
    exit();
}

// Execute SQL query 
$sql = "SELECT * 
        FROM week7 
        WHERE city = '{$_GET['city']}' 
        AND weather_when >= DATE_SUB(NOW(), INTERVAL 10 SECOND) 
        ORDER BY weather_when 
        DESC LIMIT 1";

$result = $mysqli -> query($sql);

// get data, convert to JSON and print
$row = $result -> fetch_assoc();
print(json_encode($row));

// Free result set and close connection
$result -> free_result();
$mysqli -> close();
?>