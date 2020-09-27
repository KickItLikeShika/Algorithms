public class QuickSort {

    public static void main(String[] args) {
        int[] nums = { 5, 2, 4, 6, 1, 3 };
        int n = nums.length;
        quickSort(nums, 0, n - 1);
        for (int i = 0; i < n; ++i)
            System.out.print(nums[i] + " ");
    }

    public static void quickSort(int[] nums, int start, int end) {
        if (start < end) {
            int mid = partition(nums, start, end);
            quickSort(nums, start, mid - 1);
            quickSort(nums, mid + 1, end);
        }
    }

    public static int partition(int[] nums, int start, int end) {
        int pivot = nums[end];
        int i = start - 1;
        for (int j = start; j < end; j++) {
            if (nums[j] < pivot) {
                i++;
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
        i++;
        int temp = nums[i];
        nums[i] = nums[end];
        nums[end] = temp;
        return i;
    }
}