# create model architechture

from keras.models import Sequential
from keras.layers import Dense, MaxPooling2D,Flatten,Convolution2D
import random

model = Sequential()
for i in range(0,random.choice([1,2,3])):
	model.add(Convolution2D(filters=random.choice([32,64]),kernel_size=random.choice([(3,3),(5,5),(7,7)]),activation='relu',input_shape=(64,64,3)))

model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(units=random.choice([10,16,32,64,128]),activation='relu',input_shape=(28,28)))
i=1
while i<=random.choice([1,2,3,4,5,6]):
  model.add(Dense(units=random.choice([10,16,32,96,64,256,128]),activation='relu'))
  i+=1
model.add(Dense(units=1,activation='sigmoid'))
model.compile(optimizer=random.choice(["adam","RMSprop"]),loss="binary_crossentropy",metrics=['accuracy'])
model.summary()

# prepare dataset

from keras_preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory(
        '/dlcode/cnn_dataset/training_set/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
test_set = test_datagen.flow_from_directory(
        '/dlcode/cnn_dataset/test_set/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

# train model

history = model.fit(training_set,steps_per_epoch=50,epochs=10,validation_data=test_set,validation_steps=10)

# store accuracy 

accuracy = open('/dlcode/accuracy.txt','w+')
accuracy.write(str(history.history['accuracy'][-1]))
accuracy.close()


# save model
model.save("trained_model.h5")