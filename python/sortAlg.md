# 排序算法

太长时间没有学习排序算法了。早已经忘记如何排序了。。。学习学习

![排序算法](https://www.runoob.com/wp-content/uploads/2019/03/0B319B38-B70E-4118-B897-74EFA7E368F9.png)

往往在一些算法题目里面会要求时间复杂度，或者空间复杂度。这样的话上述一张表格就十分有用了。记得之前看过的O(logn)的时间复杂度，基本都代表着二分查找法。

让我们一一道来。

## 冒泡排序

算法：从头遍历到尾，每次循环的时候从第一个元素开始，逐次将当前元素和下一元素进行大小比较。把较大的元素向后移动。实现从小打大排序。

第一个循环，将第一个元素到N-1个元素分别与后面的元素比较，较大的则交换元素。  
每次递增循环的时候，由于靠后的元素顺序已经排好了。所以每次循环的时候将需要循环的元素个数-1.  
直到最后循环只需要比较第一个和第二个元素。

```python3
def bubbleSort(arr):
	for i in range(1, len(arr)):
		for j in range(0, len(arr)-i):
			if arr[j]>arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr
```

这个算法是在远数组的基础上进行数值的替换。所以空间复杂度位 O(1)。  
循环套循环的时间复杂度为O(N<sup>2</sup>)

## 选择排序

循环多次，每次从未排序数组中找到最小的放到未排序数组的第一位。  
第一次将最小的放在第一位，第二次将最小的放在第二位，以此类推

```python3
def selectionSort(arr):
	for i in range(0, len(arr)-1):
		min_index = i
		for j in range(i+1, len(arr)):
			if arr[j]<arr[min_index]:
				min_index = j
		if min_index!=i:
			arr[min_index],arr[i] = arr[i], arr[min_index]
	return arr
```

因为数组每次比较是从当前元素的下一个元素和当前元素比较大小的，所以内套的循环从i+1开始。
空间复杂度O(1)和时间复杂度O(N<sup>2</sup>)同上

## 插入排序

将第一个数组元素当作是已经排序好的数组。将后面的元素当作未排序序列。  
遍历未排序序列，每次将元素插入排序序列的对应位置。

```python3
def insertionSort(arr):
	for i in range(len(arr)):
		preIndex = i-1
		current = arr[i]

		while preIndex>=0 and arr[preIndex] > current:
			arr[preIndex+1] = arr[preIndex]
			preIndex-=1
		acc[preIndex+1] = current
	return arr
```

从当前遍历位置往前遍历排序好的序列。直到将所有的大于当前元素的元素后移完全之后，将该元素插入。

空间复杂度O(1)和时间复杂度O(N<sup>2</sup>)同上

### 二分插入排序

## 希尔排序

属于插入排序的一种高效版本。但是不太稳定。  
希尔排序是将数组从无序->基本有序->有序的一个过程。

```python3
def shellSort(arr):
    import math
    gap=1

    while(gap < len(arr)/3):
        gap = gap*3+1

    while gap > 0:
        for i in range(gap,len(arr)):
            temp = arr[i]
            j = i-gap
            while j >=0 and arr[j] > temp:
                arr[j+gap]=arr[j]
                j-=gap
            arr[j+gap] = temp
        gap = math.floor(gap/3)
    return arr
```

将数组里面的元素按照gap分为不同的组合，先对这个组合排序。   
对gap进行递减操作，每次哦度灰重新分组，并重新排序。  
知道最后gap为一，数组只有一组的时候，进行最后一次排序。  
while 循环中间的部分可以看作一个插入排序。 这边每次距离gap位的第j个元素就是插入排序里面的preIndex.

## 归并排序

归并就是将两个数组合并的意思。  
将数组分位两个数组，对两个数组进行排序。对排序好的数组进行插入归并。  
可以将此过程加上递归操作。将最小的数组只包含两个元素。组成递归，最终将所有的元素合并。

```python3
def mergeSort(arr):
    import math
    if(len(arr)<2):
        return arr
    middle = math.floor(len(arr)/2)
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0));
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0));
    return result
```

## 快速排序

将第一个元素作为基准，将所有比他小的元素移到他的前面。
然后对基准前后的分区循环采用分区的操作。最后所有的数组都被有序排列。

```python3
def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(arr)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr

def partition(arr, left, right):
    pivot = left
    index = pivot+1
    i = index
    while  i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index+=1
        i+=1
    swap(arr,pivot,index-1)
    return index-1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
```

## 堆排序

```python3
def buildMaxHeap(arr):
    import math
    for i in range(math.floor(len(arr)/2),-1,-1):
        heapify(arr,i)

def heapify(arr, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        arrLen -=1
        heapify(arr, 0)
    return arr
```

## 计数排序

先找到最大值和最小值。对最大值和最小值范围内的所有的数字进行计数。
然后按序填充相应个数的数字，完成排序。

```python3
def countingSort(arr, maxValue):
    bucketLen = maxValue+1
    bucket = [0]*bucketLen
    sortedIndex =0
    arrLen = len(arr)
    for i in range(arrLen):
        if not bucket[arr[i]]:
            bucket[arr[i]]=0
        bucket[arr[i]]+=1
    for j in range(bucketLen):
        while bucket[j]>0:
            arr[sortedIndex] = j
            sortedIndex+=1
            bucket[j]-=1
    return arr
```

对数组元素范围较小的排序比较友好。

## 桶排序

将元素放在代表对应取值范围的桶里面。每个桶进行排序。然后组合输出。

## LSD基数排序

先将元素按照个位数放入不同的桶内，然后取出。  
再将元素按照十位数放入不同的桶内，取出就是排好序的结果。

xiang

# 参考目录
[排序-维基](https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95)