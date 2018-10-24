<?php
header('Content-Type: application/json');
require "dom.php";
$app = $_GET['app'];

$data = str_get_html(file_get_contents('https://www.alldeb.net/webmaker/bionic?varian=ubuntu&arsitektur=amd64&aplikasi='.$app));

if(strpos($data->plaintext, 'Maaf') == false){
    $body = $data->find('a');
    $jadi['status'] = true;
    $jadi['nama_paket'] = $app;

    for($a = 1; $a < 5; $a++){
        $tmp = explode(' : ',$data->find('div')[0]->find('div')[6]->find('div')[0]->find('div')[2]->find('div')[0]->find('p')[$a]->plaintext);
        $jadi['deskripsi_paket'][strtolower(str_replace(' ', '_', $tmp[0]))] = $tmp[1];
    }

    $jadi['tautan'] = 'https://www.alldeb.net'.$body[3]->href;
} else {
    $jadi['status'] = false;
    $jadi['nama_paket'] = $app;	
    $jadi['pesan'] = 'Paket tidak ditemukan';
}
echo json_encode($jadi,JSON_PRETTY_PRINT);
?>