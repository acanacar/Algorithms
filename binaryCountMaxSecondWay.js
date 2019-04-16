// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function dec_to_bin(n){
  return parseInt(n,10).toString(2);
}


function solution(N) {
  const arr_Binary = dec_to_bin(N).split('')

  const indices = []
  for (const [index,element] of arr_Binary.entries())
    if (element==='1'){indices.push(index)}

  const l = []
  let i;
  for (i=0;i<indices.length-1;i++){
    l.push(indices[i+1]-indices[i]-1)
  }
  const maxx = Math.max.apply(Math,l)
  return indices,l,maxx
  // write your code in JavaScript (Node.js 8.9.4)
}
