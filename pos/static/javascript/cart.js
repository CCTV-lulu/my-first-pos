$(document).ready(function () {
    $("button").click(function () {
      var id=$(this).attr('id')
      var group=$(this).attr('class')
        if(group=='left'){
          count=-1
        }
        else{
            count=1
        }
      $.ajax({
          type:'POST',
          url:'/shopping_cart',
          data:{id:id,count:count},
          success:function(count){
              $($('#'+id).next()).text(count)
          }
      })
    })
})
