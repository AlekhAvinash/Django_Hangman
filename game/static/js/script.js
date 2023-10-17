function start(){
    console.log("hello!")
    $('#keycover').addClass("d-none");
    for (i = 97; i <= 122; i++) {
        $.id = "#button-".concat(String.fromCharCode(i));
        if($($.id).hasClass("btn-outline-primary")==false){
            if($($.id).hasClass("btn-outline-success")){
                $($.id).removeClass("disabled btn-outline-success");
            }
            else{
                $($.id).removeClass("disabled btn-outline-danger");
            }
            $($.id).addClass("btn-outline-primary")
        }
    }
    for(i = 49; i <= 54; i++) {
        $("#itd-".concat(String.fromCharCode(i))).attr('stroke', 'white');
    }
    if($("#rEyes").hasClass("d-none")){
        $("#xEyes").addClass("d-none");
        $("#rEyes").removeClass("d-none");
    }
    $.ajax({
        type: 'POST',
        url: '/',
        data: {
            opt:'start',
            val:$(this).text()
        },
        success: function(data){
            $("#xtcword").text(data.out);
            $("#xtcscre").text(data.ptr);
        },
        error: function(error){
            console.log(error);
        }
    })
}

$(document).ready(start);
$('#keycover').click(start);
$('.xtcbtn').click(function(){
    $.ajax({
        type: 'POST',
        url: '/',
        data: {
            opt:'update',
            val:$(this).text()
        },
        success: function(data){
            $.id = "#button-".concat(data.val);
            $($.id).removeClass("btn-outline-primary");
            $($.id).addClass("disabled btn-outline-".concat(data.stk));
            $("#xtcscre").text(data.ptr);
            $("#xtcword").text(data.out);
            if(data.ctr>0 && data.ctr<7){
                $("#itd-".concat(data.ctr)).attr('stroke', 'var(--bs-danger)');
            }
            if(data.win){
                $("#keycover").removeClass("d-none");
            }
            if(data.ctr>=7){
                $("#rEyes").addClass("d-none");
                $("#xEyes").removeClass("d-none");
                $("#keycover").removeClass("d-none");
            }
        },
        error: function(error){
            console.log(error);
        }
    })
});