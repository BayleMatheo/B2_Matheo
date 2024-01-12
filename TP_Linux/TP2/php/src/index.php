<?php
$host = 'mysql';
$user = 'root';
$password = 'passwd';
$db = 'db_docker';

$conn = new mysqli($host, $user, $password, $db);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$message = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];

    $sql = "INSERT INTO users (username) VALUES ('$username')";
    if ($conn->query($sql) === TRUE) {
        $message = "Username added successfully!";
        echo '<script>alert("' . $message . '");</script>';
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

$sql = "SELECT username FROM users";
$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TP2 Linux : Docker PHP</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        body {
            background-color: #3498db;
        }
    </style>
</head>
<body>

    <h2>ADD</h2>
    <form method="post">
        <label for="username">Username:</label>
        <input type="text" name="username" required>
        <button type="submit">+</button>
    </form>

    <h2>DB Users</h2>
    <?php
    if ($result->num_rows > 0) {
        echo "<ul>";
        while ($row = $result->fetch_assoc()) {
            echo "<li>" . htmlspecialchars($row["username"]) . "</li>";
        }
        echo "</ul>";
    } else {
        echo "<p class='no-users'>No users in the database.</p>";
    }

    $conn->close();
    ?>

</body>
</html>
