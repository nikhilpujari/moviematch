<?php
// fetch_movies.php
require 'vendor/autoload.php'; // Ensure you have the Google Cloud client library installed
ini_set('log_errors', 1);
ini_set('error_log', 'php-error.log');
use Google\Cloud\Storage\StorageClient;

function fetchMovies() {
    // Initialize the Google Cloud Storage client
    $storage = new StorageClient([
        'keyFilePath' => '../../../dbsmovie-0abde0e89895.json' // Replace with your key file path
    ]);

    // Replace these with your actual bucket and file details
    $bucketName = 'movie-datalake';
    $fileName = 'MovieGenre.csv';

    // Connect to the bucket
    $bucket = $storage->bucket($bucketName);

    // Download and read the content of the file
    $object = $bucket->object($fileName);
    $content = $object->downloadAsString();

    // Parse CSV content
    $lines = explode("\n", $content);
    $movies = [];
    foreach ($lines as $line) {
        $data = str_getcsv($line);
        if (count($data) > 1) { // Change this condition based on your CSV structure
            $movies[] = [
                'id' => iconv('ISO-8859-1', 'UTF-8//IGNORE', $data[0]),
                'name' => iconv('ISO-8859-1', 'UTF-8//IGNORE', $data[2]),
                'posterUrl' => iconv('ISO-8859-1', 'UTF-8//IGNORE', $data[5])
            ];
        }
    }

    //return $movies;
    $randomKeys = array_rand($movies, 6);
    $randomMovies = [];
    foreach ($randomKeys as $key) {
        $randomMovies[] = $movies[$key];
    }

    return $randomMovies;
}

header('Content-Type: application/json');
// Convert the movies array to JSON and output it
echo json_encode(fetchMovies());
?>