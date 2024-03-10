async function Create(id){
    answer = await fetch(`http://127.0.0.1:8080/api/token/create/${id}`, {method: "GET",
                                                                         headers: { "Content-type": "application/json" },
                                                                         })
    var info = JSON.parse(await answer.text())
    if (answer.statusText == "OK"){  
        answer = await fetch(`http://127.0.0.1:8080/api/token/show/${id}`, {method: "GET",
                                                                         headers: { "Content-type": "application/json" },
                                                                         })
        var info = JSON.parse(await answer.text())
        $(".profile .col .form-control").val(info['status'])
        
        $(".profile .col p").remove();
        var help = document.getElementById("liveToast")
        document.getElementById("helpcolor").style.background = "green"
        document.getElementById("helptitle").innerHTML = "Успех!"
        document.getElementById("helpbody").innerHTML = "Данные были обновлены"
        var s = new bootstrap.Toast(document.getElementById("liveToast")).show()
    }
    else{
        var help = document.getElementById("liveToast")
        document.getElementById("helpcolor").style.background = "red"
        document.getElementById("helptitle").innerHTML = "Ошибка!"
        document.getElementById("helpbody").innerHTML = "Ошибка обновления, повторите попытку позде"
        var s = new bootstrap.Toast(document.getElementById("liveToast")).show()
    } 
}

async function update(id){
    answer = await fetch(`http://127.0.0.1:8080/api/token/update/${id}`, {method: "GET",
                                                                         headers: { "Content-type": "application/json" },
                                                                         })
    var info = JSON.parse(await answer.text())
    if (answer.statusText == "OK"){  
        answer = await fetch(`http://127.0.0.1:8080/api/token/show/${id}`, {method: "GET",
                                                                         headers: { "Content-type": "application/json" },
                                                                         })
        var info = JSON.parse(await answer.text())
        $(".profile .col .form-control").val(info['status'])
        
        var help = document.getElementById("liveToast")
        document.getElementById("helpcolor").style.background = "green"
        document.getElementById("helptitle").innerHTML = "Успех!"
        document.getElementById("helpbody").innerHTML = "Данные были обновлены"
        var s = new bootstrap.Toast(document.getElementById("liveToast")).show()
    }
    else{
        var help = document.getElementById("liveToast")
        document.getElementById("helpcolor").style.background = "red"
        document.getElementById("helptitle").innerHTML = "Ошибка!"
        document.getElementById("helpbody").innerHTML = "Ошибка обновления, повторите попытку позде"
        var s = new bootstrap.Toast(document.getElementById("liveToast")).show()
    } 
}