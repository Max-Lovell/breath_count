<?php
if ( $_SERVER['REQUEST_METHOD']=='GET' && realpath(__FILE__) == realpath( $_SERVER['SCRIPT_FILENAME'] ) ) {
        header( 'HTTP/1.0 403 Forbidden', TRUE, 403 );
        die( header( 'location: /error.php' ) );
    }

if($_SERVER['HTTP_ORIGIN'] == 'https://[sso].eu.qualtrics.com') { 
    header('Access-Control-Allow-Origin: https://[sso].eu.qualtrics.com'); 
//header('Content-Type: application/json')

$blacklist = array(".php", ".phtml", ".php3", ".php4", ".js", ".shtml", ".pl" ,".py");
foreach ($blacklist as $file){
    if(preg_match("/$file\$/i", $_FILES['userfile']['name'])){ 
        exit;}
} //http://www.mysql-apache-php.com/fileupload-security.htm

if (isset($_POST['exp_data']) == true)
{
    //check uploads are json
    $test = json_decode(file_get_contents($_POST['exp_data']), true);
    if (JSON_ERROR_NONE !== json_last_error()){
    exit;} //https://stackoverflow.com/questions/48242848/how-to-parse-php-json-decode-data-to-jquery-ajax-request
    json_encode($test);

    $exp_data = $_POST['exp_data'];
    $exp_data = trim($exp_data, '"');
} else { exit; }

//sanitize data
$_POST = filter_input_array(INPUT_POST, FILTER_SANITIZE_STRING); //must come after exp_data - unsure how to sanitize this yet

if (isset($_POST['file_name']) == true)
{
    $file_name = $_POST['file_name'];
} else { exit; }

file_put_contents("[local_path]/$file_name.csv", $exp_data);
exit;

} else { exit; }

?>
