function getAlternates(arr) {
    let res = [];

    for(let i = 0; i < arr.length; i += 2) {
        res.push(arr[i])
    }
    return res;
}

const arr = [10,20,30,40,50];
const res = getAlternates(arr)
console.log(res)