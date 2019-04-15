// 'Find longest sequence of zeros in binary representation of an integer.'

function dec2bin(n) {
  return parseInt(n, 10).toString(2)
}

function findIntervals(arrBin, intervals) {
  // '1101100011001110110'
  let firstIndex = arrBin.indexOf('1')
  //0
  let remainPart = arrBin.slice(firstIndex + 1)
  // '101100011001110110'
  let secondIndex = remainPart.indexOf('1')
  if (secondIndex > -1) {
    if (secondIndex !== 0) {
      intervals.push(secondIndex)
    }
    let willRemainPart = remainPart.slice(secondIndex)
    if (willRemainPart.length > 0) {
      findIntervals(willRemainPart, intervals)
    }
  }
  return intervals
}

const x = 444022
const binaryX = dec2bin(x)
