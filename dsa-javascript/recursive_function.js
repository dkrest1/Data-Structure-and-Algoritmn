function countDown(num) {
    if(num < 0) {
        console.log("all done")
        return
    }

    console.log(num)
    num--
    countDown(num)
}

function rangeOfNum(num) {
    if (num === 1) {
        return 1
    }

    return num + rangeOfNum(num -1)
    
}