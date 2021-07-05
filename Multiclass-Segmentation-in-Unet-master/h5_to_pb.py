
# from keras.models import load_model
# import tensorflow as tf
# import os 
# import os.path as osp
# from keras import backend as K
# #path parameter
# input_path = ''
# weight_file = 'model_1.h5'
# weight_file_path = osp.join(input_path,weight_file)
# output_graph_name = weight_file[:-3] + '.pb'
#  # function
# def h5_to_pb(h5_model,output_dir,model_name,out_prefix = "output_",log_tensorboard = True):
#     if osp.exists(output_dir) == False:
#         os.mkdir(output_dir)
#     out_nodes = []
#     for i in range(len(h5_model.outputs)):
#         out_nodes.append(out_prefix + str(i + 1))
#         tf.identity(h5_model.output[i],out_prefix + str(i + 1))
#     sess = K.get_session()
#     from tensorflow.python.framework import graph_util,graph_io
#     init_graph = sess.graph.as_graph_def()
#     main_graph = graph_util.convert_variables_to_constants(sess,init_graph,out_nodes)
#     graph_io.write_graph(main_graph,output_dir,name = model_name,as_text = False)
#     if log_tensorboard:
#         from tensorflow.python.tools import import_pb_to_tensorboard
#         import_pb_to_tensorboard.import_to_tensorboard(osp.join(output_dir,model_name),output_dir)
#  #output path
# output_dir = osp.join(os.getcwd(),"trans_model")
#  #Load model
# h5_model = load_model(weight_file_path)
# h5_to_pb(h5_model,output_dir = output_dir,model_name = output_graph_name)
# print('model saved')

import tensorflow as tf
from tensorflow.python.framework.convert_to_constants import convert_variables_to_constants_v2
 
def convert_h5to_pb():
    model = tf.keras.models.load_model("model.h5",compile=False)
    model.summary()
    full_model = tf.function(lambda Input: model(Input))
    full_model = full_model.get_concrete_function(tf.TensorSpec(model.inputs[0].shape, model.inputs[0].dtype))
 
    # Get frozen ConcreteFunction
    frozen_func = convert_variables_to_constants_v2(full_model)
    frozen_func.graph.as_graph_def()
 
    layers = [op.name for op in frozen_func.graph.get_operations()]
    print("-" * 50)
    print("Frozen model layers: ")
    for layer in layers:
        print(layer)
 
    print("-" * 50)
    print("Frozen model inputs: ")
    print(frozen_func.inputs)
    print("Frozen model outputs: ")
    print(frozen_func.outputs)
 
    # Save frozen graph from frozen ConcreteFunction to hard drive
    tf.io.write_graph(graph_or_graph_def=frozen_func.graph,
                      logdir="~/model",
                      name="mnist.pb",
                      as_text=False)
  
convert_h5to_pb()
