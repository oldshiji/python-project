
$(function(){
	// tab
	$(document).on('click', '[data-toggle^="class"]', function(e){
	  e && e.preventDefault();
	  console.log('abc');
	  var $this = $(e.target), $class , $target, $tmp, $classes, $targets;
	  !$this.data('toggle') && ($this = $this.closest('[data-toggle^="class"]'));
	  $class = $this.data()['toggle'];
	  $target = $this.data('target') || $this.attr('href');
	  $class && ($tmp = $class.split(':')[1]) && ($classes = $tmp.split(','));
	  $target && ($targets = $target.split(','));
	  $classes && $classes.length && $.each($targets, function( index, value ) {
		if ( $classes[index].indexOf( '*' ) !== -1 ) {
		  var patt = new RegExp( '\\s' + 
			  $classes[index].
				replace( /\*/g, '[A-Za-z0-9-_]+' ).
				split( ' ' ).
				join( '\\s|\\s' ) + 
			  '\\s', 'g' );
		  $($this).each( function ( i, it ) {
			var cn = ' ' + it.className + ' ';
			while ( patt.test( cn ) ) {
			  cn = cn.replace( patt, ' ' );
			}
			it.className = $.trim( cn );
		  });
		}
		($targets[index] !='#') && $($targets[index]).toggleClass($classes[index]) || $this.toggleClass($classes[index]);
	  });
	  $this.toggleClass('active');
	});

	// collapse nav
	$(document).on('click', 'nav a', function (e) {
	  var $this = $(e.target), $active;
	  $this.is('a') || ($this = $this.closest('a'));
	  
	  $active = $this.parent().siblings( ".active" );
	  $active && $active.toggleClass('active').find('> ul:visible').slideUp(200);
	  
	  ($this.parent().hasClass('active') && $this.next().slideUp(200)) || $this.next().slideDown(200);
	  $this.parent().toggleClass('active');
	  
	  $this.next().is('ul') && e.preventDefault();

	  setTimeout(function(){ $(document).trigger('updateNav'); }, 300);      
	});
  });
	  
//下拉输入框
function openShutManager(oSourceObj,oTargetObj,shutAble,oOpenTip,oShutTip){
var sourceObj = typeof oSourceObj == "string" ? document.getElementById(oSourceObj) : oSourceObj;
var targetObj = typeof oTargetObj == "string" ? document.getElementById(oTargetObj) : oTargetObj;
var openTip = oOpenTip || "";
var shutTip = oShutTip || "";
if(targetObj.style.display!="none"){
   if(shutAble) return;
   targetObj.style.display="none";
   if(openTip  &&  shutTip){
    sourceObj.innerHTML = shutTip; 
   }
} else {
   targetObj.style.display="block";
   if(openTip  &&  shutTip){
    sourceObj.innerHTML = openTip; 
   }
}
}

//图片上传预览    IE是用了滤镜。
	function previewImage(file)
	{
	  var MAXWIDTH  = 260; 
	  var MAXHEIGHT = 180;
	  var div = document.getElementById('preview');
	  if (file.files && file.files[0])
	  {
		  div.innerHTML ='<img id="img_path">';
		  var img = document.getElementById('img_path');
		  img.onload = function(){
			var rect = clacImgZoomParam(MAXWIDTH, MAXHEIGHT, img.offsetWidth, img.offsetHeight);
			img.width  =  rect.width;
			img.height =  rect.height;
//                 img.style.marginLeft = rect.left+'px';
			img.style.marginTop = rect.top+'px';
		  }
		  var reader = new FileReader();
		  reader.onload = function(evt){img.src = evt.target.result;}
		  reader.readAsDataURL(file.files[0]);
	  }
	  else //兼容IE
	  {
		var sFilter='filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod=scale,src="';
		file.select();
		var src = document.selection.createRange().text;
		div.innerHTML = '<img id=imghead>';
		var img = document.getElementById('imghead');
		img.filters.item('DXImageTransform.Microsoft.AlphaImageLoader').src = src;
		var rect = clacImgZoomParam(MAXWIDTH, MAXHEIGHT, img.offsetWidth, img.offsetHeight);
		status =('rect:'+rect.top+','+rect.left+','+rect.width+','+rect.height);
		div.innerHTML = "<div id=divhead style='width:"+rect.width+"px;height:"+rect.height+"px;margin-top:"+rect.top+"px;"+sFilter+src+"\"'></div>";
	  }
	}
	function clacImgZoomParam( maxWidth, maxHeight, width, height ){
		var param = {top:0, left:0, width:width, height:height};
		if( width>maxWidth || height>maxHeight )
		{
			rateWidth = width / maxWidth;
			rateHeight = height / maxHeight;
			
			if( rateWidth > rateHeight )
			{
				param.width =  maxWidth;
				param.height = Math.round(height / rateWidth);
			}else
			{
				param.width = Math.round(width / rateHeight);
				param.height = maxHeight;
			}
		}
		
		param.left = Math.round((maxWidth - param.width) / 2);
		param.top = Math.round((maxHeight - param.height) / 2);
		return param;
	}
	
	//$('.add-btn').click(function(){  
			//$(this).parent().find('.add-btn').addClass('btn-primary');
		//})