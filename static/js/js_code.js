

function getUsers(user_id_front){
    console.log('click');
    fetch('https://reqres.in/api/users/').then(
        response => response.json() //removing from json to object
        ).then( response_obj => put_users_inside_html(response_obj.data,user_id_front)
    ).catch(
        err => console.log(err)
    )
}

// Get users from front-end
function put_users_inside_html(response_obj_data,user_id_front){
    //console.log(response_obj_data);
    const curr_main = document.querySelector("main")
    for (let user of response_obj_data){
       if (user.id == user_id_front) {
           const section = document.createElement('section');
           section.innerHTML = `
           <img src="${user.avatar}" alt = "picture"/>
           <div>
              <span>${user.first_name} ${user.last_name}</span>
              <br>
              <a href="mail_to:${user.email}">send email</a>
           </div>
          `;
             curr_main.append(section); //Must to do in order to present the html tag
       }
    }
}

