<?php
session_start();
header('Content-Type: application/json');
ini_set('log_errors', 1);
ini_set('error_log', 'php-error.log');

include 'db_connection.php'; // Database connection

$input = json_decode(file_get_contents('php://input'), true);

$userId = uniqid();

if ($input) {
foreach ($input as $vote) {
    $movieId = $vote['movieId'];
    // Convert vote to integer
    switch ($vote['vote']) {
        case 'like':
            $rating = 1;
            break;
        case 'dislike':
            $rating = -1;
            break;
        case 'none':
        default:
            $rating = 0;
            break;
        }

    $stmt = $pdo->prepare("INSERT INTO Userpreference (UserID, MovieID, Rating) VALUES (?, ?, ?)
    ON DUPLICATE KEY UPDATE Rating = ?");
    $stmt->execute([$userId, $movieId, $rating, $rating]);
}
    echo json_encode(['status' => 'success']);
} else {
    echo json_encode(['status' => 'error', 'message' => 'No data received']);
}

