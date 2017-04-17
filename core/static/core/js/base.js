$(".chosen-select").chosen();


$(document).on('click', 'button.ajaxlike', function (e) {
    var data = $(this).data();
    console.log(data);
    var url = data.url;
    var likesSpan = $('#likes-' + data.postid);
    $.ajax({url: url, method: "POST"}).done(function (data, status, response) {
        likesSpan.html(data);
    });
    return false;
});


$(document).ready(
    function () {

        $(document).on('submit', '.ajaxform', function () {
            $.post(
                $(this).data('url'),
                $(this).serialize(),
                function(data) {
                    if (data == 'OK') {
                        document.location.href = document.location.href;
                    }
                    form.html(data);
                }
            );
            return false;
        });

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf]').attr("content"));
                }
            }
        });

        window.setInterval(
            function () {
                $('.commentsdiv').each(function () {
                    $(this).load($(this).data('url'));
                })
            },
            5000
        );


    }
);

$('.blog-edit-link').click(function () {
    $('#myModal').modal('show');
    $('.dialog').load($(this).attr('href'));
    return false;
})
