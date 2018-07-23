Apollo Client Apollo Client is a fully-featured caching GraphQL client with integrations for React, Angular, and more. It allows you to easily build UI components that fetch data via GraphQL. To get the most value out of apollo-client, you should use it with one of its view layer integrations. To get started with the React integration, go to our React Apollo documentation website. Apollo Client also has view layer integrations for all the popular frontend frameworks. For the best experience, make sure to use the view integration layer for your frontend framework of choice. Apollo Client can be used in any JavaScript frontend where you want to use data from a GraphQL server. Its: Incrementally adoptable, so that you can drop it into an existing JavaScript app and start using GraphQL for just part of your UI. Universally compatible, so that Apollo works with any build setup, any GraphQL server, and any GraphQL schema. Simple to get started with, so you can start loading data right away and learn about advanced features later. Inspectable and understandable, so that you can have great developer tools to understand exactly what is happening in your app. Built for interactive apps, so your users can make changes and see them reflected in the UI immediately. Small and flexible, so you dont get stuff you dont need. The core is under 25kb compressed. Community driven, because Apollo is driven by the community and serves a variety of use cases. Everything is planned and developed in the open. Get started on the home page, which has great examples for a variety of frameworks. Installation ```bash installing the preset package npm install apollo-boost graphql-tag graphql --save installing each piece independently npm install apollo-client apollo-cache-inmemory apollo-link-http graphql-tag graphql --save ``` To use this client in a web browser or mobile app, youll need a build system capable of loading NPM packages on the client. Some common choices include Browserify, Webpack, and Meteor 1.3+. Install the Apollo Client Developer tools for Chrome for a great GraphQL developer experience! Usage You get started by constructing an instance of the core class [ApolloClient][]. If you load ApolloClient from the [apollo-boost][] package, it will be configured with a few reasonable defaults such as our standard in-memory cache and a link to a GraphQL API at /graphql. ```js import ApolloClient from apollo-boost; const client = new ApolloClient(); ``` To point ApolloClient at a different URL, add your GraphQL APIs URL to the uri config property: ```js import ApolloClient from apollo-boost; const client = new ApolloClient({ uri: https://graphql.example.com }); ``` Most of the time youll hook up your client to a frontend integration. But if youd like to directly execute a query with your client, you may now call the client.query method like this: ```js import gql from graphql-tag; client.query({ query: gqlquery TodoApp { todos { id text completed } }, }) .then(data => console.log(data)) .catch(error => console.error(error)); ``` Now your client will be primed with some data in its cache. You can continue to make queries, or you can get your client instance to perform all sorts of advanced tasks on your GraphQL data. Such as [reactively watching queries with watchQuery][], [changing data on your server with mutate][], or [reading a fragment from your local cache with readFragment][]. To learn more about all of the features available to you through the apollo-client package, be sure to read through the apollo-client API reference. Learn how to use Apollo Client with your favorite framework React Angular Vue Ember Polymer Meteor Blaze Vanilla JS Next.js Contributing Read the Apollo Contributor Guidelines. Running tests locally: ``` nvm use node npm install npm run build npm test ``` This project uses TypeScript for static typing and TSLint for linting. You can get both of these built into your editor with no configuration by opening this project in Visual Studio Code, an open source IDE which is available for free on all platforms. Important discussions If youre getting booted up as a contributor, here are some discussions you should take a look at: Static typing and why we went with TypeScript also covered in the Medium post Idea for pagination handling Discussion about interaction with Redux and domain vs. client state Long conversation about different client options, before this repo existed