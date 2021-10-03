package HashTable.evil.calculator;

import de.congrace.exp4j.Calculable;
import de.congrace.exp4j.ExpressionBuilder;

import java.util.Map;

/**
 * 计算哈希值
 * @Author: Twiss
 * @Date: 2021/10/3 1:38 下午
 */
public class CalculatorHashValue{

    public Double calculatorIndex(Map<String, Integer> variables, String expression) throws Exception {
        // 构建表达式，并声明变量定义。 例如 h(x) = x mod 9 expression 是 x%m
        ExpressionBuilder builder = new ExpressionBuilder(expression);
        // 设置变量
        for (String key:variables.keySet()){
            builder.withVariableNames(key);
        }
        // 以下两种方式也可以声明变量，并直接给变量进行赋值
        // 生成计算对象
        Calculable calc = builder.build();

        // 设置变量的值
        for (String key:variables.keySet()){
            calc.setVariable(key, variables.get(key));
        }
        // 计算结果
        return calc.calculate();
    }
}
