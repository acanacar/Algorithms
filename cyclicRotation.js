// [1,2,3,4,5,6]  -->  123456123456123456|=>123456<=|123456123456123456
// the number between arrows are our exact list

function rotate(L, R) {
  const lengthL = L.length
  const result = (lengthL > 0) ? L.slice(lengthL - R) + L.slice(0, -R) : L
  return result
}

rotate([0,1,2,3,9,1,5,7,12,14],32)
