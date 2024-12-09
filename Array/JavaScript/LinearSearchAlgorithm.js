function search(arr,x,N) {
    for (let i=0; i<N; i++) {
        if (arr[i]  == x) 
            return i
    }
    return -1
    
}

arr=[10,20,30,40,50]
x = 40
N = arr.length

let result = search(arr, x, N)
console.log(result)