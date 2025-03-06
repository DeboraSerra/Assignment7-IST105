<?php

  $list = $_GET('numbers');
  $threshold = $_GET('threshold');

  $command = escapeshellcmd("python3 bitwise_operations.py $list $threshold");
  $output = shell_exec($command);
  $host = $_SERVER['HTTP_HOST'];
  echo $host;
  echo $output;
?>