Google Test Welcome to Google Test, Googles C++ test framework! This repository is a merger of the formerly separate GoogleTest and GoogleMock projects. These were so closely related that it makes sense to maintain and release them together. Please see the project page above for more information as well as the mailing list for questions, discussions, and development. There is also an IRC channel on OFTC (irc.oftc.net) #gtest available. Please join us! Getting started information for Google Test is available in the Google Test Primer documentation. Google Mock is an extension to Google Test for writing and using C++ mock classes. See the separate Google Mock documentation. More detailed documentation for googletest (including build instructions) are in its interior googletest/README.md file. Features An xUnit test framework. Test discovery. A rich set of assertions. User-defined assertions. Death tests. Fatal and non-fatal failures. Value-parameterized tests. Type-parameterized tests. Various options for running the tests. XML test report generation. Platforms Google test has been used on a variety of platforms: Linux Mac OS X Windows Cygwin MinGW Windows Mobile Symbian Who Is Using Google Test? In addition to many internal projects at Google, Google Test is also used by the following notable projects: The Chromium projects (behind the Chrome browser and Chrome OS). The LLVM compiler. Protocol Buffers, Googles data interchange format. The OpenCV computer vision library. tiny-dnn: header only, dependency-free deep learning framework in C++11. Related Open Source Projects GTest Runner is a Qt5 based automated test-runner and Graphical User Interface with powerful features for Windows and Linux platforms. Google Test UI is test runner that runs your test binary, allows you to track its progress via a progress bar, and displays a list of test failures. Clicking on one shows failure text. Google Test UI is written in C#. GTest TAP Listener is an event listener for Google Test that implements the TAP protocol for test result output. If your test runner understands TAP, you may find it useful. gtest-parallel is a test runner that runs tests from your binary in parallel to provide significant speed-up. Requirements Google Test is designed to have fairly minimal requirements to build and use with your projects, but there are some. Currently, we support Linux, Windows, Mac OS X, and Cygwin. We will also make our best effort to support other platforms (e.g. Solaris, AIX, and z/OS). However, since core members of the Google Test project have no access to these platforms, Google Test may have outstanding issues there. If you notice any problems on your platform, please notify googletestframework@googlegroups.com. Patches for fixing them are even more welcome! Linux Requirements These are the base requirements to build and use Google Test from a source package (as described below): GNU-compatible Make or gmake POSIX-standard shell POSIX(-2) Regular Expressions (regex.h) A C++98-standard-compliant compiler Windows Requirements Microsoft Visual C++ 2015 or newer Cygwin Requirements Cygwin v1.5.25-14 or newer Mac OS X Requirements Mac OS X v10.4 Tiger or newer Xcode Developer Tools Contributing change Please read the CONTRIBUTING.md for details on how to contribute to this project. Happy testing!