$(function () {

    /**
     * Some examples of how to use features.
     *
     **/

    var roomName = roomname;

    var chatSocket = new WebSocket(
        'ws://' + window.location.host +
        '/ws/chatting/' + roomName + '/');


    var sUserAgent = navigator.userAgent.toLowerCase();
    var bIsIpad = sUserAgent.match(/ipad/i) == "ipad";//判断是否为iPad
    var bIsIphoneOs = sUserAgent.match(/iphone os/i) == "iphone os";//判断是否为iPhone用户
    var bIsMidp = sUserAgent.match(/midp/i) == "midp";
    var bIsUc7 = sUserAgent.match(/rv:1.2.3.4/i) == "rv:1.2.3.4";
    var bIsUc = sUserAgent.match(/ucweb/i) == "ucweb";
    var bIsAndroid = sUserAgent.match(/android/i) == "android";
    var bIsCE = sUserAgent.match(/windows ce/i) == "windows ce";
    var bIsWM = sUserAgent.match(/windows mobile/i) == "windows mobile";

    if (!(bIsIpad || bIsIphoneOs || bIsMidp || bIsUc7 || bIsUc || bIsAndroid || bIsCE || bIsWM)) {
      $(".layout .content .chat .chat-body").getNiceScroll(
          {
              cursorcolor: 'rgba(66, 66, 66, 0.20)',
              cursorwidth: "4px",
              cursorborder: '0px',
              touchbehavior:false,
          }
      )
    }else{
$(".layout .content .chat .chat-body").getNiceScroll(
          {
              cursorcolor: 'rgba(66, 66, 66, 0.20)',
              cursorwidth: "4px",
              cursorborder: '0px',
              touchbehavior:true,
          }
      )
}

    var ChatosExamle = {
        Message: {
            add: function (name,message, type,time) {
                var chat_body = $('.layout .content .chat .chat-body ');
                name = name ? name : 'unknow';
                type = type ? type : '';
                message = message ? message : '';

                $('.layout .content .chat .chat-body .messages').append('<div class="message-item ' + type + '"><small class="text-muted"><i>' + name + '</i></small><div class="message-content">' + message + '</div><div class="message-action">' + time + ' ' + (type ? '<i class="ti-check"></i>' : '') + '</div></div>');


                chat_body.scrollTop(chat_body.get(0).scrollHeight, -1);
                $(".layout .content .chat .chat-body").getNiceScroll().resize();
            }}};
    var Userlist = {
        Online:{
            add: function (user) {
                $('#userlist').append('<li class="list-group-item"><div class="users-list-body"><h5>'+ user +'</h5></div></li>');

            }
        }
    };


    $(document).on('submit', '.layout .content .chat .chat-footer form', function (e) {
        e.preventDefault();

        var input = $(this).find('input[type=text]');
        var message = input.val();
        var name = user ;
        var time =get_time();

        message = $.trim(message);

        if (message) {
            ChatosExamle.Message.add(name,message, 'outgoing-message',time);

            input.val('');
        } else {
            input.focus();
        }
        chatSocket.send(JSON.stringify({
            'message': message,
            'name': name,
            'time':time,
            'm_type' : 'c_message',
            'userlist' : 'blank',

        }));
    });


    chatSocket.onmessage = function(e) {
        var data = JSON.parse(e.data);
        var message = data['message'];
        var name = data['name'];
        var time = data['time'];
        var type = data['m_type'];
        if(user != name){

            ChatosExamle.Message.add(name,message, '',time);
            }
        if( type == 's_message'){
            var userlist = data['userlist'][roomName];
            $('#userlist').empty();
            $('#onlineNUM').text('当前在线人数：'+ userlist.length+'人');
            userlist.forEach(function (a) {

                Userlist.Online.add(a);
            });

        }


    };



    $(document).on('click', '.layout .content .sidebar-group .sidebar .list-group-item', function () {
        if (jQuery.browser.mobile) {
            $(this).closest('.sidebar-group').removeClass('mobile-open');
        }
    });

    function get_time() {
        var time = new Date();
        return time.getHours()+'时'+time.getMinutes()+'分'+time.getSeconds()+'秒'
    }


    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };
});