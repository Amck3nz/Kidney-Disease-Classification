import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load model
        model = load_model(os.path.join("trained_model", "model.h5"))

      
        image_name = self.filename                                              # Recieve image user gives
        test_image = image.load_img(image_name, target_size = (224,224))        # Load image
        test_image = image.img_to_array(test_image)                             # Convert image to numpy array
        test_image = np.expand_dims(test_image, axis=0)                         # Expand dims to 4D (to add batch dimension)
        result = np.argmax(model.predict(test_image), axis=1)                   # Get prediction (soft max of output)
        print(result)

        if result[0] ==1:
            prediction = "Tumor"
            return [{"image" : prediction}]
    
        else:
            prediction = "Normal"
            return [{"image" : prediction}]
        
