<?php
header('Content-Type: application/json');
require "dom.php";
$app = $_GET['app'];

$base_link = 'https://raw.githubusercontent.com/PapirusDevelopmentTeam/papirus-icon-theme/master/Papirus/64x64/apps/';
$link = $base_link . $app . '.svg';
// $link = 'http://localhost/lpm/papirus-icon-theme-master/Papirus/64x64/apps/' . $app . '.svg';
$data = str_get_html(file_get_contents($link));

if ($data === FALSE) {
    $jadi['link'] = 'http://artemtech.me/api/lpm/kemangi.svg';
} else {
    if ($data->find('svg')[0]) {
        $jadi['link'] = $link;
    } else {
        $tmp = str_replace('.svg', '', $data);
        $jadi['link'] = $base_link . $tmp . '.svg';
    }
}

echo json_encode($jadi, JSON_PRETTY_PRINT);
