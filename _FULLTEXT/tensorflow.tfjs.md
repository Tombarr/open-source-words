TensorFlow.js TensorFlow.js is an open-source hardware-accelerated JavaScript library for training and deploying machine learning models. Develop ML in the Browser Use flexible and intuitive APIs to build models from scratch using the low-level JavaScript linear algebra library or the high-level layers API. Run Existing models Use TensorFlow.js model converters to run pre-existing TensorFlow models right in the browser. Retrain Existing models Retrain pre-existing ML models using sensor data connected to the browser, or other client-side data. About this repo This repository contains the logic and scripts that combine two packages: - TensorFlow.js Core, a flexible low-level API, formerly known as deeplearn.js. - TensorFlow.js Layers, a high-level API which implements functionality similar to Keras. If you care about bundle size, you can import those packages individually. Examples Check out our examples repository and our tutorials. Migrating from deeplearn.js See these release notes for how to migrate from deeplearn.js to TensorFlow.js. Getting started There are two main ways to get TensorFlow.js in your JavaScript project: via script tags or by installing it from NPM and using a build tool like Parcel, WebPack, or Rollup. via Script Tag Add the following code to an HTML file: ```html Load TensorFlow.js <!-- Place your code in the script tag below. You can also use an external .js file --> <script> // Notice there is no import statement. tf is available on the index-page // because of the script tag above. // Define a model for linear regression. const model = tf.sequential(); model.add(tf.layers.dense({units: 1, inputShape: [1]})); // Prepare the model for training: Specify the loss and the optimizer. model.compile({loss: meanSquaredError, optimizer: sgd}); // Generate some synthetic data for training. const xs = tf.tensor2d([1, 2, 3, 4], [4, 1]); const ys = tf.tensor2d([1, 3, 5, 7], [4, 1]); // Train the model using the data. model.fit(xs, ys).then(() => { // Use the model to do inference on a data point the model hasnt seen before: // Open the browser devtools to see the output model.predict(tf.tensor2d([5], [1, 1])).print(); }); </script> ``` Open up that html file in your browser and the code should run! via NPM Add TensorFlow.js to your project using yarn or npm. Note: Because we use ES2017 syntax (such as import), this workflow assumes you are using a modern browser or a bundler/transpiler to convert your code to something older browsers understand. See our examples to see how we use Parcel to build our code. However you are free to use any build tool that you prefer. ```js import * as tf from @tensorflow/tfjs; // Define a model for linear regression. const model = tf.sequential(); model.add(tf.layers.dense({units: 1, inputShape: [1]})); // Prepare the model for training: Specify the loss and the optimizer. model.compile({loss: meanSquaredError, optimizer: sgd}); // Generate some synthetic data for training. const xs = tf.tensor2d([1, 2, 3, 4], [4, 1]); const ys = tf.tensor2d([1, 3, 5, 7], [4, 1]); // Train the model using the data. model.fit(xs, ys).then(() => { // Use the model to do inference on a data point the model hasnt seen before: model.predict(tf.tensor2d([5], [1, 1])).print(); }); ``` See our tutorials, examples and documentation for more details. Importing pre-trained models We support porting pre-trained models from: - TensorFlow SavedModel - Keras Find out more TensorFlow.js is a part of the TensorFlow ecosystem. For more info: - js.tensorflow.org - Tutorials - API reference - Help mailing list