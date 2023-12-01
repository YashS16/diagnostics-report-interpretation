from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf


app = FastAPI()
endpoint = "http://localhost:8501/v1/models/pueumonia_model:predict"
MODEL = tf.keras.models.load_model('/home/rahimdadfaisalsafi/code/YashS16/diagnostics-report-interpretation/models/1')
CLASS_NAMES = ['NORMAL', 'PNEUMONIA']
@app.get('/ping')
def ping():
    # load a machine learning model
    # model.predict
    return {"ok": True}

def read_file_as_image(data) -> np.ndarray:

    image = np.array(Image.open(BytesIO(data)).resize((244, 244)))
    return image

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)

    ):
     image = read_file_as_image(await file.read())
     img_batch = np.expand_dims(image, 0)
     my_img = np.stack((img_batch,) * 3, axis=-1)
     prediction = MODEL.predict(my_img)

     prediction_class = CLASS_NAMES[np.argmax(prediction[0])]
     confidence = np.max(prediction[0])
     return {
         'Class': prediction_class,
         'Confidence': float(confidence)
     }


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
