import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy import ndimage
from matplotlib.backends.backend_pdf import PdfPages

font = {'family' : 'normal',
        'size'   : 20}

matplotlib.rc('font', **font)

class CIFAR10:
    def __init__(self):
        pass
    def natural(self):
        return [0.4425, 0.6407, 0.6890, 0.6857, 0.7016, 0.7735, 0.7838, 0.7552, 0.7781, 0.8071, 0.7816, 0.8244, 0.8310, 0.8083, 0.8116, 0.8041, 0.8163, 0.8064, 0.8159, 0.8309, 0.8277, 0.8211, 0.8318, 0.7793, 0.8137, 0.8262, 0.8039, 0.8215, 0.8080, 0.8240, 0.8314, 0.8372, 0.8104, 0.8426, 0.8206, 0.8202, 0.8402, 0.8213, 0.8249, 0.8363, 0.8421, 0.8437, 0.8457, 0.8324, 0.8525, 0.8460, 0.8289, 0.8408, 0.8314, 0.8443, 0.8479, 0.8209, 0.8236, 0.8179, 0.8377, 0.8141, 0.7981, 0.8293, 0.8199, 0.8220, 0.8401, 0.8235, 0.8417, 0.8391, 0.8470, 0.8594, 0.8572, 0.8394, 0.8582, 0.8531, 0.8394, 0.8576, 0.8562, 0.8495, 0.8376, 0.8601, 0.8570, 0.8523, 0.8504, 0.8329, 0.8254, 0.8829, 0.8855, 0.8863, 0.8863, 0.8868, 0.8860, 0.8873, 0.8866, 0.8867, 0.8865, 0.8880, 0.8881, 0.8881, 0.8882, 0.8884, 0.8882, 0.8882, 0.8884, 0.8883, 0.8883, 0.8886, 0.8880, 0.8887, 0.8875, 0.8880, 0.8882, 0.8881, 0.8889, 0.8885, 0.8880, 0.8884, 0.8877, 0.8889, 0.8890, 0.8898, 0.8881, 0.8886, 0.8888, 0.8884, 0.8890, 0.8880, 0.8883, 0.8874, 0.8892, 0.8888, 0.8876, 0.8891, 0.8882, 0.8887, 0.8879, 0.8881, 0.8876, 0.8888, 0.8886, 0.8884, 0.8877, 0.8876, 0.8878, 0.8887, 0.8879, 0.8875, 0.8884, 0.8874, 0.8886, 0.8879, 0.8872, 0.8877, 0.8875, 0.8881, 0.8878, 0.8878, 0.8873, 0.8880, 0.8875, 0.8876, 0.8880, 0.8878, 0.8878, 0.8878, 0.8881, 0.8876, 0.8873, 0.8872, 0.8882, 0.8874, 0.8874, 0.8880, 0.8879, 0.8879, 0.8876, 0.8876, 0.8885, 0.8877, 0.8885, 0.8880, 0.8882, 0.8878, 0.8883, 0.8888, 0.8877, 0.8873, 0.8878, 0.8877, 0.8881, 0.8883, 0.8877, 0.8874, 0.8883, 0.8886, 0.8882, 0.8874, 0.8879, 0.8876, 0.8883, 0.8874, 0.8885, 0.8876, 0.8870, 0.8878]

    def attack(self):
        return [0.21185, 0.31095, 0.3351 , 0.33345, 0.3414 , 0.37735, 0.3825 ,
       0.3682 , 0.37965, 0.39415, 0.3814 , 0.4028 , 0.4061 , 0.39475,
       0.3964 , 0.39265, 0.39875, 0.3938 , 0.39855, 0.40605, 0.40445,
       0.40115, 0.4065 , 0.38025, 0.39745, 0.4037 , 0.39255, 0.40135,
       0.3946 , 0.4026 , 0.4063 , 0.4092 , 0.3958 , 0.4119 , 0.4009 ,
       0.4007 , 0.4107 , 0.40125, 0.40305, 0.40875, 0.41165, 0.41245,
       0.41345, 0.4068 , 0.41685, 0.4136 , 0.40505, 0.411  , 0.4063 ,
       0.41275, 0.41455, 0.40105, 0.4024 , 0.39955, 0.40945, 0.39765,
       0.38965, 0.40525, 0.40055, 0.4016 , 0.41065, 0.40235, 0.41145,
       0.41015, 0.4141 , 0.4203 , 0.4192 , 0.4103 , 0.4197 , 0.41715,
       0.4103 , 0.4194 , 0.4187 , 0.41535, 0.4094 , 0.42065, 0.4191 ,
       0.41675, 0.4158 , 0.40705, 0.4033 , 0.40205, 0.41335, 0.41375,
       0.41375, 0.414  , 0.4136 , 0.42425, 0.4239 , 0.42395, 0.42385,
       0.4246 , 0.42465, 0.42465, 0.4247 , 0.4248 , 0.4247 , 0.4247 ,
       0.4348 , 0.43475, 0.43475, 0.4349 , 0.4346 , 0.43495, 0.43435,
       0.4346 , 0.4347 , 0.43465, 0.43505, 0.43485, 0.4346 , 0.4348 ,
       0.43445, 0.43505, 0.4351 , 0.4355 , 0.43465, 0.4349 , 0.435  ,
       0.4348 , 0.4351 , 0.4346 , 0.43475, 0.4343 , 0.4352 , 0.435  ,
       0.4344 , 0.43515, 0.4347 , 0.43495, 0.43455, 0.43465, 0.4344 ,
       0.435  , 0.4349 , 0.4348 , 0.43445, 0.4344 , 0.4345 , 0.43495,
       0.43455, 0.43435, 0.4348 , 0.4343 , 0.4349 , 0.43455, 0.4342 ,
       0.43445, 0.43435, 0.43465, 0.4345 , 0.4345 , 0.43425, 0.4346 ,
       0.43435, 0.4344 , 0.4346 , 0.4345 , 0.4345 , 0.4345 , 0.43465,
       0.4344 , 0.43425, 0.4342 , 0.4347 , 0.4343 , 0.4343 , 0.4346 ,
       0.43455, 0.43455, 0.4344 , 0.4344 , 0.43485, 0.43445, 0.43485,
       0.4346 , 0.4347 , 0.4345 , 0.43475, 0.435  , 0.43445, 0.43425,
       0.4345 , 0.43445, 0.43465, 0.43475, 0.43445, 0.4343 , 0.43475,
       0.4349 , 0.4347 , 0.4343 , 0.43455, 0.4344 , 0.43475, 0.4343 ,
       0.43485, 0.4344 , 0.4341 , 0.4345 ]


