<?php
// Run the Python script and echo the result
$output = shell_exec('python movie-suggestions.py');
echo $output;
?>
