from definitions import model_path
from time import sleep


def train():
  print('Training...')

  for i in range(20):
    print('Epoch {}...'.format(i))
    i += 1
    sleep(1)

  print('Writing model file...')
  # Training will produce the model file
  with open(model_path, 'w+') as f:
    f.write('the good stuff')

  print('Done training.')


def test():
  print('Testing!')


def predict(data):
  return 'my-prediction'


def reload():
  pass