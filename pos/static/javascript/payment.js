$(document).ready(function () {
    $('#sure').click(function(){
        var id=$(this).attr('id')
        console.log(11111)
    })
    $.ajax({
        type:'POST',
        url:"/payment",
        data:{id:id},


    })
})