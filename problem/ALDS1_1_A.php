<?php

function insertionSort(array $A,int $N){
    print(implode(' ', $A).PHP_EOL);

    if (true === sortJudge($A, $N)) {
        return;
    }

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
    return $A;
}

function sortJudge(array $A, int $N) {
    foreach($A as $key => $val){
        if ($key + 1 === $N) {
            break;
        }

        if ($val > $A[$key + 1]) {
            return false;
        }
    }
    return true;
}

$N = (int) trim(fgets(STDIN));
$A = array_map('intval', explode(' ', trim(fgets(STDIN))));

insertionSort($A, $N);