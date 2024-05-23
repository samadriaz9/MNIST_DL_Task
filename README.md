# Deep Learning Task 02
• Custom MNIST dataset
• Train model on Custom dataset and MNIST dataset
• Cross Validation
# Custom Dataset:
For this task a Dataset has been Collection on a High-Resolution Camera. Each digit is handwritten on
a plane A4 page. A python script is attached which take images automatically after 0.2 secs. A balanced
dataset is created which has about 350 images in each class from 0 to 9.
# Model Training:
A simple deep learning model is created containing 2 convolution layers and 2 dense layers with
trainable parameters of 225034 and trained for 20 epochs on both the custom and MNIST dataset.
# Cross Validation:
The model looks well generalized on the MNIST dataset because it is a large dataset while it showed little
over fitness on the custom dataset.
On the other hand, cross validation on the MNIST dataset the model showed very poor performance, due
to the DATA DRIFT. I mean the distribution of the MNIST dataset is much different from the custom
dataset created.
