<?php

function insertionSort(array $A,int $N) {
    print(implode(' ', $A).PHP_EOL);

    for ($i = 1; $i < $N; $i++) {
        $v = $A[$i];
        $j = $i - 1;
        while ($j >= 0 && $A[$j] > $v) {
            $A[$j+1] = $A[$j];
            $j--;
        }
        $A[$j+1] = $v;
        print(implode(' ', $A).PHP_EOL);
    }
}

$N = (int) trim(fgets(STDIN));
$A = array_map('intval', explode(' ', trim(fgets(STDIN))));

insertionSort($A, $N);