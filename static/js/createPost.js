var myModal

function createPost(){
    myModal = new bootstrap.Modal(document.getElementById('CreatePost'))
    myModal.show()
}

async function SavePost(id){
    var main = $("#CreatePost .modal-dialog .modal-content .modal-body")
    data = {}
    data['title'] = $($(main).find("#exampleFormControlInput1")).val()
    data['discribe'] = $($(main).find("#exampleFormControlTextarea1")).val()
    data['image'] = $($(main).find("#exampleFormControlTextarea2")).val().replace("\n", " ")
    
    answer = await fetch(`http://127.0.0.1:8080/api/post/create/${id}`, {method: "POST",
                                                                         headers: { "Content-type": "application/json" },
                                                                         body: JSON.stringify(data)})
    var info = JSON.parse(await answer.text())
    if (answer.statusText == "OK"){
        myModal.hide()    

        var img = data['image'].split(" ")[0]
        $(".story-post").append(`
        <div class="card" style="width: 18rem;">
                    <img src="${img}" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">${data['title']}</h5>
                      <p class="card-text"><span class="d-inline-block text-truncate" style="max-width: 600px;">
                      ${data['discribe']}
                    </span></p>
                      <a href="/web/main/post/1" class="btn btn-primary">Читать статью...</a>
                    </div>
        </div>
        `)

        
        var help = document.getElementById("liveToast")
        document.getElementById("helpcolor").style.background = "green"
        document.getElementById("helptitle").innerHTML = "Успех!"
        document.getElementById("helpbody").innerHTML = "Данные были обновлены"
        var s = new bootstrap.Toast(document.getElementById("liveToast")).show()
    }
    else{

        myModal.hide()
        var help = document.getElementById("liveToast")
        document.getElementById("helpcolor").style.background = "red"
        document.getElementById("helptitle").innerHTML = "Ошибка!"
        document.getElementById("helpbody").innerHTML = "Ошибка обновления, повторите попытку позде"
        var s = new bootstrap.Toast(document.getElementById("liveToast")).show()
    } 
}

