# zzz

个人在`python`交互式环境下常用的一些函数

用途

1. 于个人，使这些函数可以通过`from zzz import xxx`来使用，但这些函数应该不会在个人的任何公开代码中使用
2. 于他人，展示一个简单的python-package结构

## quickstart

1. install `pip install .`
2. uninstall `pip uninstall zzz`
3. use `from zzz import xxx`

## 说明

`check_internet_available()`: 测试网络是否可访问

`hfp()`: 将函数变量送至交互式环境下；函数中的默认变量是这样的格式`(a=1,b=2,c=3)`，将每一个逗号改写成分号略繁琐，故替换为`hfp(a=1,b=2,c=3)`

`to_pickle(**kwargs)`: 将变量用pickle保存至`tbd00.pkl`文件

`from_pickle(key:str)`: 从`tbd00.pkl`文件读取`key`，使用示例见下

```Python
from zzz import to_pickle, from_pickle
a = 233
b = 0.233
to_pickle(a=a, b=b)
from_pickle('a')
from_pickle('b')
```

`python -c "import zzz; zzz.known_hosts()"`：查询所有`known_hosts`
`python -c "import zzz; zzz.known_hosts('[123.45.67.89]:2022')"`：从`known_hosts`中删去`[123.45.67.89]:2022`
