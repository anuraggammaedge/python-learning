# import numpy
import numpy as np
# arr = numpy.array([1,2,3,4,5])
arr = np.array([1,2,3,4,5])

# print(np.__version__)

# print(arr)
# print(type(arr))
# print("Array Dimension ", arr.ndim)

ndArray = np.array((1,2,3,4,5))
# print(ndArray)
# print(type(ndArray))
# print("Array Dimension ", ndArray.ndim)

arr_2d = np.array([[1,2,3], [9,8,7]])
# print(arr_2d)
# print(type(arr_2d))
# print("Array Dimension ", arr_2d.ndim)
# print('2nd element on 1st row: ', arr_2d[1, 1])
# print('2nd element on 1st row: ', arr_2d[1, -1])


# slice

arr_slice = np.array([1,2,3,4,5,6,7])
print(arr_slice[1:5])
print(arr_slice[4:])
print(arr_slice[:4])
print(arr_slice[1:5:3])  #step


# Slicing 2-D Arrays
arr_slice_2d= np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr_slice_2d[0, 1:5])

print(arr_slice_2d[0:2, 1:4])


# datatype
arr_dtype = np.array([1,2,3,4,5,6,7], dtype='i')
arr_dtype_str = np.array(["a", "b", "c"], dtype="S")
print(arr_dtype.dtype)
print(arr_dtype_str.dtype)