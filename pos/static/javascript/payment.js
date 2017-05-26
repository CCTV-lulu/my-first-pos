$(document).ready(function () {
    $(".sure").click(function(){
        var id=$(this).attr('id')
        $.ajax({
            type:'POST',
            url:'/payment',
            data:{id:id},
            success:function () {
                location.href="/shopping_list"
            }
         })
    })
})