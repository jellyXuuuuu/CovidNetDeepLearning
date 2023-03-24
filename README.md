# CovidNetDeepLearning
Deep learning explaination for covid 19 model using CovidNet and Grad-cam.

## Brief Summary
Created a series of experiments and tested ipynb file in order to find a way to explain the covid net model visually, and finally used IOU and robust value to get the result of the explanation of the covid-net model numerically.

- 1covid19model_ex_gradcam.ipynb

In this file, I test for the grad-cam XAL tool successfully to produce some explanation;

I also tried other XAL tools RISE here;

Tested grad-cam in different covid-net models(CXR-2, CXR-3, CXR-large);

Tested grad-cam with the different final layers.

- 2grad_cam_covid19.ipynb

Make the progress done within 1covid19model_ex_gradcam.ipynb file into a method, tooling them;

Use the tooled method to test four different images and compare the results;

Test the whole method through a loop to test more images.

- 3_recognize_lung&gradcam.ipynb

Testing and evaluating the result cam images got from grad-cam explanation;

Showing the plot of the cam;

Continue with the loop created in 2grad_cam_covid19.ipynb file;

Manually recognized the area of the lung of a certain CXR image and threshold it with the lung part being black and the other part being white;

Changing the cam result into black and white style by checking the red color on it;

Compare the lung area and cam result using plot img.

- 4_experiment_lung_rectangle.ipynb

Show a lung rectangle to capture the lung area using a rectangle;

Show bounding box of cam result automatically;

Calculate the IOU based on the cam result bounding box and lung rectangle bounding box;

Recognize grad-cam area automatically and re-rectangle it;

Put the whole process together to calculate the IOU of one explanation roughly within one step.

- 5_experiement_whole_method.ipynb

Continued with the whole method process and create a method to use it easily, tooled it;

Changed a little bit of the bounding box value for the lung and get a rough IOU result here for the view.

- 6_update_lung_recognize.ipynb

Using the method created in 5_experiement_whole_method.ipynb file and test the images in a loop;

Looped 10 images and save the results (cam and IOU) into my google drive.

- 7_robust.ipynb

Did the robust test for the cam result, and get to the conclusion that after changing the part of the grad-cam explanation part(by removing the bonding box area), the result changed(initially the result was covid-19 but changed into pneumonia).


## Other information
Besides, all files need to wget the dataset on https://github.com/ieee8023/covid-chestxray-dataset/archive/refs/heads/master.zip, which is my testing dataset;

To run the files, need to mount them to my google drive since the model (CXR-large) and the testing image(./assets/ex-covid.jpeg) I used are stored here, which initially gets the result on https://github.com/lindawangg/COVID-Net;

Models are got from https://github.com/lindawangg/COVID-Net/blob/master/docs/models.md;

Grad-cam-related work is based on https://github.com/cydonia999/Grad-CAM-in-TensorFlow/blob/master/grad-cam-tf.py.

