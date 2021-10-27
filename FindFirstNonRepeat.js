// Write an efficient function to find the first nonrepeated character
// in a string. For instance, the first nonrepeated character in “total” is ‘o’ and
// the first nonrepeated character in “teeter” is ‘r’. Discuss the efficiency of your
// algorithm

function findFirstNonRepeat(word) {
    const arr = [];
    const obj = {};
    for (let i = 0; i < word.length; i++) {
      if (arr.includes(word[i])) {
        obj[word[i]]++;
      } else {
        arr.push(word[i]);
        obj[word[i]] = 1;
      }
    }
    console.log(obj)
    console.log(arr);
    for (let i = 0; i < arr.length; i++) {
      console.log(obj[arr[i]])
      if (obj[arr[i]] == 1) {
        return arr[i];
      }
    }
  }
  
  console.log(findFirstNonRepeat('teeter'))

  // the efficiency of the algorithm is O(2n) -> O(n).