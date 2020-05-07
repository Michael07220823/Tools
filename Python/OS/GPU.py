from gpuinfo import GPUInfo

available_device=GPUInfo.check_empty()
#available_device就是一个含有所有没有任务的gpu编号的列表
print(available_device)

percent,memory=GPUInfo.gpu_usage()
#获得所有gpu的使用百分比和显存占用量
print(percent, memory)

min_percent=percent.index(min([percent[i] for i in available_device]))
#未被使用的gpu里percent最小的
print(min_percent)

min_memory=memory.index(min([memory[i] for i in available_device]))
#未被使用的gpu里显存占用量最少的

print(min_memory)