'use strict';
window.bika = window.bika || { lims: {} };
window.bika['custom']={};
window.jarn.i18n.loadCatalog("bika.custom");
var _s = window.jarn.i18n.MessageFactory("bika.custom");

/**
 * Dictionary of JS objects to be loaded at runtime.
 * The key is the DOM element to look for in the current page. The
 * values are the JS objects to be loaded if a match is found in the
 * page for the specified key. The loader initializes the JS objects
 * following the order of the dictionary.
 */
window.bika.custom.controllers =  {

};

/**
 * Initializes only the js controllers needed for the current view.
 * Initializes the JS objects from the controllers dictionary for which
 * there is at least one match with the dict key. The JS objects are
 * loaded in the same order as defined in the controllers dict.
 */
window.bika.custom.initview = function() {
    var loaded = new Array();
    var controllers = window.bika.custom.controllers;
    for (var key in controllers) {
        if ($(key).length) {
            controllers[key].forEach(function(js) {
                if ($.inArray(js, loaded) < 0) {
                    console.debug('[bika.custom.loader] Loading '+js);
                    try {
                        var obj = new window[js]();
                        obj.load();
                        // Register the object for further access
                        window.bika.custom[js]=obj;
                        loaded.push(js);
                    } catch (e) {
                       // statements to handle any exceptions
                       var msg = '[bika.custom.loader] Unable to load '+js+": "+ e.message +"\n"+e.stack;
                       console.warn(msg);
                       window.bika.lims.error(msg);
                    }
                }
            });
        }
    }
    return loaded.length;
};

window.bika.custom.initialized = false;

/**
 * Initializes all bika.custom js stuff
 */
window.bika.custom.initialize = function() {
    if (bika.lims.initialized == true) {
        return window.bika.custom.initview();
    }
    // We should wait after bika.lims being initialized
    setTimeout(function() {
        return window.bika.custom.initialize();
    }, 500);
};

(function( $ ) {
$(document).ready(function(){

    // Initializes bika.custom
    var length = window.bika.custom.initialize();
    window.bika.custom.initialized = true;

});
}(jQuery));
