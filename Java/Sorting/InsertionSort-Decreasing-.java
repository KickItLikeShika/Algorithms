package Java.Sorting;

public class InsertionSortDecreasing {

    public static void main(String[] args) {
        int[] nums = { 5, 2, 4, 6, 1, 3 };
        insertionSortDecreasing(nums);
        for (int i = 0; i < nums.length; i++) {
            System.out.println(nums[i]);
        }
    }

    public static void insertionSortDecreasing(int[] nums) {
        for (int j = 1; j < nums.length; j++) {
            int key = nums[j];
            int i = j - 1;
            while (i > -1 && nums[i] < key) {
                nums[i + 1] = nums[i];
                i--;
            }
            nums[i + 1] = key;
        }
    }
}