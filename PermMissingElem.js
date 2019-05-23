function solution(A) {
  const n = A.length
  const sumWithoutMissingValue = parseInt((n + 1) * (n + 2) / 2)
  const arrSum = arr => arr.reduce((a, b) => a + b, 0)
  const sumWithMissingValue = arrSum(A)
  return sumWithoutMissingValue-sumWithMissingValue
}

solution([2,1,3,5])
