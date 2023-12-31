public class BinarySearch {
    // Returns the index of the target element in the array, or -1 if not found
    static int binarySearch(int arr[], int target) {
        int left = 0, right = arr.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;

            // Check if the target is present at the middle
            if (arr[mid] == target)
                return mid;

            // If the target is greater, ignore the left half
            if (arr[mid] < target)
                left = mid + 1;

            // If the target is smaller, ignore the right half
            else
                right = mid - 1;
        }

        // Target not present in the array
        return -1;
    }

    public static void main(String args[]) {
        int arr[] = { 2, 3, 4, 10, 40 };
        int target = 10;

        int result = binarySearch(arr, target);

        if (result == -1)
            System.out.println("Element not present in the array");
        else
            System.out.println("Element found at index " + result);
    }
}


public class QuickSort {
    // Sorts the array using the QuickSort algorithm
    static void quickSort(int arr[], int low, int high) {
        if (low < high) {
            // Find the pivot element such that elements smaller than the pivot are on the left,
            // and elements greater than the pivot are on the right
            int pivotIndex = partition(arr, low, high);

            // Recursively sort the sub-arrays
            quickSort(arr, low, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, high);
        }
    }

    // Helper method for partitioning the array
    static int partition(int arr[], int low, int high) {
        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;

                // Swap arr[i] and arr[j]
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        // Swap arr[i+1] and arr[high] (pivot)
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        return i + 1;
    }

    public static void main(String args[]) {
        int arr[] = { 10, 7, 8, 9, 1, 5 };
        int n = arr.length;

        quickSort(arr, 0, n - 1);

        System.out.println("Sorted array:");
        for (int i : arr) {
            System.out.print(i + " ");
        }
    }
}
