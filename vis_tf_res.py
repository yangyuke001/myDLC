
import matplotlib.pyplot as plt
from tensorboard.backend.event_processing import event_accumulator
 
#加载日志数据
ea=event_accumulator.EventAccumulator(r'C:\Users\Citydo\Documents\yyk\zju\mypaper\code\DeepLabCut76\test-yyk-2022-09-17\dlc-models\iteration-0\testSep17-trainset50shuffle1\train\log\events.out.tfevents.1663393285.DESKTOP-28HPGCB') 
ea.Reload()
print(ea.scalars.Keys())
 
val_psnr=ea.scalars.Items('locref_loss')
print(len(val_psnr))
# print([(i.step,i.value) for i in val_psnr])


fig=plt.figure(figsize=(6,4))
ax1=fig.add_subplot(111)
locref_loss=ea.scalars.Items('locref_loss')
ax1.plot([i.step for i in locref_loss],[i.value for i in locref_loss],label='locref_loss')
ax1.set_xlim(0)

loss=ea.scalars.Items('part_loss')
ax1.plot([i.step for i in loss],[i.value for i in loss],label='part_loss')


loss=ea.scalars.Items('total_loss')
ax1.plot([i.step for i in loss],[i.value for i in loss],label='total_loss')
ax1.set_xlabel("step")
ax1.set_ylim(0, 0.05)
ax1.set_ylabel("")

plt.legend(loc='upper right')
plt.show()