package HashTable.evil.parameters;

/**
 * @Author: Twiss
 * @Date: 2021/10/3 11:50 上午
 */
public class Parameters {
    // 输入数组
    private int[] nums;
    // 给的要除的alpha
    private int m;
    // 哈希计算表达式
    private String expression;

    public Parameters(){

    }

    public Parameters(int[] arrays, int m, String expression){
        this.nums = arrays;
        this.m = m;
        this.expression = expression;
    }

    public int[] getNums() {
        return nums;
    }

    public void setNums(int[] nums) {
        this.nums = nums;
    }

    public int getM() {
        return m;
    }

    public void setM(int m) {
        this.m = m;
    }

    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
}
