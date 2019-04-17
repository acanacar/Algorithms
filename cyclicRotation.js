// [1,2,3,4,5,6]  -->  123456123456123456|=>123456<=|123456123456123456
// the number between arrows are our exact list

function rotate(L, R) {
  const lengthL = L.length
  R = R % lengthL
  if (R === 0 || lengthL === 0) {
    return L
  } else {
    return L.slice(lengthL - R).concat(L.slice(0, -R))
  }
}


