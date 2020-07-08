$(function () {

    /**
     * Some examples of how to use features.
     *
     **/

    var ChatosExamle = {
        Message: {
            add: function (name,message, type,time) {
                var chat_body = $('.layout .content .chat .chat-body');
                if (chat_body.length > 0) {
                    name = name ? name: 'unknow';
                    type = type ? type : '';
                    message = message ? message : '';

                    $('.layout .content .chat .chat-body .messages').append('<div class="message-item ' + type + '"><small class="text-muted"><i>'+ name +'</i></small><div class="message-content">' + message + '</div><div class="message-action">'+time+' ' + (type ? '<i class="ti-check"></i>' : '') + '</div></div>');

                    chat_body.scrollTop(chat_body.get(0).scrollHeight, -1).niceScroll({
                        cursorcolor: 'rgba(66, 66, 66, 0.20)',
                        cursorwidth: "4px",
                        cursorborder: '0px'
                    });
                }
            }
        }
    };




    $(document).on('submit', '.layout .content .chat .chat-footer form', function (e) {
        e.preventDefault();

        var input = $(this).find('input[type=text]');
        var message = input.val();
        var name = '我';
        var time =get_time();

        message = $.trim(message);

        if (message) {
            ChatosExamle.Message.add(name,message, 'outgoing-message',time);
            input.val('');
        } else {
            input.focus();
        }
    });

    $(document).on('click', '.layout .content .sidebar-group .sidebar .list-group-item', function () {
        if (jQuery.browser.mobile) {
            $(this).closest('.sidebar-group').removeClass('mobile-open');
        }
    });

    function get_time() {
        var time = new Date();
        return time.getHours()+'时'+time.getMinutes()+'分'+time.getSeconds()+'秒'
    }

});