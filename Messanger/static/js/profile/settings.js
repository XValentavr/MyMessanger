    fetch(`/api/departments/${identifier}`)
        .then((response) => response.json())
        .catch(() => {
            swal("There is no this department. Please select currect department")
                .then(() => {
                    window.location = '/departments';
                });
        })