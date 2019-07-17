def bubbleSort(arr):
    """
    BubbleSort 冒泡排序
    :param arr: 待排序数组
    :return:
    """

    flag = False
    for n in range(len(arr) - 1):
        for i in range(len(arr) - n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = True
        if not flag:  # 如果没有进行过数据交换，则无需再进行排序
            break
        else:
            flag = False

    return arr


def selectionSort(arr):
    """
    SelectionSort 选择排序
    :param arr: 待排序数组
    :return:
    """

    for i in range(len(arr) - 1):
        _min = arr[i]
        min_index = i
        for j in range(i + 1, len(arr)):
            if _min > arr[j]:
                _min = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def insertSort(arr):
    """
    InsertSort 插入排序
    :param arr: 待排序数组
    :return:
    """

    for i in range(1, len(arr)):
        val = arr[i]
        index = i - 1
        while (index >= 0) & (val < arr[index]):
            arr[index + 1] = arr[index]
            index -= 1

        arr[index + 1] = val

    return arr


def shellSotr(arr):
    """
    ShellSort 希尔排序
    :param arr: 待排序数组
    :return:
    """

    n = len(arr) // 2
    while n > 0:
        for i in range(n):
            for j in range(i + n, len(arr), n):
                for k in range(j, i, -n):
                    temp = arr[k]
                    index = k
                    if temp < arr[k - n]:
                        arr[k] = arr[k - n]
                        index -= n
                    arr[index] = temp

        n = n // 2
