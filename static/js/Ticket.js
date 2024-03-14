function myRandom(hrs, mins) {
    hrs = Math.round(Math.random()*hrs);
    mins = Math.round(Math.random()*mins);    
    var hFormat = (hrs<10 ? "0" : "");
    var mFormat = (mins<10 ? "0" : "");
    return hFormat+hrs+ ":" +mFormat+mins;
}

var myDate = new Date();
var myHour = myDate.getUTCHours();
var myMinutes = myDate.getMinutes();

async function FindTiket(){
    data = {}
    data['language'] = "ru"
    data['start'] = $(".filter #start").val()
    data['end'] = $(".filter #end").val()
    data['date'] = $(".filter #dateStart").val()

    answer = await fetch(`http://127.0.0.1:8080/api/way/{wayes}`, {method: "POST",
                                                    headers: { "Content-type": "application/json" },
                                                    body: JSON.stringify(data)})
    var info = JSON.parse(await answer.text())
    
    for(i in info){
        random_minute = myRandom(myHour, myMinutes)
        start_data = data['date'].split("-")
        start_data = start_data[2] + "." + start_data[1] + "." + start_data[0]

        for(j in info[i]){
            info[i][j]['start-date'] = start_data
            info[i][j]['start-time'] = random_minute
            times = myRandom(myHour, myMinutes)
            if (random_minute > times){
                date = info[i][j]['start-date'].split(".")
                s = parseInt(date[0]) + 1
                s < 10 ? s = "0"+s : s
                new_date = s + "." + date[1] + "." + date[2]
                
                info[i][j]['end-date'] = new_date
                info[i][j]['end-time'] = times
                
                random_minute = times
                start_data = new_date
            }
            else{
                info[i][j]['end-date'] = start_data
                info[i][j]['end-time'] = times
                
                random_minute = times
                start_data = info[i][j]['end-date']
            }
        }
    }
    
    $(".list").empty();
    for(i in info){
        transport = ""
        for(j in info[i]){
            info[i][j]['type'] == "air" ? transport += "✈️" : info[i][j]['type'] == "bus" ? transport += "🚘" : transport += "🚂"
        }
        first_poz = `<div class="ticket">
        <div class="titleTicket">
            <div style="text-align: center;">
                ${data['start']} -> ${transport}-> ${data['end']}
            </div>
            <div style="height: 2px; width: 90%; margin-left:5%; background-color: gray; border-radius: 2px;">
            </div>
        </div>
        <div class="bodyTicket">
            <div style="display: flex; flex-direction: row;">
                <div>
                    <div class="ShowPicture">
                        <div id="picture">
                            Наведи на меня
                        </div>
                        <div id="smena_kanpo_taymeru">
                        <img class="knopasa" src="https://4x4photo.ru/wp-content/uploads/2023/05/a40df128-0b36-47bd-a694-b57f1c97e9b1.jpg" style="height: 100%; width: 100%;" />
                            <img class="vesan" src="https://kakogo-chisla.ru/wp-content/uploads/2022/06/Den-fotografii-prirody-2048x1363.jpg" style="height: 100%; width: 100%;" />
                        </div>
                    </div>
                    
                </div>
                
                <div style="display: flex; flex-direction: row; padding: 15px">
                    <div>
                        <table style="width: 236px;">
                            <colgroup>
                                <col span="0" style="width: 74px;">
                                <col span="0" style="width: 49px;">
                                <col span="1" style="width: 15%;">
                             </colgroup>
                            <tbody>`
        table = ""
        time = "02:30"
        date = []
        for(j in info[i]){
            table += `<tr> <td>${info[i][j]['start']}</td> <td>${info[i][j]['start-date']}</td> <td>${info[i][j]['start-time']}</td></tr>`
        }
        table += `</tbody>
        </table>
    </div>
    <div>
        <table style="width: 236px; margin-left: 30px;">
            <tbody>
                <colgroup>
                    <col span="0" style="width: 74px;">
                    <col span="0" style="width: 49px;">
                    <col span="1" style="width: 15%;">
                 </colgroup>`
        table_2 = ""
        for(j in info[i]){
            table_2 += `<tr> <td>${info[i][j]['end']}</td> <td>${info[i][j]['end-date']}</td> <td>${info[i][j]['end-time']}</td></tr>`
        }
        table_2 += ` </tbody>
        </table>
    </div>
</div>
</div>
</div>
<div class="buyTicket">
<button onclick="Buy(this)">Купить</button>
</div>
</div>`
        text = first_poz + table + table_2
        $(".list").append(text)
    }
}

async function Buy(place){
    table = $($(place).parent("div").parent("div")).find(".bodyTicket table")
    count = 0
    info = []
    $($($(table[0]).children()[1]).children()).each(function(){
        info[count] = {"start": $($(this).children()[0]).text().trim(),
                       "date-Start": $($(this).children()[1]).text().trim(),
                       "time-Start": $($(this).children()[2]).text().trim(),
                       "end": null,
                       "date-end": null,
                       "time-end": null
                    }
        count +=1
    } 
    )
    s = 0
    $($($(table[1]).children()[2]).children()).each(function(){
        info[s]['end'] = $($(this).children()[0]).text().trim()
        info[s]["date-end"] = $($(this).children()[1]).text().trim()
        info[s]["time-end"] = $($(this).children()[2]).text().trim()
        s+=1
    } 
    )
    
    var arrStr = encodeURIComponent(JSON.stringify(info));
    location.href = `http://127.0.0.1:8000/web/buy/tiket?count=${count}&transport=${arrStr}`;

}