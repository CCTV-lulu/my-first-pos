$(document).ready(function () {
    $(".input").click(function(){
        var id=$(this).attr('id')
        $.ajax({
            type:'POST',
            url:'/shopping_list/',
            data:{id:id},
            success:function(sum_count){
                $("#number").text(sum_count)
            }

       })
    })
})
