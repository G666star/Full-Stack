$('h1').mouseover(function () {
	console.log('lelo')
	// body...
})

$('input').eq(1).mouseover(function(){
    $(this).val('chal be')})

$('input').eq(1).mouseout(function(){
    $(this).val('muh toh band karo uncle')})

$('input').eq(1).click(function(){
    $(this).attr('type','checkbox')})