<?php
echo 'hai';
die();
$icon = $_GET['icon'];
header('Content-Type: image/png');

echo imagepng(imagecreatefromstring(file_get_contents($icon))); 
