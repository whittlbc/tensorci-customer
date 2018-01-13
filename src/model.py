from definitions import model_path


def train():
  print('Training...')

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