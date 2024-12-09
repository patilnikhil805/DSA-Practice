function large(arr, N) {
    max = arr[0]

    for (let i = 0; i < N; i++){
        if (arr[i] > max)
            max = arr[i]
    }
    return max
}

arr = [152,235,26,235,23,25,25,62,5]
N = arr.length
res = large(arr, N)
console.log(res)