<?php

  $list = $_GET['numbers'];
  $threshold = $_GET['threshold'];

  $command = escapeshellcmd("python3 bitwise_operations.py $list $threshold");
  $output = shell_exec($command);
  $host = $_SERVER['HTTP_HOST'];
  echo "<div style='text-align: center; border: 1px solid #999; border-radius: 4px; padding: 12px 8px; max-width: 500px; margin: 128px auto 0;'>";
  echo "<h1>$host</h1>";
  echo "<br>";
  echo $output;
  echo "</div>";
?>