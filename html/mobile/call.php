<?php
$postdata = http_build_query(
    array(
        'ST0q' => $_POST['ST0q']
    )
);

$opts = array('http' =>
    array(
        'method'  => 'POST',
        'header'  => 'Content-Type: application/x-www-form-urlencoded',
        'content' => $postdata
    )
);

$context  = stream_context_create($opts);

$result = file_get_contents('http://localhost:481/call/', false, $context);

echo($result);
?>
