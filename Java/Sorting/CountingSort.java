package Java.Sorting;

public class CountingSort {

    public static void main(String args[]) {
        int[] nums = { 2, 5, 3, 0, 2, 3, 0, 3 };
        int[] output = countSort(nums, 6);
        System.out.println("Sorted Array in Ascending Order: ");
        for (int i = 0; i < output.length; i++)
            System.out.println(output[i]);
    }

    public static int[] countSort(int nums[], int k) {
        int[] output = new int[nums.length];
        int[] count_occurrences = new int[k];

        // Initialize count array with all zeros.
        for (int i = 0; i < k; ++i) {
            count_occurrences[i] = 0;
        }

        // Store the count of each element
        for (int i = 0; i < nums.length; i++) {
            count_occurrences[nums[i]]++;
        }

        // Store the cummulative count of each array
        for (int i = 1; i < k; i++) {
            count_occurrences[i] += count_occurrences[i - 1];
        }

        // Find the index of each element of the original array in count array, and
        // place the elements in output array
        for (int i = 0; i < nums.length; i++) {
            output[count_occurrences[nums[i]] - 1] = nums[i];
            count_occurrences[nums[i]]--;
        }
        return output;
    }
}
