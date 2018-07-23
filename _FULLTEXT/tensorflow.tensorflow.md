| Documentation | |-----------------| | | TensorFlow is an open source software library for numerical computation using data flow graphs. The graph nodes represent mathematical operations, while the graph edges represent the multidimensional data arrays (tensors) that flow between them. This flexible architecture enables you to deploy computation to one or more CPUs or GPUs in a desktop, server, or mobile device without rewriting code. TensorFlow also includes TensorBoard, a data visualization toolkit. TensorFlow was originally developed by researchers and engineers working on the Google Brain team within Googles Machine Intelligence Research organization for the purposes of conducting machine learning and deep neural networks research. The system is general enough to be applicable in a wide variety of other domains, as well. Keep up to date with release announcements and security updates by subscribing to announce@tensorflow.org. Installation See Installing TensorFlow for instructions on how to install our release binaries or how to build from source. People who are a little more adventurous can also try our nightly binaries: Nightly pip packages * We are pleased to announce that TensorFlow now offers nightly pip packages under the tf-nightly and tf-nightly-gpu project on pypi. Simply run pip install tf-nightly or pip install tf-nightly-gpu in a clean environment to install the nightly TensorFlow build. We support CPU and GPU packages on Linux, Mac, and Windows. Try your first TensorFlow program shell $ python ```python import tensorflow as tf hello = tf.constant(Hello, TensorFlow!) sess = tf.Session() sess.run(hello) Hello, TensorFlow! a = tf.constant(10) b = tf.constant(32) sess.run(a + b) 42 sess.close() ``` Learn more examples about how to do specific tasks in TensorFlow at the tutorials page of tensorflow.org. Contribution guidelines If you want to contribute to TensorFlow, be sure to review the contribution guidelines. This project adheres to TensorFlows code of conduct. By participating, you are expected to uphold this code. We use GitHub issues for tracking requests and bugs. So please see TensorFlow Discuss for general questions and discussion, and please direct specific questions to Stack Overflow. The TensorFlow project strives to abide by generally accepted best practices in open-source software development: Continuous build status Official Builds | Build Type | Status | Artifacts | | --- | --- | --- | | Linux CPU | | pypi | | Linux GPU | | pypi | | Linux XLA | TBA | TBA | | MacOS | | pypi | | Windows CPU | | pypi | | Windows GPU | | pypi | | Android | | demo APK, native libs build history | Community Supported Builds | Build Type | Status | Artifacts | | --- | --- | --- | | IBM s390x | | TBA | | IBM ppc64le CPU | | TBA | | IBM ppc64le GPU | | TBA | | Linux CPU with Intel® MKL-DNN® | | TBA | For more information TensorFlow Website TensorFlow White Papers TensorFlow YouTube Channel TensorFlow Model Zoo TensorFlow MOOC on Udacity TensorFlow Course at Stanford Learn more about the TensorFlow community at the community page of tensorflow.org for a few ways to participate. License Apache License 2.0