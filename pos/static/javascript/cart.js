$(document).ready(function () {
    $("button").click(function () {
      var id=$(this).attr('id')
      var group=$(this).attr('class')
        if(group=='left'){
          count=-1
        }
        else if(group=='right'){
            count=1
        }
      $.ajax({
          type:'POST',
          url:'/shopping_cart',
          data:{id:id,count:count},
          success:function(result){
              $($('#'+id).next()).text(result.quantity)
              $((($('#'+id).parent()).parent()).next()).text(result.total+'元')
              $('#number').text(result.sum_count)
          }
      })
    })
})
