from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import tensorflow as tf

from tensorflow.keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras.applications import mobilenet_v2
from tensorflow import keras

import os
import numpy as np
from .models import Result

model_graph = tf.compat.v1.Graph()
with model_graph.as_default():
    tf_session = tf.compat.v1.Session()
    with tf_session.as_default():
        model = mobilenet_v2.MobileNetV2(weights='imagenet')


class DetectionPage(View):

    def get(self, request, *args, **kwargs):
        response = {'file_url': '#'}
        return render(request, 'image_classification/home.html', response)

    def post(self, request, *args, **kwargs):
        upload = request.FILES['data']
        response = {}
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        
        original = keras.preprocessing.image.load_img(os.path.join(settings.MEDIA_ROOT, file), target_size=(224, 224), color_mode='rgb')
        numpy_img = keras.preprocessing.image.img_to_array(original)
        image_batch = np.expand_dims(numpy_img, axis=0)
        processed_image = mobilenet_v2.preprocess_input(image_batch.copy())

        with model_graph.as_default():
            with tf_session.as_default():
                predictions = model.predict(processed_image)

        label = decode_predictions(predictions, top=1)
        # label = np.argmax(predictions)
        label = label[0][0]

        response['file_url'] = file_url
        response['predictions'] = label[1]
        response['probability'] = "{0:.2f}%".format(float(label[2])*100)
        Result.objects.create(path=file_url, prediction=label[1])

        return render(request, "image_classification/home.html", response)
