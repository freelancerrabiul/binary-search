const binarySearch = (arr, target) => {
  left = 0
  right = arr.length -1
  mid = 0

  while (left<= right) {
    mid = Math.floor((left + right) / 2)
    if (arr[mid] > target) right = mid - 1
    else if (arr[mid] < target) left = mid + 1
    else return `Element is present at index ${mid}`
  }
  return 'Element does not exist!'
}




const list = [1,2,3,4,5,6,7,8,9,10]
const target = 10
let bs = binarySearch(list, target)
console.log(bs)