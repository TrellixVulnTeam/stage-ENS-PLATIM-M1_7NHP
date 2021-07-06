# from yapic.session import Session
import yapicy
from yapic.session import Session


img_path = 'test_frames/train/*.tif'
results_path = 'results_yapic/'

t = yapic.session.Session()
t.load_prediction_data(img_path, results_path)
t.load_model('my_model.h5')

t.predict()