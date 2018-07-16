ory is a company building and maintaining developer tools for a safer more accessible web you might also like our other open source projects the ory editor is a smart extensible and modern editor wysiwyg for the web written in react if you are fed up with the limitations of contenteditable you are in the right place the ory editor is used at germanys largest 800k uniques per month e learning website www serlo org to improve the wiki experience we use the ory editor for ory sites a tool for creating websites its similar to squarespace but it works offline the sites you created are stored on your device and you are able to create your own designs and plugins check out the demo at editor ory am please note ory editor is pre release and backwards compatibility is not guaranteed however we try our best to make breaking changes visible and easy to recover from start doctoc generated toc please keep comment here to allow auto update dont edit this section instead re run doctoc to update introduction whats the problem what makes it different ory sites quickstart documentation how to run develop and contribute install dependencies run the example s run the toolchain run the documentation known issues end doctoc generated toc please keep comment here to allow auto update introduction we have been running the wikipedia for learning for almost a decade now the experience and the lessons learned made us embark on the journey to build the ory editor we wanted to make content editing on the web easy and enrich the open source community with technology that moves the needle significantly for how content is created and edited on the web whats the problem we had to realize that existing open source content editing solutions had one of the three flaws the produced markup was horrific a lot of sanitation had to take place and xss is always a threat the author must learn special mark up like markdown before being able to produce content these text based solutions are usually unable to specify a layout and complex data structures like tables are annoying to edit promising libraries potentially solving the above where abandoned by their maintainers because it started as a special use case or a free time project so whats different we concluded that a solution must meet the following principles the state is a normalized json object no html involved it is a visual editor that does not require programming experience or special training it is built by a company reducing the likelihood of abandonment based on reusable react components it gives developers authors and designers new ways of working together and creating better and richer experiences more easily it works on mobile and touch devices with these principles in mind we went out and implemented the ory editor which you are looking at right now ory sites ory sites is an innovative open source static site generator similar to jekyll or hugo content creation is done in your browser with the full extensibility of the ory editor learn more about ory sites quickstart currently our focus is on optimizing the ory editor for usage with react we will work on and ship versions that do not require react in the future please check the reactjs tutorial npm install save ory editor note the ory editor package is a metapackage it includes the core our default ui and some plugins we officially support use this package primarily for convenience documentation check out the user guide on gitbook how to run develop and contribute do you want to run develop or contribute to the ory editor for that you need node installed on your system use git to check out this repository as followed bash git clone https github com ory editor git cd editor install dependencies the ory editor is a monorepo that you initialise with bash npm i run the example s here are some examples that are a good starting point if you want to familiarize yourself with the editor to run the examples use one of the following commands npm run build cd examples npm run start run the toolchain our toolchain contains tests eslint and flow types we highly recommend to run this toolchain while developing bash run the tests in watch mode npm run test watch run eslint in watch mode npm run lint watch run flowtype in watch mode npm run flow watch run the documentation to run the guide in watch mode do bash npm run docs guide to generate api docs run bash npm run docs api known issues we keep track of known issues in the issues tab