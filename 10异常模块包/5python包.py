from package import module
module.info_print()

from package import *
# module.info_print()
# 这里无法使用的原因是在包的init文件没有all他所以当导入*的时候就无法使用
module_new.info_print1()