<?php

function insertionSort(array $A,int $N){
    print(implode(' ', $A).PHP_EOL);

    if (true === sortJudge($A)) {
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

function sortJudge(array $A) {
    foreach($A as $key => $val){
        if ($key + 1 === count($A) - 1) {
            break;
        }

        if ($val > $A[$key + 1]) {
            return false;
        }
    }
    return true;
}

$test_arr = [5, 2, 4, 6, 1, 3];
$ans = insertionSort($test_arr, count($test_arr));
print("\n");

$test_arr = [1, 2, 3];
$ans = insertionSort($test_arr, count($test_arr));
print("\n");

$test_arr = [1001,2,300, 54, 9000, 6, 5, 400000];
$ans = insertionSort($test_arr, count($test_arr));

# docker exec php8.1 php /var/www/php-py/problem/ALDS1_1_A.php 