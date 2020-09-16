package Java.Sorting;

public class BubbleSort {
    public static void main(String[] args) {
        int[] nums = { 5, 2, 4, 6, 1, 3 };
        bubbleSort(nums);
        for (int i = 0; i < nums.length; i++)
            System.out.println(nums[i]);
    }

    public static void bubbleSort(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (nums[j] > nums[i]) {
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }
            }
        }
    }
}