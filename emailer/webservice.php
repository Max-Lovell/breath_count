<?php

if(isset($_GET["condition"])){ //null !== htmlspecialchars($_GET["condition"])
    $p_data = array(
        "email" => htmlspecialchars($_GET["email"]),
        "survey" => htmlspecialchars($_GET["survey"]),
        "date" => htmlspecialchars($_GET["date"]),
        "condition" => htmlspecialchars($_GET["condition"]),
    );
} else {
    $p_data = array(
        "email" => htmlspecialchars($_GET["email"]),
        "survey" => htmlspecialchars($_GET["survey"]),
        "date" => htmlspecialchars($_GET["date"])
    );
};

file_put_contents("[local_path]/".$p_data['email'].$p_data['survey'].".json", json_encode($p_data));
?>
