# bdtransjs
百度翻译API
设置headsers后,发送请求只能翻译一个
使用chrome开发者工具获取post接口发送请求
发现每个单词form表单的sign值都不相同，对其进行了加密
通过api发现了两个js文件
在两个js文件中查找加密该字段的js代码
搜索关键字sign: 在index.js第６２９行发现了该内容，调用了m()方法
回到chrome开发者工具，找到js文件，６２９行，开启debug模式，再次进行测试
发现了m()方法，找到m()对应的function
将该段js代码复制到文件中，使用pyexecjs加载js代码
对自己需要翻译的内容生成sign
再次发送请求，成功！
