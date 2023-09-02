//const { data } = require("jquery");

var host = window.location.host;

function format(lis){
    
    let table_html = `<table>
                        <tbody>
                            <tr class="title">
                                <th id="c">File Name</th>
                                <th id="c">File Type</th>
                                <th id="c">Size</th>
                                <th id="c">Date</th>
                                <th>User</th>
                            </tr>`
    //loop here
    for (let dict = 0; dict < lis.length; dict++){
        //format html here
        table_html += `<tr class="row">
                            <td id="c">
                                <a href="/api/download/${lis[dict]['file_name']}.${lis[dict]['file_type']}@ID=${lis[dict]['id']}"
                                 download="">
                                 ${lis[dict]['file_name']} </a>
                            </td>
                            <td id="c">${lis[dict]['file_type']}</td>
                            <td id="c">${lis[dict]['file_size']} ${lis[dict]['unit']}</td>
                            <td id="c">${lis[dict]['date']}</td>
                            <td id="cl">${lis[dict]['username']}</td>
                        </tr>`
    }
    //end loop
    table_html += `</tbody></table>`
    //return formatted string
    console.log(table_html)
    return table_html;
}

fetch('/api/downloadable')
    .then(Response => Response.json())
    .then( data => 
        document.getElementById('table').innerHTML = format(data) //data.list[num] to access item
    ).catch(error => console.log(error));

console.log('bruhh')