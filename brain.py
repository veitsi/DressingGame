from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import LinearLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import numpy

def sindex(ds,arr):
    for i in range(len(ds['input'])):
        if numpy.array_equal(ds['input'][i],arr):
            return i
    return -1

# r=[]
# for i in range(300):
#     net = buildNetwork(6, 4, 1, outclass=LinearLayer)
#     r.append(net.activate([0,0,3, 1,4,1]))
# print(max(r),min(r))
#
net = buildNetwork(6, 4, 1, outclass=LinearLayer)

ds = SupervisedDataSet(6, 1)
ds.addSample((0, 0, 1, 0, 3, 1), (0,))
ds.addSample((4, 1, 3, 0, 2, 1), (1,))
ds.addSample((4, 1, 3, 0, 2, 1), (0,))

print(len(ds))

print(sindex(ds,[4, 1, 3, 0, 2, 1]))

print(ds['input'][0])
ds['input'][0][1] = 1
print(ds['input'][0])

trainer = BackpropTrainer(net, ds)
trainer.trainUntilConvergence()

print(net.activate([4, 1, 3, 0, 2, 1]))
