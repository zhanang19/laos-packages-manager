<?php
header('Content-Type: application/json');
require "dom.php";
$app = $_GET['app'];

$data = str_get_html(file_get_contents('https://packages.ubuntu.com/search?suite=bionic&section=all&arch=any&keywords='.$app.'&searchon=names'));
$data2 = str_get_html(file_get_contents('https://www.alldeb.net/webmaker/cari-bionic?aplikasi='.$app));

if (strlen($app) > 1) {
    if (! strpos($data->plaintext, 'Sorry, your')) {
        $jadi['status'] = true;
        $jadi['nama_paket'] = $app;

        $tmp = strip_tags($data->find('li')[0]);
        $tmp = explode(': 	', $tmp)[1];
        $tmp = explode(' [', $tmp)[0];
        $tmp = explode('  ', $tmp)[0];
        $tmp = explode(' (', $tmp)[0];
        
        $jadi['deskripsi_paket'][] = $tmp;

        $tmp = $data2->find('em')[0]->plaintext;
        $tmp = explode('"  ', $tmp)[1];
        $tmp = explode(' "', $tmp)[0];
        $jadi['deskripsi_paket'][] = $tmp;
    } else {
        $jadi['status'] = false;
        $jadi['cari'] = $app;	
        $jadi['pesan'] = 'Paket tidak ditemukan, silahkan periksa kembali kata kunci pencarian';
    }
        
} else {
    $jadi['status'] = false;
    $jadi['cari'] = $app;	
    $jadi['pesan'] = 'Masukkan kata kunci minimal 2 karakter';
}


echo json_encode($jadi,JSON_PRETTY_PRINT);