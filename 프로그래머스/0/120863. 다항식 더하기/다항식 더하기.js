function solution(polynomial) {
    let x_num = 0, cons = 0;
    
    polynomial.split(' + ').forEach(i => {
        if (Number(i)) {
            cons += Number(i);
        } else {
            x_num += i == 'x' ? 1 : Number(i.slice(0, -1));
        }
    })
    
    if (x_num == 0) {
        return String(cons);
    } else if (x_num == 1) {
        return cons == 0 ? 'x' : ('x + ' + cons);
    } else {
        return cons == 0 ? (x_num + 'x') : (x_num + 'x + ' + cons);
    }
}