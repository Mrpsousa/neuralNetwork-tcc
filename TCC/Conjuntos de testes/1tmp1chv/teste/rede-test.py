from keras.models import Sequential
from keras.layers import Dense
import numpy
import pandas as pd

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load pima indians dataset
train_data_path ='train.csv'
dataset = pd.read_csv(train_data_path)
# split into input (X) and output (Y) variables
X = dataset[:,0:88]
Y = dataset[:,88]
# create model
model = Sequential()
model.add(Dense(12, input_dim=6, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, nb_epoch=150, batch_size=10)
# evaluate the model
scores = model.evaluate(X, Y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))