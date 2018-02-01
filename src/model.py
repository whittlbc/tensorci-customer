from definitions import model_path
from time import sleep
from tensorci_client.graphs.xy_scatter_plot import XYScatterPlot

graph = XYScatterPlot(title='Loss vs. Iterations',
                      x_axis='Iterations',
                      y_axis='Loss')


def train():
  print('Training...')

  train_series = graph.series(name='Train Series', color='#ff7277')

  for i in range(25):
    print('Iter {}...'.format(i))

    # Get training loss
    loss = 1

    train_series.add_data_point(x=i, y=loss)

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

  test_series = graph.series(name='Test Series', color='#35ACC4')

  for i in range(25):
    print('Iter {}...'.format(i))

    # Get test loss
    loss = 1

    test_series.add_data_point(x=i, y=loss)

    i += 1
    sleep(1)

  print('Done testing.')


def predict(data):
  return 'i-love-TensorCI'


def reload():
  print('Reloading model...')