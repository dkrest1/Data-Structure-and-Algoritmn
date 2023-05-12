function two_pointer(arr) {
    let pointer1 = 0
    let pointer2 = arr.length - 1
   while (pointer1 < pointer2) {
      let sum = arr[pointer1] + arr[pointer2]
       if(sum === 0) {
           return [arr[pointer1], arr[pointer2]]
       }else if (sum > 0) {
           pointer2--
       }else {
           pointer1++
       }
   }
}

two_pointer([1,2,3,4, 4])