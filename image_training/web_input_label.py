# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

MODEL_FILE = "bigmodel.pb"
LABEL_FILE = "retrained_labels.txt"

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from PIL import Image
import requests
from io import BytesIO

from flask import Flask
app = Flask(__name__)

import argparse

import numpy as np
import tensorflow as tf

def load_graph(model_file):
  graph = tf.Graph()
  graph_def = tf.GraphDef()

  with open(model_file, "rb") as f:
    graph_def.ParseFromString(f.read())
  with graph.as_default():
    tf.import_graph_def(graph_def)

  return graph


def read_tensor_from_image_file(file_name,
                                input_height=299,
                                input_width=299,
                                input_mean=0,
                                input_std=255):
  input_name = "file_reader"
  output_name = "normalized"
  
  if file_name.startswith("https://") or file_name.startswith("http://"):
    response = requests.get(file_name)
    img = Image.open(BytesIO(response.content))
    img.save("temp",format=img.format)
    file_reader = tf.read_file("temp", input_name)
    img.close()
  else : file_reader = tf.read_file(file_name, input_name)

  if file_name.endswith(".png"):
    image_reader = tf.image.decode_png(
        file_reader, channels=3, name="png_reader")
  elif file_name.endswith(".gif"):
    image_reader = tf.squeeze(
        tf.image.decode_gif(file_reader, name="gif_reader"))
  elif file_name.endswith(".bmp"):
    image_reader = tf.image.decode_bmp(file_reader, name="bmp_reader")
  else:
    image_reader = tf.image.decode_jpeg(
        file_reader, channels=3, name="jpeg_reader")
  float_caster = tf.cast(image_reader, tf.float32)
  dims_expander = tf.expand_dims(float_caster, 0)
  resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
  normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
  sess = tf.Session()
  result = sess.run(normalized)
  img.close()

  return result


def load_labels(label_file):
  label = []
  proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
  for l in proto_as_ascii_lines:
    label.append(l.rstrip())
  return label

@app.route("/test")
  def testImage():
    arg1 = request.args['img']

    model_file = MODEL_FILE
    label_file = LABEL_FILE
    input_height = 299
    input_width = 299
    input_mean = 0
    input_std = 255
    input_layer = "input"
    output_layer = "InceptionV3/Predictions/Reshape_1"

    # parse arg1 into url
    # file_name = url

    graph = load_graph(model_file)
    t = read_tensor_from_image_file(
      file_name,
      input_height=input_height,
      input_width=input_width,
      input_mean=input_mean,
      input_std=input_std)

    input_name = "import/" + input_layer
    output_name = "import/" + output_layer
    input_operation = graph.get_operation_by_name(input_name)
    output_operation = graph.get_operation_by_name(output_name)

    with tf.Session(graph=graph) as sess:
      results = sess.run(output_operation.outputs[0], {
        input_operation.outputs[0]: t
      })
    results = np.squeeze(results)

    top_k = results.argsort()[-5:][::-1]
    labels = load_labels(label_file)

      
    
if __name__ == "__main__":
  # model_file = MODEL_FILE
  # label_file = LABEL_FILE
  # input_height = 299
  # input_width = 299
  # input_mean = 0
  # input_std = 255
  # input_layer = "input"
  # output_layer = "InceptionV3/Predictions/Reshape_1"

  #Import image url from frontend
  #file_name = <url string>

  # graph = load_graph(model_file)
  # t = read_tensor_from_image_file(
  #     file_name,
  #     input_height=input_height,
  #     input_width=input_width,
  #     input_mean=input_mean,
  #     input_std=input_std)

  # input_name = "import/" + input_layer
  # output_name = "import/" + output_layer
  # input_operation = graph.get_operation_by_name(input_name)
  # output_operation = graph.get_operation_by_name(output_name)

  # with tf.Session(graph=graph) as sess:
  #   results = sess.run(output_operation.outputs[0], {
  #       input_operation.outputs[0]: t
  #   })
  # results = np.squeeze(results)

  # top_k = results.argsort()[-5:][::-1]
  # labels = load_labels(label_file)
  # for i in top_k:
  #   print(labels[i] + results[i])
  app.run()