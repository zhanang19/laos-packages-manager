<?php
$icon = $_GET['icon'];
header('Content-Type: image/png');

echo file_get_contents(base64_decode($icon));