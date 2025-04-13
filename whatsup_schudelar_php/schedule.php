<?php
header('Content-Type: application/json');

$phone = $_POST['phone'];
$message = $_POST['message'];
$dateTime = $_POST['dateTime'];

// Sanitize the inputs to prevent command injection
$phone = escapeshellarg($phone);
$message = escapeshellarg($message);
$dateTime = escapeshellarg($dateTime);

// Call the Python script to schedule the message
$command = "python app.py $phone $message $dateTime 2>&1";
exec($command, $output, $return_var);

// Log the output of the Python script
$logMessage = "Phone: " . $phone . ", Message: " . $message . ", DateTime: " . $dateTime . ", Python Output: " . implode("\n", $output) . "\n";
file_put_contents('log.txt', $logMessage, FILE_APPEND);

if ($return_var === 0) {
    $response = array('message' => 'Message scheduled successfully!');
} else {
    $response = array('message' => 'Message scheduling failed. Check log.txt for details. Return code: ' . $return_var);
}
echo json_encode($response);
?>
