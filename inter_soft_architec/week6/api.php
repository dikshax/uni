<?php

// Connect to database
$mysqli = new mysqli("localhost","1916829","4al1l1","db1916829");
if ($mysqli -> connect_errno) {
  echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
  exit();
}

// Execute SQL query
$sql = "SELECT * FROM weather_info ORDER BY city DESC limit 1";

$result = $mysqli -> query($sql);

// Get data, convert to JSON and print
$row = $result -> fetch_assoc();
print json_encode($row);

// Free result set and close connection
$result -> free_result();
$mysqli -> close();

?>