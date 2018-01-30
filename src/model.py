from definitions import model_path
from time import sleep


def train():
  print('Training...')

  for i in range(25):
    print('Epoch {}...'.format(i))
    i += 1
    sleep(1)

  print('Done training.')

  # Training will produce the model file
  with open(model_path, 'w+') as f:
    f.write('I love TensorCI!')

  print('Writing model file...')
  sleep(1)
  


def test():
  print('Testing...')


def predict(data):
  return 'i-love-TensorCI'


def reload():
  print('Reloading model...')