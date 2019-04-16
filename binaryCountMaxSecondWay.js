function dec_to_bin(n) {
  return parseInt(n, 10).toString(2)
}

function solution(N) {
  const arr_Binary = dec_to_bin(N).split('')

  const indices = []
  for (const [index, element] of arr_Binary.entries())
    if (element === '1') {indices.push(index)}

  const l = []
  let i
  for (i = 0; i < indices.length - 1; i++) {
    l.push(indices[i + 1] - indices[i] - 1)
  }
  const result = (l.length > 0) ? Math.max.apply(Math, l) : 0
  return result
}
