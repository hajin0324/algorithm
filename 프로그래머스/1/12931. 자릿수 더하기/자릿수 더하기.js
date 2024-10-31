function solution(n)
{
    return [...String(n)].map(Number).reduce((arr, cur) => arr + cur, 0)
}