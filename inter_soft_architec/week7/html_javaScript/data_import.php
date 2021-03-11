<?php

// Select weather data for given parameters
$sql = "SELECT * 
        FROM week7 
        WHERE city = '{$_GET['city']}' 
        AND weather_when >= DATE_SUB(NOW(), INTERVAL 10 SECOND) 
        ORDER BY weather_when 
        DESC LIMIT 1";

$result = $mysqli -> query($sql);

// if 0 record found
if ($result -> num_rows == 0) {
    $url = 'https://api.openweathermap.org/data/2.5/weather?q='.$_GET['city'].'&appid=a9674e7298c06e2d719d1133e6178cba&units=metric';

    // get data from openweathermap and store in JSON object
    $data = file_get_contents($url);
    $json = json_decode($data, true);

    // Fetch the required fields
    $city = $json['main'][1];
    $country = $json['sys'][0]['country'];
    $pic =  $json['weather'][0]['icon'];
    $temperature = $json['main']['temp'];
    $tem_max = $json['main']['temp_max'];
    $tem_min = $json['main']['temp_min'];
    $weather_when = date("Y-m-d H:i:a");


    // build INSERT sql statement
    $sql = "INSERT INTO week7 (city, country, pic, temperature, tem_max, tem_min, weather_when) VALUES ('{$city}', '{$country}', '{$pic}', '{$temperature}', '{$tem_max}', '{$tem_min}, '{$weather_when}'";
    
    // run SQL statement
    $mysqli -> query($sql);
}
?>