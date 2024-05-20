from django.conf import settings
from PIL import Image
import os
import numpy as np
from tensorflow.keras.models import load_model


model_path = os.path.join(settings.BASE_DIR, 'models/My_last_model.h5')
model = load_model(model_path)

cat=['ain','al','aleff','bb','dal','dha','dhad','fa','gaaf','ghain','ha','haa','jeem','kaaf','khaa','la','laam','meem','nun','ra','saad',
        'seen','sheen','ta','taa','thaa','thal','toot','waw','ya','yaa','zay']

kaggle_to_arabic={'ain':'ع','aleff':"أ",'bb':"ب",'dhad':"ض",'dal':"د",'fa':"ف",'jeem':"ج",'ghain':"غ",
        'ha':"ه",'kaaf':"ك","khaa":"خ",'laam':"ل","meem":'م','nun':"ن",'gaaf':"ق",'ra':"ر",
        'saad':"ص",'seen':"س",'sheen':"ش",'ta':"ط",'waw':"و",'thal':"ذ",'dha':"ظ",'haa':"ح",
        'thaa':"ث",'ya':"ئ",'zay':"ز","al":"ال","toot":"ة","yaa":"يا","taa":"ت","haa":"ح","la":"لا"}

def classify_image(image_path):
    # Load the pre-trained model

    # Load and convert the RGB image to grayscale
    rgb_image = Image.open(image_path)

    # Resize the grayscale image to the model's input size (e.g., 64x64)
    rgb_resized_image = rgb_image.resize((64, 64)).convert('RGB')

    # Convert the grayscale image to a numpy array
    rgb_image_array = np.array(rgb_resized_image)

    # Normalize the pixel values to match the model's preprocessing
    rgb_image_array = rgb_image_array / 255.0  # Assuming pixel values are in the range [0, 255]

    # Expand the dimensions to match the input shape expected by the model
    input_image = np.expand_dims(rgb_image_array, axis=0)

    # Make the prediction
    prediction = model.predict(input_image)

    # Decode the prediction into a class label (assuming one-hot encoding)
    class_label = np.argmax(prediction)
    
    predicted_arabic=cat[class_label]

    return kaggle_to_arabic[predicted_arabic]

    



