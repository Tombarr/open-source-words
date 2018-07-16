better scroll 中文文档 what is better scroll better scroll is a plugin which is aimed at solving scrolling circumstances on the mobile side pc supported already the core is inspired by the implementation of iscroll so the apis of better scroll are compatible with iscroll on the whole whats more better scroll also extends some features and optimizes for performance based on iscroll better scroll is implemented with plain javascript which means its dependency free the size of compiled code is 63 kb 35 kb after compressed and only 9kb after gzip better scroll is a really lightweight javascript lib getting started the best way to learn and use better scroll is by viewing its demo we have put all the code in example directory considering that one of the most suitable javascript mvvm framework for mobile development currently is vue and better scroll can be applied in conjunction with vue very well so i rewrote the demo with vue the most common application scenario of better scroll is list scrolling lets see its html html div class wrapper ul class content li li li li ul you can put some other doms here it wont affect the scrolling div in the code above better scroll is applied to the outer wrapper container and the scrolling part is content element pay attention that better scroll only handles the scroll of the first child element content of the container wrapper which means other elements will be ignored the simplest initialization code is as follow javascript import bscroll from better scroll const wrapper document queryselector wrapper const scroll new bscroll wrapper better scroll provides a class whose first parameter is a plain dom object when instantiated certainly better scroll inside would try to use queryselector to get the dom object so the initiazation code can also be like the following javascript import bscroll from better scroll const scroll new bscroll wrapper the core of scrolling many developers have used better scroll but the most common problem they have met is i have initiated better scroll but the content cant scroll the phenomenon is the content cant scroll and we need to figure out the root cause before that lets take a look at the browsers scrolling principle everyone can see the browsers scroll bar when the height of the page content exceeds the viewport height the vertical scroll bar will appear when the width of page content exceeds the viewport width the horizontal bar will appear that is to say when the viewport cant display all the content the browser would guide the user to scroll the screen with scroll bar to see the rest of content the principle of better scroll is samed as the browser we can feel about this more obviously using a picture the green part is the wrapper also known as the parent container which has fixed height the yellow part is the content which is the first child element of the parent container and whose height would grow with the size of its content then when the height of the content doesnt exceed the height of the parent container the content would not scroll once exceeded the content can be scrolled that is the principle of better scroll using better scroll with mvvm frameworks i wrote an article when better scroll meets vue in chinese i also hope that developers can contribute to share the experience of using better scroll with other frameworks a fantastic mobile ui lib implement by vue cube ui using better scroll in the real project if you want to learn how to use better scroll in the real project，you can learn my two practical courses in chinese 。 high imitating starvation takeout practical course base on vue js project demo address music app advanced practical course base on vue js project demo address document visit better scroll document communication demo visit demo or scan qr code： changelog detailed changes for each release are documented in the release notes