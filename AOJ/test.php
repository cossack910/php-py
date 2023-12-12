<?php

function change($n) {
    $tmp = $n[0];
    $n[0] = $n[1];
    $n[1] = $tmp;
}

$N = [1, 2];
change($N);
print_r($N);