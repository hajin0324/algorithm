function solution(my_string) {
    return [...my_string].reduce((acc, cur) => {
        if (!isNaN(cur)) {
            acc += Number(cur)
        }
        return acc;
    }, 0);
}