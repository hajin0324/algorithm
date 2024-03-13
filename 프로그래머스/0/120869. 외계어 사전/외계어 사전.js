function solution(spell, dic) {
    return dic.some(e => [...e].sort().toString() == spell.sort().toString()) ? 1 : 2
}