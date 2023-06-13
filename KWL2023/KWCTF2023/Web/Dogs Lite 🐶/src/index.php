<?php

session_start();

if(!isset($_SESSION['login'])){
  header("Location: login.php");
  exit;
}

$login = $_SESSION['login'];

if ($login != true) {
  header("Location: login.php");
  exit;
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Welcome 👋</title>
  <link rel="stylesheet" href="./assets/style.css">
</head>

<body>
  <div class="container">
    <img src="./assets/dog.gif" alt="dog">
    <h1>Welcome 🐶</h1>
    <p>Nice to meet you again bro, what do you want in here?</p>
    <form action="./logout.php">
      <button>Logout</button>
    </form>
  </div>
</body>

</html>
