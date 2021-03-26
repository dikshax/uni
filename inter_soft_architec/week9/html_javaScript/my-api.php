<?php
// connecting to the database
$mysqli = new
mysqli('localhost', '1916829', '19chiffchaff92', 'db1916829');

if ($mysqli -> connect_error) {
    echo 'Failed to connect to MySQL:' . $mysqli -> connect_error; 
    exit();
}

// first check requested daata is present and fresh
include('fresh_data.php');

// Execute SQL query 
$sql = "SELECT * 
        FROM week_7 
        WHERE city = '{$_GET['city']}' 
        AND time >= DATE_SUB(NOW(), INTERVAL 10 SECOND) 
        ORDER BY time 
        DESC LIMIT 1";

$result = $mysqli -> query($sql);

// get data, convert to JSON and print
$row = $result -> fetch_assoc();
print(json_encode($row));

// Free result set and close connection
$result -> free_result();
$mysqli -> close();
?>
