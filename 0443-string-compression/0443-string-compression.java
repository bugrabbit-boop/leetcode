class Solution {
    public int compress(char[] chars) {

        int index = 0; // Position to write compressed characters
        int i = 0;

        while (i < chars.length) {

            char current = chars[i];
            int count = 0;

            // Count consecutive characters
            while (i < chars.length && chars[i] == current) {
                count++;
                i++;
            }

            // Write character
            chars[index++] = current;

            // Write count if greater than 1
            if (count > 1) {
                String num = String.valueOf(count);

                for (char c : num.toCharArray()) {
                    chars[index++] = c;
                }
            }
        }

        return index;
    }
}