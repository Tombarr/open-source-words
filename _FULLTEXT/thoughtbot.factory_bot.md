factory_bot factory_bot is a fixtures replacement with a straightforward definition syntax, support for multiple build strategies (saved instances, unsaved instances, attribute hashes, and stubbed objects), and support for multiple factories for the same class (user, admin_user, and so on), including factory inheritance. If you want to use factory_bot with Rails, see factory_bot_rails. Interested in the history of the project name? Transitioning from factory_girl? Check out the guide. Documentation You should find the documentation for your version of factory_bot on Rubygems. See GETTING_STARTED for information on defining and using factories. We also have a detailed introductory video, available for free on Upcase. Install Add the following line to Gemfile: ruby gem factory_bot and run bundle install from your shell. To install the gem manually from your shell, run: shell gem install factory_bot Caveat: As of ActiveSupport 5.0 and above, Ruby 2.2.2+ is required. Because of Rubygems dependency resolution when installing gems, you may see an error similar to: $ gem install factory_bot ERROR: Error installing factory_bot: activesupport requires Ruby version >= 2.2.2. To bypass this, install a pre-5.0 version of ActiveSupport before installing manually. Supported Ruby versions The factory_bot 3.x+ series supports MRI Ruby 1.9. Additionally, factory_bot 3.6+ supports JRuby 1.6.7.2+ while running in 1.9 mode. See GETTING_STARTED for more information on configuring the JRuby environment. For versions of Ruby prior to 1.9, please use factory_bot 2.x. More Information Rubygems Stack Overflow Issues GIANT ROBOTS SMASHING INTO OTHER GIANT ROBOTS You may also find useful information under the factory_girl tag on Stack Overflow. Contributing Please see CONTRIBUTING.md. factory_bot was originally written by Joe Ferris and is now maintained by Josh Clayton. Many improvements and bugfixes were contributed by the open source community. License factory_bot is Copyright © 2008-2016 Joe Ferris and thoughtbot. It is free software, and may be redistributed under the terms specified in the LICENSE file. About thoughtbot factory_bot is maintained and funded by thoughtbot, inc. The names and logos for thoughtbot are trademarks of thoughtbot, inc. We love open source software! See our other projects or hire us to design, develop, and grow your product.