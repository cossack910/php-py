<?php
/**
 * 最大公約数
 *
 * 整数 x, y について、x ≥ y ならば x と y の最大公約数は y と x % y の最大公約数に等しい。ここで x % y は x を y で割った余りである。
 * 
 */
function divRemainder(int $x, int $y) {
    if ($x >= $y) {
        return [
            "remainder" => $x % $y, 
            "num" => $y
        ];
    } 
    return [
        "remainder" => $y % $x, 
        "num" => $x
    ];
}


[$x, $y] = array_map('intval', explode(' ', trim(fgets(STDIN))));

function calc(int $x, $y) {
    $arr = divRemainder($x, $y);
    if (0 === $arr["remainder"]) {
        return $arr["num"];
    } else {
        return calc($arr["remainder"], $arr["num"]);        
    }

}


print(calc($x, $y).PHP_EOL);