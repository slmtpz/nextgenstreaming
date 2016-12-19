function playRTMP(src){

    var flashvars={autoPlay:'true',src:escape(src),streamType:'live',scaleMode:'letterbox',};
    var params={allowFullScreen:'true',allowScriptAccess:'always',wmode:'opaque'};
    var attributes={id:'player'};
    swfobject.embedSWF('https://www.hlsplayer.net/player/grindplayer/GrindPlayer.swf','player','640','480','10.2',null,flashvars,params,attributes);
}
