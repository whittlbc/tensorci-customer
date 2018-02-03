import os
from time import sleep
from definitions import model_path, train_steps, test_steps
from utils import compute_train_loss, compute_test_loss
from tensorci_client.graphs.xy_scatter_plot import XYScatterPlot

# Create TensorCI scatter plot to log real-time loss info to
graph = XYScatterPlot(title='Loss vs. Iterations',
                      x_axis='Iterations',
                      y_axis='Loss')


def train():
  print('Training model...')

  # Create Train data series for the scatter plot
  train_series = graph.series(name='Train Series', color='#ff7277')

  for i in range(train_steps):
    print('Iter {}/{}'.format(i + 1, train_steps))

    # Find training loss
    loss = compute_train_loss(i)

    # Add this loss to our graph
    train_series.add_data_point(x=(i + 1), y=loss)

    sleep(1)

  print('Training complete.')

  # Save the trained model
  save_model()


def test():
  print('Testing model accuracy...')

  # Create Test data series for the scatter plot
  test_series = graph.series(name='Test Series', color='#35ACC4')

  for i in range(test_steps):
    print('Iter {}/{}'.format(i + 1, test_steps))

    # Find test loss
    loss = compute_test_loss(i)

    # Add this loss to our graph
    test_series.add_data_point(x=(i + 1), y=loss)

    sleep(1)

  print('Testing complete.')


def predict(data):
  return 'i-love-TensorCI'


def save_model():
  print('Writing model file...')
  sleep(1)

  # Training will produce the model file
  with open(model_path, 'w+') as f:
    f.write('I love TensorCI!')

  print('Uploading trained model...')
  sleep(1)


def reload():
  print('Reloading model...')
