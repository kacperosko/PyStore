function LikeComment(comment_id) {
    $.ajax({
        type: "GET",
        url: "/ajax/likecomment",
        dataType: 'json',
        contentType: 'application/json; encode=UTF-8',
        beforeSend: function (jqXHR) {
            jqXHR.setRequestHeader('X-CSRFToken', $('input[name=csrfmiddlewaretoken]').val());
        },
        data: {
            comment_id: comment_id,
            isliked: !$('#like-' + comment_id).is(':checked')
        },
        success: function (data) {
            document.getElementById('like-count-' + comment_id).innerHTML = data.counter > 0 ? data.counter : "";
        },
        error: function ($xhr, textStatus, errorThrown) {
            $('#like-' + comment_id).prop("checked", false);
            // @ts-ignore
            Alert.error(JSON.parse($xhr.responseText).message, 'Oh no what a green mess!', { displayDuration: 5000, pos: 'top' });
        }
    });
}
