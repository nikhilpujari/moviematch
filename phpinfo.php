<?php
require 'vendor/autoload.php'; // Adjust the path if necessary

use Google\Cloud\Storage\StorageClient;

try {
    // Attempt to initialize the Google Cloud Storage client
    $storage = new StorageClient([
        'keyFilePath' => '../../../dbsmovie-0abde0e89896.json' // Replace with your actual path
    ]);

    echo "Google Cloud Storage client initialized successfully.";
} catch (Exception $e) {
    echo "Error initializing Google Cloud Storage client: " . $e->getMessage();
}
