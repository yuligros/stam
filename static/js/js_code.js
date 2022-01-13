console.log('inside fetch example')


// users to json file
function getUsers(users){
   const myJSON_users = JSON.stringify(users);
   return myJSON_users;
   const curr_main = document.querySelector("main")
   const section = document.createElement('section');
        section.innerHTML = `
        <div>
            <span>myJSON_users</span>
        </div>
        `;
        curr_main.append(section); //Must to do in order to present the html tag
}


function getUsers(){
    console.log('click');
    fetch('https://reqres.in/api/users/').then(
        response => response.json() //removing from json to object
        ).then( response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

// Get users from front-end
function put_users_inside_html(response_obj_data){
    //console.log(response_obj_data);
    const curr_main = document.querySelector("main")
    for (let user of response_obj_data){
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


// function getUsers_to_json(users) {
//     const users_json = JSON.stringify(users);
//     const curr_main = document.querySelector("main")
//     for (let user of users_json) {
//         const section = document.createElement('section');
//         section.innerHTML = `
//         <div>
//            <span>${user.id}</span>
//            <br>
//             <span>${user.user_name}</span>
//             <br>
//             <a href="mail_to:${user.email}">send email</a>
//         </div>
//         `;
//         curr_main.append(section); //Must to do in order to present the html tag
//         return users_json;
//     }
// }