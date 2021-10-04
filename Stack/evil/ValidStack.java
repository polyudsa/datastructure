package com.twiss.xiaohuang.util.stack;

import com.alibaba.fastjson.JSONObject;

import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Stack;

/**
 * @Author: Twiss
 * @Date: 2021/10/4 1:08 下午
 */
public class ValidStack {
    public static boolean IsPopOrder(int [] pushA,int [] popA) {
        if(pushA.length == 0 || popA.length == 0)
            return false;
        Stack<Integer> stack = new Stack<Integer>();
        //用于标识弹出序列的位置
        int popIndex = 0;
        for(int i = 0; i< pushA.length;i++){
            //把数压入栈。
            stack.push(pushA[i]);
            //如果栈不为空，且获取到的栈顶元素等于弹出序列
            while(!stack.empty() &&stack.peek() == popA[popIndex]){
                //出栈
                stack.pop();
                //弹出序列向后一位
                popIndex++;
            }
        }

        if(stack.empty()){
            return true;
        }else {
            return false;
        }
    }

    public static void main(String[] args){
        CommonUtil commonUtil = new CommonUtil();
        Map<String,Boolean> res = new LinkedHashMap<>();
        int[] pushA = new int[]{0,1,2,3,4,5,6,7,8,9};
        int[][] popStacks = new int[][]{
                {1,4,3,2,6,7,8,5,9,0},
                {0,6,5,4,3,7,9,8,2,1},
                {1,2,4,3,5,6,9,8,0,7},
                {6,5,7,4,9,8,3,2,1,0},
                {7,6,5,4,8,9,3,1,2,0},
                {3,5,4,2,1,0,6,9,7,8}
        };
        for (int[] popStack:popStacks){
            Boolean isValid = IsPopOrder(pushA, popStack);
            res.put(JSONObject.toJSONString(popStack),isValid);
        }

        System.out.println(commonUtil.jsonFormat(res));
    }
}
