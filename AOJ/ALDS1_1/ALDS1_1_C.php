<?php
$n = (int) trim(fgets(STDIN));

function primeNumJudge(int $num) {
    $i = 2;
    while($i * $i <= $num) {
        if (0 === $num % $i) {
            return false;
        }
        $i++;
    }
    return true;
}

$ans = 0;
for ($i =0 ; $i < $n; $i++) {
    $num = (int) trim(fgets(STDIN));
    if (true === primeNumJudge($num)) {
        $ans++;
    }
}
print($ans.PHP_EOL);