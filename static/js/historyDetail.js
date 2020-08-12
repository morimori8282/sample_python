$(function(){
    // 計算
    changeScore();

});

// 自動計算
function changeScore(){
    var roundCnt = document.getElementById('roundCount').value;
    // var userCnt = document.getElementById('userCount').value;
    // var userCnt = [];
    var userScore = {};

    // ラウンド合計
    for(var i = 1; i <= roundCnt; i++){
        var sumRoundScore = 0;
        var elements = document.getElementsByClassName('scoreRound-' + i)
        for (var j = 0; j < elements.length; j++) {
            // ラウンド合計算出
            sumRoundScore += Number(elements[j].value.replace(/,/g, ''));

            if(i == 1){
                // userId取得
                var userId = elements[j].className.match(/scoreUser-\d+/)[0].replace('scoreUser-', '');
                // ユーザ配列にuserIdを設定(値は0)
                userScore[userId] = 0;
            }
        }
        // ラウンド合計に値を設定
        document.getElementById('roundTotal-' + i).innerText = sumRoundScore;
    }

    // ユーザ合計
    for (var key in userScore){
        var sumUserScore = 0;
        var elements = document.getElementsByClassName('scoreUser-' + key)
        for (var j = 0; j < elements.length; j++) {
            sumUserScore += Number(elements[j].value.replace(/,/g, ''));
        }
        // ユーザ合計に値を設定
        document.getElementById('userTotal-' + key).innerText = sumUserScore;
        // ユーザ配列にscoreを設定
        userScore[key] = sumUserScore;
    }


    // ランク
    var keys=[];
    for(var key in userScore)keys.push(key);
    
    // ユーザ配列のソート
    function Compare(a,b){
        return userScore[b]-userScore[a];    
    }    
    keys.sort(Compare);
    console.log(keys);

    var rankCounter = 1;
    for(var key in keys){
        // ランクの設定
        document.getElementById('userRank-' + keys[key]).innerText = rankCounter;
        rankCounter++;
    }

    // // ランク
    // for (var key in userScore){
    //     var elements = document.getElementsByClassName('scoreUser-' + i)
    //     for (var j = 0; j < elements.length; j++) {
    //         sumUserScore += Number(elements[j].value.replace(/,/g, ''));
    //     }        
    //     document.getElementById('userTotal-' + i).innerText = sumUserScore;
    // }
}