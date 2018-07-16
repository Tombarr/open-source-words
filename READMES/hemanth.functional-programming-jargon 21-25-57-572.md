functional programming jargon functional programming fp provides many advantages and its popularity has been increasing as a result however each programming paradigm comes with its own unique jargon and fp is no exception by providing a glossary we hope to make learning fp easier examples are presented in javascript es2015 why javascript this is a wip please feel free to send a pr where applicable this document uses terms defined in the fantasy land spec translations portuguese spanish chinese bahasa indonesia scala world korean table of contents rm noparent notop arity higher order functions hof closure partial application currying auto currying function composition continuation purity side effects idempotent point free style predicate contracts category value constant functor pointed functor lift referential transparency equational reasoning lambda lambda calculus lazy evaluation monoid monad comonad applicative functor morphism endomorphism isomorphism setoid semigroup foldable lens type signatures algebraic data type sum type product type option functional programming libraries in javascript rm arity the number of arguments a function takes from words like unary binary ternary etc this word has the distinction of being composed of two suffixes ary and ity addition for example takes two arguments and so it is defined as a binary function or a function with an arity of two such a function may sometimes be called dyadic by people who prefer greek roots to latin likewise a function that takes a variable number of arguments is called variadic whereas a binary function must be given two and only two arguments currying and partial application notwithstanding see below js const sum a b a b const arity sum length console log arity 2 the arity of sum is 2 higher order functions hof a function which takes a function as an argument and or returns a function js const filter predicate xs xs filter predicate js const is type x object x instanceof type js filter is number 0 1 2 null 0 2 closure a closure is a scope which retains variables available to a function when its created this is important for partial application to work js const addto x return y return x y we can call addto with a number and get back a function with a baked in x js var addtofive addto 5 in this case the x is retained in addtofives closure with the value 5 we can then call addtofive with the y and get back the desired number addtofive 3 8 this works because variables that are in parent scopes are not garbage collected as long as the function itself is retained closures are commonly used in event handlers so that they still have access to variables defined in their parents when they are eventually called further reading lambda vs closure how do javascript closures work partial application partially applying a function means creating a new function by pre filling some of the arguments to the original function js helper to create partially applied functions takes a function and some arguments const partial f args returns a function that takes the rest of the arguments moreargs and calls the original function with all of them f args moreargs something to apply const add3 a b c a b c partially applying 2 and 3 to add3 gives you a one argument function const fiveplus partial add3 2 3 c 2 3 c fiveplus 4 9 you can also use function prototype bind to partially apply a function in js js const add1more add3 bind null 2 3 c 2 3 c partial application helps create simpler functions from more complex ones by baking in data when you have it curried functions are automatically partially applied currying the process of converting a function that takes multiple arguments into a function that takes them one at a time each time the function is called it only accepts one argument and returns a function that takes one argument until all arguments are passed js const sum a b a b const curriedsum a b a b curriedsum 40 2 42 const add2 curriedsum 2 b 2 b add2 10 12 auto currying transforming a function that takes multiple arguments into one that if given less than its correct number of arguments returns a function that takes the rest when the function gets the correct number of arguments it is then evaluated lodash ramda have a curry function that works this way js const add x y x y const curriedadd curry add curriedadd 1 2 3 curriedadd 1 y 1 y curriedadd 1 2 3 further reading favoring curry hey underscore youre doing it wrong function composition the act of putting two functions together to form a third function where the output of one function is the input of the other js const compose f g a f g a definition const floorandtostring compose val val tostring math floor usage floorandtostring 121 212121 121 continuation at any given point in a program the part of the code thats yet to be executed is known as a continuation js const printasstring num console log given num const addoneandcontinue num cc const result num 1 cc result addoneandcontinue 2 printasstring given 3 continuations are often seen in asynchronous programming when the program needs to wait to receive data before it can continue the response is often passed off to the rest of the program which is the continuation once its been received js const continueprogramwith data continues program with data readfileasync path to file err response if err handle error return continueprogramwith response purity a function is pure if the return value is only determined by its input values and does not produce side effects js const greet name hi name greet brianne hi brianne as opposed to each of the following js window name brianne const greet hi window name greet hi brianne the above examples output is based on data stored outside of the function js let greeting const greet name greeting hi name greet brianne greeting hi brianne and this one modifies state outside of the function side effects a function or expression is said to have a side effect if apart from returning a value it interacts with reads from or writes to external mutable state js const differenteverytime new date js console log io is a side effect idempotent a function is idempotent if reapplying it to its result does not produce a different result f f x ≍ f x js math abs math abs 10 js sort sort sort 2 1 point free style writing functions where the definition does not explicitly identify the arguments used this style usually requires currying or other higher order functions a k a tacit programming js given const map fn list list map fn const add a b a b then not points free numbers is an explicit argument const incrementall numbers map add 1 numbers points free the list is an implicit argument const incrementall2 map add 1 incrementall identifies and uses the parameter numbers so it is not points free incrementall2 is written just by combining functions and values making no mention of its arguments it is points free points free function definitions look just like normal assignments without function or predicate a predicate is a function that returns true or false for a given value a common use of a predicate is as the callback for array filter js const predicate a a 2 1 2 3 4 filter predicate 3 4 contracts a contract specifies the obligations and guarantees of the behavior from a function or expression at runtime this acts as a set of rules that are expected from the input and output of a function or expression and errors are generally reported whenever a contract is violated js define our contract int int const contract input if typeof input number return true throw new error contract violated expected int int const addone num contract num num 1 addone 2 3 addone some string contract violated expected int int category a category in category theory is a collection of objects and morphisms between them in programming typically types act as the objects and functions as morphisms to be a valid category 3 rules must be met there must be an identity morphism that maps an object to itself where a is an object in some category there must be a function from a a morphisms must compose where a b and c are objects in some category and f is a morphism from a b and g is a morphism from b c g f x must be equivalent to g • f x composition must be associative f • g • h is the same as f • g • h since these rules govern composition at very abstract level category theory is great at uncovering new ways of composing things further reading category theory for programmers value anything that can be assigned to a variable js 5 object freeze name john age 30 the freeze function enforces immutability a a 1 undefined constant a variable that cannot be reassigned once defined js const five 5 const john object freeze name john age 30 constants are referentially transparent that is they can be replaced with the values that they represent without affecting the result with the above two constants the following expression will always return true js john age five name john age 30 age 5 functor an object that implements a map function which while running over each value in the object to produce a new object adheres to two rules preserves identity object map x x ≍ object composable object map compose f g ≍ object map g map f f g are arbitrary functions a common functor in javascript is array since it abides to the two functor rules js 1 2 3 map x x 1 2 3 and js const f x x 1 const g x x 2 1 2 3 map x f g x 3 5 7 1 2 3 map g map f 3 5 7 pointed functor an object with an of function that puts any single value into it es2015 adds array of making arrays a pointed functor js array of 1 1 lift lifting is when you take a value and put it into an object like a functor if you lift a function into an applicative functor then you can make it work on values that are also in that functor some implementations have a function called lift or lifta2 to make it easier to run functions on functors js const lifta2 f a b a map f ap b note itsapand notmap const mult a b a b const liftedmult lifta2 mult this function now works on functors like array liftedmult 1 2 3 3 6 lifta2 a b a b 1 2 3 4 4 5 5 6 lifting a one argument function and applying it does the same thing as map js const increment x x 1 lift increment 2 3 2 map increment 3 referential transparency an expression that can be replaced with its value without changing the behavior of the program is said to be referentially transparent say we have function greet js const greet hello world any invocation of greet can be replaced with hello world hence greet is referentially transparent equational reasoning when an application is composed of expressions and devoid of side effects truths about the system can be derived from the parts lambda an anonymous function that can be treated like a value js function a return a 1 a a 1 lambdas are often passed as arguments to higher order functions js 1 2 map a a 1 2 3 you can assign a lambda to a variable js const add1 a a 1 lambda calculus a branch of mathematics that uses functions to create a universal model of computation lazy evaluation lazy evaluation is a call by need evaluation mechanism that delays the evaluation of an expression until its value is needed in functional languages this allows for structures like infinite lists which would not normally be available in an imperative language where the sequencing of commands is significant js const rand function while 1 2 yield math random js const randiter rand randiter next each execution gives a random value expression is evaluated on need monoid an object with a function that combines that object with another of the same type one simple monoid is the addition of numbers js 1 1 2 in this case number is the object and is the function an identity value must also exist that when combined with a value doesnt change it the identity value for addition is 0 js 1 0 1 its also required that the grouping of operations will not affect the result associativity js 1 2 3 1 2 3 true array concatenation also forms a monoid js 1 2 concat 3 4 1 2 3 4 the identity value is empty array js 1 2 concat 1 2 if identity and compose functions are provided functions themselves form a monoid js const identity a a const compose f g x f g x foo is any function that takes one argument compose foo identity ≍ compose identity foo ≍ foo monad a monad is an object with of and chain functions chain is like map except it un nests the resulting nested object js implementation array prototype chain function f return this reduce acc it acc concat f it usage array of cat dog fish bird chain a a split cat dog fish bird contrast to map array of cat dog fish bird map a a split cat dog fish bird of is also known as return in other functional languages chain is also known as flatmap and bind in other languages comonad an object that has extract and extend functions js const coidentity v val v extract return this val extend f return coidentity f this extract takes a value out of a functor js coidentity 1 extract 1 extend runs a function on the comonad the function should return the same type as the comonad js coidentity 1 extend co co extract 1 coidentity 2 applicative functor an applicative functor is an object with an ap function ap applies a function in the object to a value in another object of the same type js implementation array prototype ap function xs return this reduce acc f acc concat xs map f example usage a a 1 ap 1 2 this is useful if you have two objects and you want to apply a binary function to their contents js arrays that you want to combine const arg1 1 3 const arg2 4 5 combining function must be curried for this to work const add x y x y const partiallyappliedadds add ap arg1 y 1 y y 3 y this gives you an array of functions that you can call ap on to get the result js partiallyappliedadds ap arg2 5 6 7 8 morphism a transformation function endomorphism a function where the input type is the same as the output js uppercase string string const uppercase str str touppercase decrement number number const decrement x x 1 isomorphism a pair of transformations between 2 types of objects that is structural in nature and no data is lost for example 2d coordinates could be stored as an array 2 3 or object x 2 y 3 js providing functions to convert in both directions makes them isomorphic const pairtocoords pair x pair 0 y pair 1 const coordstopair coords coords x coords y coordstopair pairtocoords 1 2 1 2 pairtocoords coordstopair x 1 y 2 x 1 y 2 setoid an object that has an equals function which can be used to compare other objects of the same type make array a setoid js array prototype equals function arr const len this length if len arr length return false for let i 0 i len i if this i arr i return false return true 1 2 equals 1 2 true 1 2 equals 0 false semigroup an object that has a concat function that combines it with another object of the same type js 1 concat 2 1 2 foldable an object that has a reduce function that can transform that object into some other type js const sum list list reduce acc val acc val 0 sum 1 2 3 6 lens a lens is a structure often an object or function that pairs a getter and a non mutating setter for some other data structure js using ramdas lens http ramdajs com docs lens const namelens r lens getter for name property on an object obj obj name setter for name property val obj object assign obj name val having the pair of get and set for a given data structure enables a few key features js const person name gertrude blanch invoke the getter r view namelens person gertrude blanch invoke the setter r set namelens shafi goldwasser person name shafi goldwasser run a function on the value in the structure r over namelens uppercase person name gertrude blanch lenses are also composable this allows easy immutable updates to deeply nested data js this lens focuses on the first item in a non empty array const firstlens r lens get first item in array xs xs 0 non mutating setter for first item in array val xs val xs const people name gertrude blanch name shafi goldwasser despite what you may assume lenses compose left to right r over compose firstlens namelens uppercase people name gertrude blanch name shafi goldwasser other implementations partial lenses tasty syntax sugar and a lot of powerful features nanoscope fluent interface type signatures often functions in javascript will include comments that indicate the types of their arguments and return values theres quite a bit of variance across the community but they often follow the following patterns js functionname firstargtype secondargtype returntype add number number number const add x y x y increment number number const increment x x 1 if a function accepts another function as an argument it is wrapped in parentheses js call a b a b const call f x f x the letters a b c d are used to signify that the argument can be of any type the following version of map takes a function that transforms a value of some type a into another type b an array of values of type a and returns an array of values of type b js map a b a b const map f list list map f further reading ramdas type signatures mostly adequate guide what is hindley milner on stack overflow algebraic data type a composite type made from putting other types together two common classes of algebraic types are sum and product sum type a sum type is the combination of two types together into another one it is called sum because the number of possible values in the result type is the sum of the input types javascript doesnt have types like this but we can use sets to pretend js imagine that rather than sets here we have types that can only have these values const bools new set true false const halftrue new set half true the weaklogic type contains the sum of the values from bools and halftrue const weaklogicvalues new set bools halftrue sum types are sometimes called union types discriminated unions or tagged unions theres a couple libraries in js which help with defining and using union types flow includes union types and typescript has enums to serve the same role product type a product type combines types together in a way youre probably more familiar with js point number number x number y number const point x y x y its called a product because the total possible values of the data structure is the product of the different values many languages have a tuple type which is the simplest formulation of a product type see also set theory option option is a sum type with two cases often called some and none option is useful for composing functions that might not return a value js naive definition const some v val v map f return some f this val chain f return f this val const none map f return this chain f return this maybeprop string a option a const maybeprop key obj typeof obj key undefined none some obj key use chain to sequence functions that return option sjs getitem cart option cartitem const getitem cart maybeprop item cart getprice item option number const getprice item maybeprop price item getnestedprice cart option a const getnestedprice cart getitem cart chain getprice getnestedprice none getnestedprice item foo 1 none getnestedprice item price 9 99 some 9 99 option is also known as maybe some is sometimes called just none is sometimes called nothing functional programming libraries in javascript mori immutable ramda ramda adjunct folktale monet js lodash underscore js lazy js maryamyriameliamurphies js haskell in es6 sanctuary crocks p s this repo is successful due to the wonderful contributions