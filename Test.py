from tensorflow.python.saved_model.loader_impl import load
from FileProcessor import FileProcessor
from ResidualFCNetwork import ResidualFCNetwork
import tensorflow.keras as keras
import tensorflow as tf
from tensorflow.keras.optimizers import Adam

file_processor = FileProcessor()
inputs, outputs = file_processor.read_all_files()

in_num, out_num = file_processor.in_num, file_processor.out_num
forward_network = ResidualFCNetwork(10, 24, 300, in_num, out_num)

forward_network.compile(
    optimizer=Adam(learning_rate=10 ** -3),
    loss=keras.losses.MeanSquaredError(),
    metrics=[keras.metrics.MeanAbsoluteError(), 'accuracy'])

inputs = inputs[25:]
outputs = outputs[25:]

val_inputs = inputs[:25]
val_outputs = outputs[:25]



forward_network.fit(inputs, outputs, batch_size=32, epochs=5000, validation_data=(val_inputs, val_outputs))

# forward_network.save('forward_network.pth')
print(outputs[2:3])
print(forward_network.predict(inputs[2:3]))

forward_network.save_weights('forward_network4.pth')
