<?php
// Execute the Python script and capture the output
exec('python news.py', $output);

// Since exec returns an array of lines, we implode it to a string
$json_output = implode("\n", $output);

// Decode the JSON output of the Python script
$scraped_data = json_decode($json_output, true);

// Set header for JSON response
header('Content-Type: application/json');

// Echo the data as JSON
echo json_encode($scraped_data);
?>