class GTSRB:
    def __init__(self):
        self.x=[10,20,30]
        
    def natural(self):
        return [0.8217, 0.9116, 0.9512, 0.9550, 0.9450, 0.9535, 0.9519, 0.9558, 0.9473, 0.9550, 0.9636, 0.9589, 0.9636, 0.9535, 0.9581, 0.9581, 0.9659, 0.9682, 0.9426, 0.9566, 0.9713, 0.9651, 0.9636, 0.9605, 0.9682, 0.9690, 0.9566, 0.9698, 0.9550, 0.9721]

    def attack(self):
        return [0.5866 , 0.63155, 0.65135, 0.65325, 0.64825, 0.6525 , 0.6517 ,
       0.65365, 0.6494 , 0.65325, 0.65755, 0.6552 , 0.65755, 0.6525 ,
       0.6548 , 0.6548 , 0.6587 , 0.65985, 0.64705, 0.65405, 0.6614 ,
       0.6583 , 0.65755, 0.656  , 0.65985, 0.66025, 0.65405, 0.66065,
       0.65325, 0.6618 ]


fig = plt.figure(figsize=(10, 7))
dataset = CIFAR10()
plt.xlabel('epoch', fontsize=20)
plt.ylabel('test accuracy', fontsize=20)
plt.figure(1)
ax=plt.subplot(111)
#ax.set_aspect(, 0.6)
#plt.axis([0, 1, -, 0.05, 1])
line1, = plt.plot(dataset.natural(), 'g', label="natural test", linewidth=3.0)
line2, = plt.plot(dataset.attack(), 'r--', label="advarsarial attack", linewidth=3.0)
plt.legend()
plt.show()
