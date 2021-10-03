package HashTable.evil.calculator;

import HashTable.evil.parameters.Parameters;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 链表结构
 * @Author: Twiss
 * @Date: 2021/10/3 1:28 下午
 */
public class Chaining extends AbstractCalculator{

    @Override
    protected Map<Double,String> getIndexMap(Parameters parameters) throws Exception {
        Map<Double, List<Integer>> resultHashIndex = new HashMap<>();
        int[] array = parameters.getNums();
        int m = parameters.getM();
        String expression = parameters.getExpression();
        Map<String,Integer> variables = new HashMap<>();
        // 设置阿尔法值
        variables.put("m",m);
        for (int x : array) {
            // 设置k值
            variables.put("x",x);
            Double index = new CalculatorHashValue().calculatorIndex(variables, expression);

            if (resultHashIndex.get(index)!=null){
                resultHashIndex.get(index).add(x);
            }else {
                resultHashIndex.put(index,new ArrayList<Integer>(){{add(x);}});
            }
        }

        return convert(resultHashIndex);
    }

    private Map<Double,String> convert(Map<Double, List<Integer>> map){
        Map<Double,String> res = new HashMap<>();
        for (Double index : map.keySet()){
            List<Integer> lists = map.get(index);
            StringBuilder stringBuilder = new StringBuilder();
            for (int i=0;i<lists.size();i++){
                if (i!=lists.size()-1){
                    stringBuilder.append(lists.get(i)).append(", ");
                }else {
                    stringBuilder.append(lists.get(i));
                }
            }
            res.put(index,stringBuilder.toString());
        }
        return res;
    }
}
