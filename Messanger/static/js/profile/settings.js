let session = document.getElementById('session').textContent;
let string = ''
let part_session = session.split(',')
for (let variable in part_session) {
    if (part_session[variable].includes('UUID')) {
        let user = part_session[variable].split(':')
        string = user[1]
    }
}
let identifier = document.URL.substring(document.URL.lastIndexOf('/') + 1);

function checker_where_are_you() {
    if (identifier.includes('profile')) {
        deleter()
    } else if (identifier.includes('settings')) {
        insert_data()
    } else {
        change_data()
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

function change_data() {
    let data = get_data(string)
    fetch(`/api/profiles`, {
        method: 'PUT',
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

function get_identifier_to_delete(string) {
    let identifier = string.replace("'", "");
    let res = identifier.replace("'", "");
    return {
        'name': null,
        'lastname': null,
        'email': null,
        'location': null,
        'identifier': res
    }
}

function deleter() {
    let data = get_identifier_to_delete(string)
    fetch(`/api/profiles`, {
        method: 'DELETE',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then((response) => response.json())
        .then(() => {
            alert("You have deleted your account")
                .then(() => {
                    window.location = '/profile';
                });
        })
}