(function() {
    var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
    po.src = '//apis.google.com/js/plusone.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
})();


(function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/zh_TW/all.js#xfbml=1&appId=427606900621352";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));


var change_background_image = function () {
    var d = new Date();
    var number = d.getDay() + 1;
    //var number = d.getSeconds() % 7 + 1;
    var $body = $('body');
    var ori_image = $body.css('background-image');
    var l = window.location;
    var new_image = 'url('+l.protocol+'//'+l.host+'/blog/_static/'+number+'.JPG)';
    if (ori_image != new_image) {
        $('body').css('background-image', new_image);
    }
    setTimeout('change_background_image()', 6000);
}
$(document).ready(function(){
    change_background_image();
    $('.figure img').each(function(){
        var src = $(this).attr('src');
        var $p = $(this).next();
        if ($p.hasClass('caption')){
            var title = $p.text();
        } else {
            var title = 'No title';
        }
        $(this).wrap($('<a>').attr('target', '_blank').attr('title', title).attr('href', src));
        //.attr('rel', 'superbox[gallery][my_gallery]'));
    });
//        $.superbox.settings = {
//            boxId: "superbox", // Id attribute of the "superbox" element
//            boxClasses: "", // Class of the "superbox" element
//            overlayOpacity: .6, // Background opaqueness
//            loadTxt: "Loading...", // Loading text
//            closeTxt: "Close", // "Close" button text
//            prevTxt: " <- ", // "Previous" button text
//            nextTxt: " -> " // "Next" button text
//        };
//        $.superbox();
});