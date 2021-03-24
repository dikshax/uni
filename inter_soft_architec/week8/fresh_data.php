<?php
// selecting weather data for given parameters
$sql = "SELECT * 
        FROM week_7 
        WHERE city = '{$_GET['city']}' 
        AND time >= DATE_SUB(NOW(), INTERVAL 10 SECOND) 
        ORDER BY time 
        DESC LIMIT 1";

$result = $mysqli -> query($sql);

// if there is no record found in the table
if ($result -> num_rows == 0) {
    $url = "https://api.openweathermap.org/data/2.5/weather?q=".$_GET['city']."&appid=a9674e7298c06e2d719d1133e6178cba&units=metric";

    //get the data from the openweathermap and store it in jsonn object form
    $data = file_get_contents($url);
    $json = json_decode($data, true);


    // fetch required fields
    $city = $json['name'];
    $country = $json['sys']['country'];
    $description = $json['weather'][0]['description'];
    $temperature = $json['main']['temp'];
    $tem_max = $json['main']['temp_max'];
    $tem_min = $json['main']['temp_min'];
    $time = date("Y-m-d H:i:s");

    // sql statement to ensert the data into the table (week_7)
    $sql = "INSERT INTO week_7 (city, country, description, temperature, tem_max, tem_min, time) VALUES ('{$city}', '{$country}', '{$description}', '{$temperature}', '{$tem_max}', '{$tem_min}', '{$time}')";

    // run sql statement and report errors
    if(!$mysqli -> query($sql)) {
        echo("<h5> SQL error description: ".$mysqli -> error."</h5>");
    }
}
?>
