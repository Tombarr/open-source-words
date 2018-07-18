synaptic important synaptic 2 x is in stage of discussion now feel free to participate synaptic is a javascript neural network library for node js and the browser its generalized algorithm is architecture free so you can build and train basically any type of first order or even second order neural network architectures this library includes a few built in architectures like multilayer perceptrons multilayer long short term memory networks lstm liquid state machines or hopfield networks and a trainer capable of training any given network which includes built in training tasks tests like solving an xor completing a distracted sequence recall task or an embedded reber grammar test so you can easily test and compare the performance of different architectures the algorithm implemented by this library has been taken from derek d monners paper a generalized lstm like training algorithm for second order recurrent neural networks there are references to the equations in that paper commented through the source code introduction if you have no prior knowledge about neural networks you should start by reading this guide if you want a practical example on how to feed data to a neural network then take a look at this article you may also want to take a look at this article demos solve an xor discrete sequence recall task learn image filters paint an image self organizing map read from wikipedia creating a simple neural network video the source code of these demos can be found in this branch getting started neurons layers networks trainer architect to try out the examples checkout the gh pages branch git checkout gh pages other languages this readme is also available in other languages chinese simplified 中文文档 thanks to noraincode chinese traditional 繁體中文 by noobtw japanese 日本語 thanks to oshirogo overview installation in node you can install synaptic with npm cmd npm install synaptic save in the browser you can install synaptic with bower cmd bower install synaptic or you can simply use the cdn link kindly provided by cdnjs html script src https cdnjs cloudflare com ajax libs synaptic 1 1 4 synaptic js script usage javascript var synaptic require synaptic this line is not needed in the browser var neuron synaptic neuron layer synaptic layer network synaptic network trainer synaptic trainer architect synaptic architect now you can start to create networks train them or use built in networks from the architect examples perceptron this is how you can create a simple perceptron javascript function perceptron input hidden output create the layers var inputlayer new layer input var hiddenlayer new layer hidden var outputlayer new layer output connect the layers inputlayer project hiddenlayer hiddenlayer project outputlayer set the layers this set input inputlayer hidden hiddenlayer output outputlayer extend the prototype chain perceptron prototype new network perceptron prototype constructor perceptron now you can test your new network by creating a trainer and teaching the perceptron to learn an xor javascript var myperceptron new perceptron 2 3 1 var mytrainer new trainer myperceptron mytrainer xor error 0 004998819355993572 iterations 21871 time 356 myperceptron activate 0 0 0 0268581547421616 myperceptron activate 1 0 0 9829673642853368 myperceptron activate 0 1 0 9831714267395621 myperceptron activate 1 1 0 02128894618097928 long short term memory this is how you can create a simple long short term memory network with input gate forget gate output gate and peephole connections javascript function lstm input blocks output create the layers var inputlayer new layer input var inputgate new layer blocks var forgetgate new layer blocks var memorycell new layer blocks var outputgate new layer blocks var outputlayer new layer output connections from input layer var input inputlayer project memorycell inputlayer project inputgate inputlayer project forgetgate inputlayer project outputgate connections from memory cell var output memorycell project outputlayer self connection var self memorycell project memorycell peepholes memorycell project inputgate memorycell project forgetgate memorycell project outputgate gates inputgate gate input layer gatetype input forgetgate gate self layer gatetype one to one outputgate gate output layer gatetype output input to output direct connection inputlayer project outputlayer set the layers of the neural network this set input inputlayer hidden inputgate forgetgate memorycell outputgate output outputlayer extend the prototype chain lstm prototype new network lstm prototype constructor lstm these are examples for explanatory purposes the architect already includes multilayer perceptrons and multilayer lstm network architectures contribute synaptic is an open source project that started in buenos aires argentina anybody in the world is welcome to contribute to the development of the project if you want to contribute feel free to send prs just make sure to run npm run test and npm run build before submitting it this way youll run all the test specs and build the web distribution files support if you like this project and you want to show your support you can buy me a beer with magic internet money btc 16epaggbbhfm2d6esjmxcubtngqpnlwnek eth 0xa423bfe9db2dc125dd3b56f215e09658491cc556 ltc leeemezj6yl6pkttteghfd6iddxhbf2hxa xmr 46wnbmwxpyxibpkbhjagjc65cyzaxtaabqjcgpazquhbkw2r8ntpqniegmjcwfmczzsbrejtmpstr54mogbdbjti2w1xmgm 3