<script>
    import { onMount } from 'svelte';

    export let user;
    let originalUsername = user[0];
    let element_username, element_email, element_password, element_permission, element_firstButton, element_secondButton;

    onMount(async () => {
		element_username = document.getElementById('userList_username');
        element_email = document.getElementById('userList_email');
        element_password = document.getElementById('userList_password');
        element_permission = document.getElementById('userList_permission');
        element_firstButton = document.getElementById('userList_firstButton');
        element_secondButton = document.getElementById('userList_secondButton');
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
        element_firstButton.style.backgroundColor = "#4fce43";
        element_secondButton.innerHTML = "Discard";
    }

    function save() {
        return;
    }

    function discard() {
        return
    }


</script>

<tr>
    <td id="userList_username">{user[0]}</td>
    <td id="userList_email">{user[1]}</td>
    <td id="userList_password">{user[2]}</td>
    <td id="userList_permission">{user[3]}</td>
    <td style='display: flex; justify-content: space-evenly;'>
        <button id='userList_firstButton' on:click={edit} style="background-color: #43b9ce;">Edit</button>
        <button id='userList_secondButton' style="background-color: #ff5353;">Delete</button>
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
        color: white;
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