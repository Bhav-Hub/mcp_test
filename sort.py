#!/usr/bin/env python3
"""
sort.py - A utility script to sort arrays using various algorithms
"""

def bubble_sort(arr):
    """
    Implementation of bubble sort algorithm.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        # Flag to optimize if array is already sorted
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # If no swapping occurred in this pass, array is sorted
        if not swapped:
            break
            
    return arr

def quick_sort(arr):
    """
    Implementation of quick sort algorithm.
    Time Complexity: O(n log n) average case, O(n^2) worst case
    Space Complexity: O(log n)
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    """
    Implementation of merge sort algorithm.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    # Divide array in half
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    """Helper function for merge sort"""
    result = []
    i = j = 0
    
    # Compare elements from both lists and add smaller one to result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def insertion_sort(arr):
    """
    Implementation of insertion sort algorithm.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original array:", test_array)
    print("Bubble sort:", bubble_sort(test_array.copy()))
    print("Quick sort:", quick_sort(test_array.copy()))
    print("Merge sort:", merge_sort(test_array.copy()))
    print("Insertion sort:", insertion_sort(test_array.copy()))
