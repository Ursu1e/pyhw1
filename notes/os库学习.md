## import os
<font size = "4"> 获取脚本所在路径的绝对路径方法:<br> 
```py
import os 
path_dir = os.path.dirname(os.path.abspath(__file__)) # 获取脚本的工作文件夹的绝对路径
file_path = os.path.join(path_dir,'') # 引号里面为文件的名称
```