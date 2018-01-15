from definitions import model_path
from time import sleep


def train():
  print('Training...')

  for i in range(20):
    print('Epoch {}...'.format(i))
    i += 1
    sleep(1)

  print('Writing model file...')

  sleep(1)

  # Training will produce the model file
  with open(model_path, 'w+') as f:
    f.write('I love TensorCI')

  print('Done training.')


def test():
  print('Testing...')


def predict(data):
  return 'my-awesome-prediction'


def reload():
  print('Reloading model...')
  pass