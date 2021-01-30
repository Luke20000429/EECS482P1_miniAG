# EECS482P1_miniAG

使用方法

将可执行文件放到该目录下

先运行

access 的范围是0-1000

每个文件长度都一样

```shell
python Gen.py [testcase数目] [每个文件长度]
>>> testdisk.in0 testdisk.in1 .....
```

运行程序

```shell
[可执行文件名] max_disk_queue testdisk*
```

自动生成一个ans文件

运行检查程序

```shell
python check.py max_disk_queue [testcase数目] [每个文件长度]
```

