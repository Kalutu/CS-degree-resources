<?php
$servername = "localhost";
$username = "root";
$password = "danvic";
$dbname = "bsit2019_db";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO students (name, gender,date_of_birth)
VALUES ('Anne Moraa','female', '2000-07-07')";

if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>