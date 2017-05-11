$(document).ready(function () {
    $(".input").click(function(){
        var arr=$(this).attr('id')
        console.log(arr)
        $.ajax({
            type:'POST',
            url:'/shopping_list/',
            data:{id:arr},
            success:function(sum_count){
                console.log(sum_count);
                $("#number").text(sum_count)
            }

       })
    })
})
