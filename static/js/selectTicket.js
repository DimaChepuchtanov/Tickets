var pla
var model

function SelectTicket(place, modl){
    pla = $(place)
    modal = new bootstrap.Modal(document.getElementById(modl))
    modal.show()
}


function SaveTicket(modl){
    $($($(pla).parent("div").parent("div").children()[3]).find("#countPlace")).html($($(`#${modl} .modal-content .modal-body .InfoBUy #countPlace`)).text().trim())
    $($($(pla).parent("div").parent("div").children()[3]).find("#NumberPlace")).html($($(`#${modl} .modal-content .modal-body .InfoBUy #NumberPlace`)).text())
    $($(pla).parent("div").parent("div").children()[4]).html('Персональные данные: Введены')
    modal.hide()
}