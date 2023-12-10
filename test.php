<?php
// [$x, $y] = explode(' ', trim(fgets(STDIN)));
// $menseki = (string) $x * $y;
// $syuhen = (string) ($x + $y) * 2;
// print($menseki . ' ' . $syuhen . PHP_EOL);

$n = (int) trim(fgets(STDIN));
$hh = (string) floor($n / 3600);
$n = $n % 3600;
$mm = (string) floor($n / 60);
$n = (string) $n % 60;
print($hh . ':' . $mm . ':' . $n .PHP_EOL);