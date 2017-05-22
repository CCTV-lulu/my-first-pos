$(document).ready(function () {
    $('button').click(function(){
        var id=$(this).attr('id')
    })
    $.ajax({
        type:'POST',
        url:"/payment",
        data:{id:id}

    })
})