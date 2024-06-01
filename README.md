# Arabic Sign Language Recognition and Generating Arabic Speech Using Convolutional Neural Network and YOLO by changing its backbone 

Sign language is used by 70 million people around the world and there’s a lack in communication between deaf and dump community and our community. Sign language encompasses the movement of the arms and hands as a means of communication for people with hearing disabilities. An automated sign recognition system requires two main courses of action: the detection of particular features and the categorization of particular input data. A vision-based system by applying CNN for the recognition of Arabic hand sign-based letters and translating them into Arabic speech is proposed in this paper. The proposed system will automatically detect hand sign letters and speaks out the result with the Arabic language with a deep learning model. This system gives 97% accuracy to recognize the Arabic hand sign-based letters which assures it as a highly dependable system. After recognizing the Arabic hand sign-based letters, the outcome will be fed to the text into the speech engine which produces the audio of the Arabic language as an output.

### 1.First Dataset For CNN Model
Raw Images. Hand sign images are called raw images that are captured using a camera for implementing the proposed system. The images are taken in the following environment:
i.	From different angles 
ii.	By changing lighting conditions 
iii.	With good quality and in focus 
iv.	By changing object size and distance

 The objective of creating raw images is to create the data set for training and testing. 
Classifying Images. The proposed system classifies the images into 32 categories for 32 letters of the Arabic Alphabet. One subfolder is used for storing images of one category to implement the system. All subfolders which represent classes are kept together in one main folder named “dataset” in the proposed system. 
Formatting Image. Usually, the hand sign images are unequal and having different background. So, it is required to delete the unnecessary element from the images for getting the hand part. The extracted images are resized to 128 × 128 pixels and converted to RGB
![image](https://github.com/YoussifAllam/Speaking-Fingers-graduation-Project-/assets/96921160/303b3783-681b-4727-a0d7-bb4e3cb9f865)

### 2. Second Dataset For YOLO Model
The contribution is a large fully-labelled dataset for Arabic Sign Language (ArSL) which is made publically available and free for all researchers. The dataset which is named RGB Arabic Alphabet Sign Language (ArSL) dataset Image Dataset consists of 21868 images for the 31 Arabic sign language sign and alphabets collected from 40 participants in different age groups. Different dimensions and different variations were present in images which can be cleared using pre-processing techniques to remove noise
Preprocessing steps :  
Auto-Orient: Applied
Resize: Stretch to 640x640
Augmentations : 
Rotation: Between -4° and +4°
Cutout: 3 boxes with 10% size each
Grayscale: Applied .
![image](https://github.com/YoussifAllam/Speaking-Fingers-graduation-Project-/assets/96921160/5ee2923a-f525-4baa-a44a-18c1735fa322)


Results:
1.	CNN 
Results from the Convolutional Neural Network (CNN) model for the Sign Language Recognition project were highly encouraging, achieving an accuracy of 97% on the test dataset. The model was trained on a dataset of 54,049 images with 32 classes representing different sign language gestures. To enhance the model's performance, data augmentation techniques were applied during training
![image](https://github.com/YoussifAllam/Speaking-Fingers-graduation-Project-/assets/96921160/96856243-7c0f-409f-99ca-b07ff170db4f)

Testing Result : 
Accuracy: 0.9715078630897317
Precision: 0.9715078630897317
F1 Score: 0.9715078630897317
Sensitivity: 0.9715078630897317
Specificity: 1.0 

![image](https://github.com/YoussifAllam/Speaking-Fingers-graduation-Project-/assets/96921160/debc8d83-d563-4674-a429-666a53e66ef2)

Confusion Matrix :
The confusion matrix revealed that the model performed well across all 32 classes, with accuracy ranging from 95% to 97.15% for individual classes. The precision and recall scores were calculated for each class, demonstrating an average precision of 0.978 and an average recall of 0.97.
![image](https://github.com/YoussifAllam/Speaking-Fingers-graduation-Project-/assets/96921160/9c02915d-ba81-4cda-9cf9-05f54f6e40af)

### 2.	YOLO 
![image](https://github.com/YoussifAllam/Speaking-Fingers-graduation-Project-/assets/96921160/f205b376-37ca-42ff-ab88-739177a0f88c)


## Mobile APP
![image](https://github.com/YoussifAllam/Speaking-Fingers-graduation-Project-/assets/96921160/653dc3c8-b3fe-4c30-aa42-f36680925225)

![image](https://github.com/YoussifAllam/Speaking-Fingers-graduation-Project-/assets/96921160/489e0ffe-6d59-42e4-8095-24f6e4a67750)

![image](https://github.com/YoussifAllam/Speaking-Fingers-graduation-Project-/assets/96921160/8ca39c41-7d4e-43f9-b119-f4ff91c4be14)
![image](https://github.com/YoussifAllam/Speaking-Fingers-graduation-Project-/assets/96921160/8dce00c4-27aa-4a99-8d2f-909a753c015e)

## WebSite
![image](https://github.com/YoussifAllam/Speaking-Fingers-graduation-Project-/assets/96921160/30c1de4d-553e-4cab-ab58-b6d449144bc4)

![image](https://github.com/YoussifAllam/Speaking-Fingers-graduation-Project-/assets/96921160/e4e9bbcc-7d0e-4a3c-9456-593df174af26)
![image](https://github.com/YoussifAllam/Speaking-Fingers-graduation-Project-/assets/96921160/a5c23220-10ad-4e2a-95f4-6c99c58f6f3c)
![image](https://github.com/YoussifAllam/Speaking-Fingers-graduation-Project-/assets/96921160/676a25e2-680f-4bc6-b38d-d7eeee274258)
![image](https://github.com/YoussifAllam/Speaking-Fingers-graduation-Project-/assets/96921160/ae3e9277-e4ac-43f5-a142-bf5c16d02fff)


