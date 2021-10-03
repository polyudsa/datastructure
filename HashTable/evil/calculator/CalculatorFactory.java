package HashTable.evil.calculator;

import HashTable.evil.parameters.Parameters;
import java.util.HashMap;
import java.util.Map;

/**
 * 计算hash值工厂模式
 * @Author: Twiss
 * @Date: 2021/10/3 12:51 下午
 */
public class CalculatorFactory {

    public Map<Double,String> hashTableMap(Integer type, Parameters parameters) throws Exception {
        Map<Double,String> hashTable = new HashMap<>();
        if (CalculatorType.LINEAR.equals(type)){
            hashTable = new LinearProbing().getIndexMap(parameters);
        }else if (CalculatorType.QUADRATIC.equals(type)){
            hashTable = new QuadraticProbing().getIndexMap(parameters);
        } else if (CalculatorType.CHAINING.equals(type)){
            hashTable =  new Chaining().getIndexMap(parameters);
        }
        return hashTable;
    }
}
