let session = document.getElementById('session').textContent;
let string = ''
let part_session = session.split(',')
for (let variable in part_session) {
    if (part_session[variable].includes('_user_id')) {
        let user = part_session[variable].split(':')
        string = user[1]
    }
}

function insert_data() {
    let data = get_data(string)
    fetch(`/api/profiles`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then((response) => response.json())
        .then(() => {
            swal("You have changed profile")
                .then(() => {
                    window.location = '/profile';
                });
        })
}

function get_data(string) {
    let name = document.getElementById("first_name").value;
    let lastname = document.getElementById("last_name").value;
    let email = document.getElementById("email").value;
    let location = document.getElementById("location").value;
    let identifier = string.replace("'", "");
    let res = identifier.replace("'", "");
    return {
        'name': name,
        'lastname': lastname,
        'email': email,
        'location': location,
        'identifier': res
    }
}