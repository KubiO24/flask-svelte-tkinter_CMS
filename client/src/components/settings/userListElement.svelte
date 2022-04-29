<script>
    import { onMount } from 'svelte';

    export let user;
    let originalUsername = user[0];
    let element_username, element_email, element_password, element_permission, element_firstButton, element_secondButton;
    let firstButton_action = edit;
    let secondButton_action = Delete;

    onMount(async () => {
		element_username = document.getElementById(`userList_username_${originalUsername}`);
        element_email = document.getElementById(`userList_email_${originalUsername}`);
        element_password = document.getElementById(`userList_password_${originalUsername}`);
        element_permission = document.getElementById(`userList_permission_${originalUsername}`);
        element_firstButton = document.getElementById(`userList_firstButton_${originalUsername}`);
        element_secondButton = document.getElementById(`userList_secondButton_${originalUsername}`);
	});

    function edit() {
        element_username.contentEditable = true;
        element_username.style.fontStyle = 'italic';

        element_email.contentEditable = true;
        element_email.style.fontStyle = 'italic';

        element_password.contentEditable = true;
        element_password.style.fontStyle = 'italic';

        element_permission.contentEditable = true;
        element_permission.style.fontStyle = 'italic';

        element_firstButton.innerHTML = "Save";
        element_firstButton.style.backgroundColor = "#45a13c";
        firstButton_action = save;

        element_secondButton.innerHTML = "Discard";
        element_secondButton.style.backgroundColor = "#ff5353";
        secondButton_action = discard;
    }

    function save() {
        element_username.contentEditable = false;
        element_username.style.fontStyle = 'normal';

        element_email.contentEditable = false;
        element_email.style.fontStyle = 'normal';

        element_password.contentEditable = false;
        element_password.style.fontStyle = 'normal';

        element_permission.contentEditable = false;
        element_permission.style.fontStyle = 'normal';

        element_firstButton.innerHTML = "Edit";
        element_firstButton.style.backgroundColor = "#43b9ce";
        firstButton_action = edit;

        element_secondButton.innerHTML = "Delete";
        element_secondButton.style.backgroundColor = "#ff5353";
        secondButton_action = Delete;
    }

    function discard() {
        element_username.contentEditable = false;
        element_username.style.fontStyle = 'normal';

        element_email.contentEditable = false;
        element_email.style.fontStyle = 'normal';

        element_password.contentEditable = false;
        element_password.style.fontStyle = 'normal';

        element_permission.contentEditable = false;
        element_permission.style.fontStyle = 'normal';

        element_firstButton.innerHTML = "Edit";
        element_firstButton.style.backgroundColor = "#43b9ce";
        firstButton_action = edit;

        element_secondButton.innerHTML = "Delete";
        element_secondButton.style.backgroundColor = "#ff5353";
        secondButton_action = Delete;
    }

    function Delete() {
        console.log("Delete")
    }


</script>

<tr>
    <td id="userList_username_{originalUsername}">{user[0]}</td>
    <td id="userList_email_{originalUsername}">{user[1]}</td>
    <td id="userList_password_{originalUsername}">{user[2]}</td>
    <td id="userList_permission_{originalUsername}">{user[3]}</td>
    <td style='display: flex; justify-content: space-evenly;'>
        <button id='userList_firstButton_{originalUsername}' style="background-color: #43b9ce;" on:click={firstButton_action}>Edit</button>
        <button id='userList_secondButton_{originalUsername}' style="background-color: #ff5353;" on:click={secondButton_action}>Delete</button>
    </td>
</tr>

<style>
    
    td {
        text-align: center;
        padding: 8px;
    }
    
    td {
        border-right: 1px solid #f8f8f8;
        font-size: 12px;
    }
    
    td button {
        padding: 5px 10px;
        color: white !important;
        border: none;
    }
    
    tr:nth-child(even) {
        background: #F8F8F8;
    }
    
    /* Responsive */
    
    @media (max-width: 1100px) {
        td {
            padding: 20px .625em .625em .625em;
            height: 60px;
            vertical-align: middle;
            box-sizing: border-box;
            overflow-x: hidden;
            overflow-y: auto;
            width: 120px;
            font-size: 13px;
            text-overflow: ellipsis;
        }
        tr {
            display: table-cell;
        }
        tr:nth-child(odd) {
            background: none;
        }
        tr:nth-child(even) {
            background: transparent;
        }
        tr td:nth-child(odd) {
            background: #F8F8F8;
            border-right: 1px solid #E6E4E4;
        }
        tr td:nth-child(even) {
            border-right: 1px solid #E6E4E4;
        }
        td {
            display: block;
            text-align: center;
        }
    }
</style>