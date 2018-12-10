<?php
    $data=$_POST['imageBase64'];
    if (preg_match('/^data:image\/(\w+);base64,/', $data, $type)) {
    $data = substr($data, strpos($data, ',') + 1);
    $type = strtolower($type[1]); // jpg, png, gif

    if (!in_array($type, [ 'jpg', 'jpeg', 'gif', 'png' ])) {
        throw new \Exception('invalid image type');
    }

    $data = base64_decode($data);

    if ($data === false) {
        throw new \Exception('base64_decode failed');
    }
    } else {
    throw new \Exception('did not match data URI with image data');
    }
    file_put_contents(dirname(__FILE__)."\\tmp\\img.{$type}", $data);
?>