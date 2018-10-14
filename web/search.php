<?php
header('Content-Type: application/json');
require "dom.php";
$app = $_GET['app'];

$data = str_get_html(file_get_contents('https://packages.ubuntu.com/search?suite=bionic&section=all&arch=any&keywords='.$app.'&searchon=names'));

function lihat_deskripsi($app) {
    $data = str_get_html(file_get_contents('https://packages.ubuntu.com/search?suite=bionic&section=all&arch=any&keywords='.$app.'&searchon=names'));
    $deskripsi = explode('[', explode(': 	', strip_tags($data->find('li')[0]))[1])[0];
    return $deskripsi;
}

if (strlen($app) > 1) {
    if(! strpos($data->plaintext, 'Sorry, your')){
        $jadi['status'] = true;
        $jadi['cari'] = $app;
    
        $i = 0;
        foreach ($data->find('a[class=resultlink]') as $e) {
            $tmp = explode('/bionic/', $e->href)[1];
            if ($i === 0) {
                $jadi['nama_paket'] = $tmp;
                $jadi['deskripsi_paket'] = explode('[', explode(': 	', strip_tags($data->find('li')[0]))[1])[0];;
            } else {
                $jadi['pilihan_paket'][$i] = $tmp;
            }
            $i++;
        }
    }else{
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