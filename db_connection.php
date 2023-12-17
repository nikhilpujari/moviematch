<?php
// Replace these variables with your actual database credentials
$dbHost = '35.185.85.110';
$dbUser = 'root'; // Database username
$dbPass = 'password'; // Database password
$dbName = 'Movies'; // Database name

// Creating a connection using PDO
try {
    $dsn = "mysql:host=$dbHost;dbname=$dbName";
    $pdo = new PDO($dsn, $dbUser, $dbPass);
    // Set PDO to throw exceptions on error
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
   // echo "Connected successfully";
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}
?>
