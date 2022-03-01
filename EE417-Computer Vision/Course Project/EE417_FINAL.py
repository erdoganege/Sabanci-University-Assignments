# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 22:25:53 2021

@author: user
"""
import time
import os
from skimage.io import imread, imshow
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt
import glob
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import plot_confusion_matrix
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from keras.layers.normalization import BatchNormalization
from keras.utils.np_utils import to_categorical
import cv2
import tensorflow as tf
from sklearn.utils import class_weight
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

def results(model, X_test, y_test, test_prediction):
    plot_confusion_matrix(model, X_test, y_test)  
    plt.title(model)
    plt.show()
    target_names = ['NOT Pedestrian (0)', 'Pedestrian (1)']
    print(classification_report(y_test, test_prediction, target_names=target_names))

def train_test_model(model, X_train, y_train, X_test, y_test): 
    model.fit(X_train, y_train)
    train_prediction = model.predict(X_train)
    train_acc_score = accuracy_score(train_prediction, y_train)
    print("Training Accuracy: ", train_acc_score)
    test_prediction = model.predict(X_test)
    test_acc_score = accuracy_score(test_prediction, y_test)
    print("Test Accuracy: ", test_acc_score)
    results(model, X_test, y_test, test_prediction)
    return model, train_acc_score, test_acc_score

running_times = []
trainning_accuracies_linear = []
trainning_accuracies_polynomial = []
trainning_accuracies_rfc = []

testing_accuracies_linear = []
testing_accuracies_polynomial = []
testing_accuracies_rfc = []


#%% Loading Positive and Negative Labeled Images
pedestrian_imgs = []
for img in glob.glob("C:/Users/user/Desktop/ComputerVisionDataset/CVC-CER-01/pedestrian/*.png"):
    img = imread(img)    	
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    pedestrian_imgs.append(img)
    
notpedestrian_imgs = []
for img in glob.glob("C:/Users/user/Desktop/ComputerVisionDataset/CVC-CER-01/not-pedestrian/*.png"):
    img = imread(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    notpedestrian_imgs.append(img)
    
print("Number of Pedestrian (Positive Label) images without mirror images:", len(pedestrian_imgs))
print("Number of Non-Pedestrian (Negative Label) images:", len(notpedestrian_imgs))


#%% Detection with HOG Features
print("*****Human Detection with HOG Features*****")
start = time.time()
df = []
label = []
for img in pedestrian_imgs:
    resized_img = resize(img, (64,128)) 
    fd = hog(resized_img, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2))
    df.append(fd)
    label.append(1)

for img in notpedestrian_imgs:
    resized_img = resize(img, (64,128)) 
    fd  = hog(resized_img, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2))
    df.append(fd)
    label.append(0)
end = time.time()
running_times.append(end-start)

X = np.array(df)
y = np.array(label)
print("Total data shape:",X.shape)
print("Labels shape:",y.shape)
print("Number of positive labels {}, negative labels {}, positive/total ratio is {}".format(y.sum(), len(y)-y.sum(), round(y.sum()/len(y), 3)))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("\nUsing Linear SVC")
svc = LinearSVC()
model, train_acc_score, test_acc_score = train_test_model(svc, X_train, y_train, X_test, y_test)
trainning_accuracies_linear.append(train_acc_score)
testing_accuracies_linear.append(test_acc_score)

print("\nUsing Polynomial SVC")
psvc = SVC(kernel="poly")
model, train_acc_score, test_acc_score = train_test_model(psvc, X_train, y_train, X_test, y_test)
trainning_accuracies_polynomial.append(train_acc_score)
testing_accuracies_polynomial.append(test_acc_score)

print("\nUsing Random Forest Classifier")
rcf = RandomForestClassifier()
model, train_acc_score, test_acc_score = train_test_model(rcf, X_train, y_train, X_test, y_test)
trainning_accuracies_rfc.append(train_acc_score)
testing_accuracies_rfc.append(test_acc_score)

#%%Testing HOG with one test image
'''
img = imread('C:/Users/user/Desktop/ComputerVisionDataset/test/frame0033.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imshow(img)

print("Shape of the image:", img.shape)

#part_img = img[116:116+128, 284:284+64]
#imshow(part_img)


for x in range(0, img.shape[0],4):
    for y in range(0, img.shape[1],4):
        if x%200 == 0:
            print("Checkpoint:",x, y)
        window = img[x:x+128, y:y+64]
        if window.shape[0] == 128 and window.shape[1] == 64:
          fd  = hog(window, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2))
          pred = svc.predict(fd.reshape(1,-1))
          if pred == 1:
              if svc.decision_function(fd.reshape(1,-1)) > 3:
                  print("Found pedestrian:", x, y, svc.decision_function(fd.reshape(1,-1)))
            

#%% Adding Mirror Image Data to HOG Detection
print("\n*****Adding Mirror images of Pedestrians to our data*****")
mirror_pedestrian_imgs = []
for img in glob.glob("C:/Users/user/Desktop/ComputerVisionDataset/CVC-CER-01/pedestrian-mirror/*.png"):
    img = imread(img)
    mirror_pedestrian_imgs.append(img)
print("Number of Mirrored Pedestrian (Positive Label) images:", len(mirror_pedestrian_imgs))
for img in mirror_pedestrian_imgs:
    resized_img = resize(img, (64,128)) 
    fd = hog(resized_img, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2))
    df.append(fd)
    label.append(1)
X = np.array(df)
y = np.array(label)
print("*****After adding Mirror Images*****")
print("Total data shape:",X.shape)
print("Labels shape:",y.shape)
print("Number of positive labels {}, negative labels {}, positive/total ratio is {}".format(y.sum(), len(y)-y.sum(), round(y.sum()/len(y), 3)))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
svc = LinearSVC()
svc.fit(X_train, y_train)

train_prediction = svc.predict(X_train)
print("Training Accuracy: ", accuracy_score(train_prediction, y_train))
test_prediction = svc.predict(X_test)
print("Test Accuracy: ", accuracy_score(test_prediction, y_test))
results(svc, X_test, y_test, test_prediction)
'''
#%% Detection with SIFT Features
print("\n*****Human Detection with SIFT Features*****")
start = time.time()
df = []
label = []
for img in pedestrian_imgs:
    sift = cv2.xfeatures2d.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(img, None)
    if descriptors is not None:
        temp = np.resize(descriptors, 128*128)
        df.append(temp)
        label.append(1)

for img in notpedestrian_imgs:
    sift = cv2.xfeatures2d.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(img, None)
    if descriptors is not None:
        temp = np.resize(descriptors, 128*128)
        df.append(temp)
        label.append(0)
end = time.time()
running_times.append(end-start)
X = np.array(df)
y = np.array(label)
print("Total data shape:",X.shape)
print("Labels shape:",y.shape)
print("Number of positive labels {}, negative labels {}, positive/total ratio is {}".format(y.sum(), len(y)-y.sum(), round(y.sum()/len(y), 3)))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("\nUsing Linear SVC")
svc = LinearSVC()
model, train_acc_score, test_acc_score = train_test_model(svc, X_train, y_train, X_test, y_test)
trainning_accuracies_linear.append(train_acc_score)
testing_accuracies_linear.append(test_acc_score)

print("\nUsing Polynomial SVC")
psvc = SVC(kernel="poly")
model, train_acc_score, test_acc_score = train_test_model(psvc, X_train, y_train, X_test, y_test)
trainning_accuracies_polynomial.append(train_acc_score)
testing_accuracies_polynomial.append(test_acc_score)

print("\nUsing Random Forest Classifier")
rcf = RandomForestClassifier()
model, train_acc_score, test_acc_score = train_test_model(rcf, X_train, y_train, X_test, y_test)
trainning_accuracies_rfc.append(train_acc_score)
testing_accuracies_rfc.append(test_acc_score)

#%% Detection with SURF Features
print("\n*****Human Detection with SURF Features*****")
start = time.time()
df = []
label = []
for img in pedestrian_imgs:
    SURF = cv2.xfeatures2d.SURF_create(500)
    kp, des = SURF.detectAndCompute(img, None)
    if des is not None:
        temp = np.resize(des, 64*64)
        df.append(temp)
        label.append(1)

for img in notpedestrian_imgs:
    SURF = cv2.xfeatures2d.SURF_create(500)
    kp, des = SURF.detectAndCompute(img, None)
    if des is not None:
        temp = np.resize(des, 64*64)
        df.append(temp)
        label.append(0)
end = time.time()
running_times.append(end-start)

X = np.array(df)
y = np.array(label)
print("Total data shape:",X.shape)
print("Labels shape:",y.shape)
print("Number of positive labels {}, negative labels {}, positive/total ratio is {}".format(y.sum(), len(y)-y.sum(), round(y.sum()/len(y), 3)))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("\nUsing Linear SVC")
svc = LinearSVC()
model, train_acc_score, test_acc_score = train_test_model(svc, X_train, y_train, X_test, y_test)
trainning_accuracies_linear.append(train_acc_score)
testing_accuracies_linear.append(test_acc_score)

print("\nUsing Polynomial SVC")
psvc = SVC(kernel="poly")
model, train_acc_score, test_acc_score = train_test_model(psvc, X_train, y_train, X_test, y_test)
trainning_accuracies_polynomial.append(train_acc_score)
testing_accuracies_polynomial.append(test_acc_score)

print("\nUsing Random Forest Classifier")
rcf = RandomForestClassifier()
model, train_acc_score, test_acc_score = train_test_model(rcf, X_train, y_train, X_test, y_test)
trainning_accuracies_rfc.append(train_acc_score)
testing_accuracies_rfc.append(test_acc_score)


#%% Show Comparison Results
labels = ['HOG', "SIFT", 'SURF']
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, trainning_accuracies_linear, width, label='Training Accuracy with Linear SVC')
rects2 = ax.bar(x + width/2, testing_accuracies_linear, width, label='Test Accuracy with Linear SVC')
ax.set_ylabel('Accuracy')
ax.set_title('Accuracy Comparisons of Different Feature Extraction Methods with Linear SVC')
ax.set_xticks(x)
ax.set_xticklabels(labels)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
plt.grid()
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

labels = ['HOG', "SIFT", 'SURF']
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, trainning_accuracies_polynomial, width, label='Training Accuracy with Polynomial SVC')
rects2 = ax.bar(x + width/2, testing_accuracies_polynomial, width, label='Test Accuracy with Polynomial SVC')
ax.set_ylabel('Accuracy')
ax.set_title('Accuracy Comparisons of Different Feature Extraction Methods with Polynomial SVC')
ax.set_xticks(x)
ax.set_xticklabels(labels)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
plt.grid()
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

labels = ['HOG', "SIFT", 'SURF']
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, trainning_accuracies_linear, width, label='Training Accuracy with Random Forest')
rects2 = ax.bar(x + width/2, testing_accuracies_linear, width, label='Test Accuracy with Random Forest')
ax.set_ylabel('Accuracy')
ax.set_title('Accuracy Comparisons of Different Feature Extraction Methods with Random Forest')
ax.set_xticks(x)
ax.set_xticklabels(labels)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
plt.grid()
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

fig = plt.figure(figsize = (10, 5))
plt.bar(labels, running_times)
plt.ylabel("Running Time (s)")
plt.title("Running Time of Feature Extraction Methods")
plt.grid()
plt.show()
from tabulate import tabulate
print(tabulate({"Feature Method": labels, "Training Acc. with Linear SVC": trainning_accuracies_linear, "Testing Acc. with Linear SVC": testing_accuracies_linear,
                "Training Acc. with Polynomial SVC": trainning_accuracies_polynomial, "Testing Acc. with Polynomial SVC": testing_accuracies_polynomial,
                "Training Acc. with RFC": trainning_accuracies_rfc, "Testing Acc. with RFC": testing_accuracies_rfc},
               headers=["Feature Method","Training Acc. with Linear SVC", "Testing Acc. with Linear SVC", 
                        "Training Acc. with Polynomial SVC", "Testing Acc. with Polynomial SVC",
                        "Training Acc. with RFC", "Testing Acc. with RFC"], tablefmt='fancy_grid'))
#%% Detection with CNN

def define_model():
    model = Sequential()
    model.add(Conv2D(filters = 16, kernel_size = (3,3), activation ='relu', input_shape = (128,128,1)))
    model.add(BatchNormalization())
    model.add(MaxPool2D(pool_size=(2,2)))
    
    model.add(Conv2D(filters = 32, kernel_size = (3,3), activation ='relu'))
    model.add(BatchNormalization())
    model.add(MaxPool2D(pool_size=(2,2)))
    model.add(Dropout(0.2))    
    
    model.add(Conv2D(filters = 64, kernel_size = (3,3), activation ='relu'))
    model.add(Conv2D(filters = 64, kernel_size = (3,3), activation ='relu'))
    model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))
    model.add(Flatten())
    model.add(Dense(256, activation = "relu"))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    model.add(Dense(2, activation = "softmax"))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

print("\n*****Human Detection with CNN*****")
df = []
label = []
for img in pedestrian_imgs:
    resized_img = resize(img, (128, 128)) 
    df.append(resized_img)
    label.append(1)

for img in notpedestrian_imgs:
    resized_img = resize(img, (128, 128)) 
    df.append(resized_img)
    label.append(0)

X = np.array(df)
X = X.reshape(-1, 128,128,1)   
y = np.array(label)
print("Total data shape:",X.shape)
print("Labels shape:",y.shape)
print("Number of positive labels {}, negative labels {}, positive/total ratio is {}".format(y.sum(), len(y)-y.sum(), round(y.sum()/len(y), 3)))

y = to_categorical(y, num_classes = 2) 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
temp = np.argmax(y_train,axis = 1) 
class_weights = class_weight.compute_class_weight('balanced', np.unique(temp), temp) #taken from StackOverFlow
class_weight_dict = {0:class_weights[0], 1:class_weights[1]}

print("Train Data Shape:", X_train.shape)
print("Test Data Shape:", X_test.shape)
model = define_model()
print(model.summary())
history = model.fit(X_train, y_train, batch_size=128, epochs=10, verbose=1, validation_split=0.2, class_weight=class_weight_dict)
score = model.evaluate(X_test, y_test, verbose=0)
print("Test Accuracy: ", score[1])
plt.plot(history.history['accuracy'], label="Training Accuracy")
plt.plot(history.history['val_accuracy'], label="Validation Accuracy")
plt.title("Accuracy Change over Epochs")
plt.xlabel("# of Epochs")
plt.ylabel("Accuracy Value")
plt.legend()
plt.show()
plt.plot(history.history['loss'], label="Training Loss")
plt.plot(history.history['val_loss'], label="Validation Loss")
plt.title("Loss Change over Epochs")
plt.xlabel("# of Epochs")
plt.ylabel("Loss Value")
plt.legend()
plt.show()

ypred = model.predict(X_test)
ypred = np.argmax(ypred,axis = 1) 
y_test =  np.argmax(y_test,axis = 1) 
print(classification_report(y_test, ypred))

