HomeworkCleaner
===============

清理C语言作业中的临时文件

===============

####使用方法：

把HomeworkCleaner.py与要处理的文件夹放在一起，
运行，
HomeworkCleaner.py会将每个文件夹打包到一个zip中，
并在打包时忽略VS生成的临时文件，
以节省空间。

basic: 删除已知类型的临时文件

aggressive: 删除debug、release文件夹下除了exe、 dll外所有文件
