import numpy as np
from keras.models import Model
from keras.layers import Dense, Dropout, Input, Lambda, Flatten
from keras.optimizers import RMSprop
from keras import backend as K
from keras.utils import to_categorical
import random
from utils import image_quintuple_generator as iqg
import reid_net
from sklearn.preprocessing import LabelBinarizer as LB
from keras.image import ImageDataGenerator as IDG

input_shape = (224,224,3,)
epochs = 20
batch_size = 16

f = np.load('../data/input.lst.npz')
data = f['tuples']

model = reid_net.reid_net(input_shape=input_shape)

model.fit_genrator(iqg(data,batch_size=),steps_per_epoch=5000, epochs=5)

model.save_weights('../data/model_weights.h5')



# test on train data set
pred_model = Model(inputs=model.input[0], outputs=model.output[1])
f = np.load('../data/input.lst.npz')
x_lst = f['data']
x_train = utils.extract_data_from_lst(x_lst,False)
pred_y = pred_model.predict(x_train):
pred_y = np.argmax(pred_y, axis = 1)
lb =  LB()
lb.fit(y_train)
accuracy = np.mean(lb.classes_[pred_y] == y_train)
print('trained model accuracy {}'.format(accuracy))
