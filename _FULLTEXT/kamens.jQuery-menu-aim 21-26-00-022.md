jquery menu aim menu aim is a jquery plugin for dropdown menus that can differentiate between a user trying hover over a dropdown item vs trying to navigate into a submenus contents try a demo this problem is normally solved using timeouts and delays menu aim tries to solve this by detecting the direction of the users mouse movement this can make for quicker transitions when navigating up and down the menu the experience is hopefully similar to amazon com s shop by department dropdown use like so menu menuaim activate noop fired on row activation deactivate noop fired on row deactivation to receive events when a menus row has been purposefully de activated the following options can be passed to menuaim all functions execute with the relevant rows html element as the execution context this menuaim function to call when a row is purposefully activated use this to show a submenus content for the activated row activate function function to call when a row is deactivated deactivate function function to call when mouse enters a menu row entering a row does not mean the row has been activated as the user may be mousing over to a submenu enter function function to call when mouse exits a menu row exit function function to call when mouse exits the entire menu if this returns true the current rows deactivation event and callback function will be fired otherwise if this isnt supplied or it returns false the currently activated row will stay activated when the mouse leaves the menu entirely exitmenu function selector for identifying which elements in the menu are rows that can trigger the above events defaults to li rowselector li you may have some menu rows that arent submenus and therefore shouldnt ever need to activate if so filter submenu rows w this selector defaults to all elements submenuselector direction the submenu opens relative to the main menu this controls which direction is forgiving as the user moves their cursor from the main menu into the submenu can be one of right left above or below defaults to right submenudirection right menu aim assumes that you are using a menu with submenus that expand to the menus right it will fire events when the users mouse enters a new dropdown item and when that item is being intentionally hovered over want an example to learn from check out example example html it has a working dropdown for you to play with play with the above example full of fun monkey pictures by opening example example html after downloading the repo faq whats the license mit does it support horizontal menus or submenus that open to the left yup check out the submenudirection option above i work at a big company that requires a version number on this third party code before i can use it do you have a version number sure current version 1 1 im not nearly bored enough got anything else read about this plugins creation