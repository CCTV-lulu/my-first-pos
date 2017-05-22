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
              $('#'+id).next().text(result.quantity)
              if(result.free_count>0) {
                  $('#' + id).parent().parent().next().text(result.total.toFixed(1) + '元' + '(' + '原价:' + result.totality.toFixed() +'元'+')' )
              }
              else{
                  $('#'+id).parent().parent().next().text(result.total+'元')
              }
              $('#number').text(result.sum_count)
              if(result.sum_count==0){
                    location.href='/shopping_list';
                }
              $('#sum_count').text('总计：'+result.sum_total.toFixed(2)+'元')
              if(result.quantity==0){
                   $('#'+id).parents('tr').detach()
              }
          }
      })
    })
})