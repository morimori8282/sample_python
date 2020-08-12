$(document).ready(function(){
    //テキストボックスにフォーカスが当たった時に実行
    $("input[type='text']").focus(function(){
      //全選択にする
      $(this).select();
    });
  });