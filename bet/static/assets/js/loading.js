$(function() {

    $('#submitBtnLol').button().click(function(event) {
        event.preventDefault(event);
        console.log("SAJNDOASHJDOIASJDIOAJSDIOASJDOILSAJDIOASJDOISAJD")
        $('#submitBtnLol').hide();
        $('#loading').show();
        $('#formSummoner').submit();// Tempo de simulação em milissegundos
      });

});