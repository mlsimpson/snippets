const euros = [29.76, 41.85, 46.5];

const average = euros.reduce((total, amount, index, array) => {
  total += amount;
  if( index === array.length-1) {
    return total/array.length;
  }else {
    return total;
  }
});

average // 39.37

