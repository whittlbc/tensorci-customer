import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

data_dir = base_dir + '/data'

model_path = data_dir + '/model.ckpt'

train_steps = 25
test_steps = 25