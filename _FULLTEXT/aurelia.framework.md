aurelia-framework This library is part of the Aurelia platform and contains the aurelia framework which brings together all the required core aurelia libraries into a ready-to-go application-building platform. To keep up to date on Aurelia, please visit and subscribe to the official blog and our email list. We also invite you to follow us on twitter. If you have questions look around our Discourse forums, chat in our community on Gitter or use stack overflow. Documentation can be found in our developer hub. If you would like to have deeper insight into our development process, please install the ZenHub Chrome or Firefox Extension and visit any of our repositorys boards. Documentation You can read the documentation for the aurelia framework here. If you would like to help improve this documentation, the source for many of the docs can be found in the doc folder within this repository. Other docs, not related to the general framework, but directed at specific libraries, can be found in the doc folder of those libraries. Platform Support This library can be used in the browser only. Building The Code To build the code, follow these steps. Ensure that NodeJS is installed. This provides the platform on which the build tooling runs. From the project folder, execute the following command: shell npm install 3. Ensure that Gulp is installed. If you need to install it, use the following command: shell npm install -g gulp 4. To build the code, you can now run: shell gulp build 5. You will find the compiled code in the dist folder, available in three module formats: AMD, CommonJS and ES6. See gulpfile.js for other tasks related to generating the docs and linting. Running The Tests To run the unit tests, first ensure that you have followed the steps above in order to install all dependencies and successfully build the library. Once you have done that, proceed with these additional steps: Ensure that the Karma CLI is installed. If you need to install it, use the following command: shell npm install -g karma-cli 2. Ensure that jspm is installed. If you need to install it, use the following command: shell npm install -g jspm 3. Install the client-side dependencies with jspm: shell jspm install You can now run the tests with this command: shell karma start