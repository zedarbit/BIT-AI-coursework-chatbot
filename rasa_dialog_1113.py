# import time
# import subprocess
#
# subp_start = subprocess.Popen('rasa shell',shell=True)
# # def cmd(command):
# #     subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
# #     # subp.wait(2)
# #     if subp.poll() == 0:
# #         print(subp.communicate()[1])
# #     else:
# #         print("失败")
#
#
#
# # cmd("rasa shell")
# # cmd("你好")
# from pip._internal import commands


# 不能实现交互
# import subprocess
#
# cmd = "rasa shell"
# start_cmd = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True)
# # dia_cmd = subprocess.getoutput("你好")
# start_cmd.stdin.write(b"nihao")
# # start_cmd.communicate("你好")
# out = start_cmd.stdout.read().decode("GBK")
# print(out)
import os
import subprocess

# proc = subprocess.Popen('rasa shell', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # To avoid deadlocks: careful to: add \n to output, flush output, use
# # readline() rather than read()
# proc.stdin.write(u'nihao\n')
# # 当将输入发送到行解释器时，不要忘记发送实际的换行符
# proc.stdin.flush()  # 将数据放入流后，始终刷新流，因为它可能会被缓冲
# print(proc.stdout.readline())  # 从行解释器获取输入
#
# proc.stdin.close()
# proc.terminate()
# proc.wait(timeout=0.2)


# os.system("shell command argusFormat" )
print("shhhh")