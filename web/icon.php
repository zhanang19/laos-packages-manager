<?php
header('Content-Type: application/json');
require "dom.php";
$app = $_GET['app'];

$link = 'https://raw.githubusercontent.com/PapirusDevelopmentTeam/papirus-icon-theme/master/Papirus/64x64/apps/' . $app . '.svg';
// $link = 'http://localhost/lpm/papirus-icon-theme-master/Papirus/64x64/apps/' . $app . '.svg';
$data = str_get_html(file_get_contents($link));

if ($data === FALSE) {
    // Atur default link disini
    $jadi['link'] = 'https://via.placeholder.com/64.svg';
} else {

    $jadi['link'] = $link;
}

echo json_encode($jadi, JSON_PRETTY_PRINT);
