package com.twiss.xiaohuang.util.common;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.SerializerFeature;

/**
 * @Author: Twiss
 * @Date: 2021/10/4 1:24 下午
 */
public class CommonUtil {

    public String jsonFormat(Object res){
        return JSON.toJSONString(res, SerializerFeature.PrettyFormat, SerializerFeature.WriteMapNullValue,
                SerializerFeature.WriteDateUseDateFormat);
    }
}
