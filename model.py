import cv2
from pycoral.utils.dataset import read_label_file
from pycoral.utils.edgetpu import make_interpreter
from pycoral.adapters import common
from pycoral.adapters import classify


MODEL_FILE_PATH = "model_files/model_edgetpu.tflite"
LABELS_FILE_PATH = "model_files/labels.txt"


class Model:

    def __init__(self):
        self.interpreter = make_interpreter(MODEL_FILE_PATH)
        self.interpreter.allocate_tensors()
        self.labels = read_label_file(LABELS_FILE_PATH)

    def assess(self, image):
        size = common.input_size(self.interpreter)
        common.set_input(self.interpreter, cv2.resize(image, size, fx=0, fy=0, interpolation=cv2.INTER_CUBIC))
        self.interpreter.invoke()
        results = classify.get_classes(self.interpreter)

        # Print prediction and confidence score
        print(f'Label: {self.labels[results[0].id]}, Score: {results[0].score}')
        # Check the confidence score of the model's decision. If >= 90%, return prediction. Otherwise, return none.
        if results[0].score >= 0.9:
            result = self.labels[results[0].id]
        else:
            result = "none"

        return result