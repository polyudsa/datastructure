package HashTable.evil.calculator;


import HashTable.evil.parameters.Parameters;

import java.util.Map;

/**
 * 计算索引抽象类
 * @Author: Twiss
 * @Date: 2021/10/3 11:47 上午
 */
public abstract class AbstractCalculator implements Calculator {
    /**
     * 计算哈希表index
     *
     * @return
     * @throws Exception
     */
    @Override
    public Map<Double,String> execute(Parameters parameters) throws Exception {
        return getIndexMap(parameters);
    }

    protected abstract Map<Double,String> getIndexMap(Parameters parameters) throws Exception;
}
